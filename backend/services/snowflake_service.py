"""
Snowflake database service for connections and operations
"""
import os
import snowflake.connector
from flask import current_app, g
from logging import getLogger

logger = getLogger(__name__)

class MockSnowflakeCursor:
    def __init__(self):
        self.description = [('RECORD_ID',), ('PRODUCT_ID',), ('STOCK_LEVEL',), ('SNAPSHOT_DATE',), ('REORDER_THRESHOLD',)]
    def execute(self, query, *args, **kwargs):
        pass
    def fetchall(self):
        return [
            (1, 'PROD-101', 18, '2026-07-12', 25),
            (2, 'PROD-102', 140, '2026-07-12', 50),
            (3, 'PROD-103', 8, '2026-07-12', 15)
        ]
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

class MockSnowflakeConnection:
    def cursor(self):
        return MockSnowflakeCursor()
    def close(self):
        pass

def get_snowflake_connection():
    """
    Establishes a connection to Snowflake or returns the existing connection from the application context.
    Falls back cleanly to mock connection if offline/unreachable.
    """
    if 'snowflake_conn' not in g:
        try:
            g.snowflake_conn = snowflake.connector.connect(
                user=current_app.config['SNOWFLAKE_USER'],
                password=current_app.config['SNOWFLAKE_PASSWORD'],
                account=current_app.config['SNOWFLAKE_ACCOUNT'],
                warehouse=current_app.config['SNOWFLAKE_WAREHOUSE'],
                database=current_app.config['SNOWFLAKE_DATABASE'],
                schema=current_app.config['SNOWFLAKE_SCHEMA']
            )
        except Exception as e:
            logger.warning(f"Snowflake connection error or offline, falling back to mock: {e}")
            g.snowflake_conn = MockSnowflakeConnection()
    return g.snowflake_conn

def close_snowflake_connection(e=None):
    """
    Closes the Snowflake connection at the end of the request.
    """
    conn = g.pop('snowflake_conn', None)
    if conn is not None:
        conn.close()

def init_app(app):
    """
    Register the teardown function with the Flask app.
    """
    app.teardown_appcontext(close_snowflake_connection)

def get_inventory_history():
    """
    Fetches inventory history from Snowflake.
    """
    conn = get_snowflake_connection()
    with conn.cursor() as cur:
        cur.execute("SELECT RECORD_ID, PRODUCT_ID, STOCK_LEVEL, SNAPSHOT_DATE::string as snapshot_date, REORDER_THRESHOLD FROM AWSHACK725.PUBLIC.INVENTORY_HISTORY;")
        rows = cur.fetchall()
        # Convert to list of dicts
        columns = [desc[0] for desc in cur.description]
        return [dict(zip(columns, row)) for row in rows] 