"""
Database service for MongoDB connections and operations
"""
import structlog
import logging
import certifi
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure
from flask import current_app, g

logger = structlog.get_logger()

# Global MongoDB client
mongo_client = None
mongo_db = None


def _seed_sample_data(db):
    """Seed rich sample data into mock database for local development and testing"""
    from datetime import datetime
    if db.products.count_documents({}) == 0:
        db.products.insert_many([
            {
                "product_id": "PROD-101",
                "name": "Industrial Sensor X200",
                "category": "Electronics",
                "sku": "ELEC-SEN-200",
                "supplier_id": "SUPP-001",
                "current_stock": 18.0,
                "reorder_threshold": 25.0,
                "reorder_quantity": 100.0,
                "cost_price": 45.0,
                "selling_price": 89.99,
                "status": "active",
                "description": "High-precision thermal sensor for industrial HVAC"
            },
            {
                "product_id": "PROD-102",
                "name": "Microcontroller Unit MCU-32",
                "category": "Electronics",
                "sku": "ELEC-MCU-032",
                "supplier_id": "SUPP-001",
                "current_stock": 140.0,
                "reorder_threshold": 50.0,
                "reorder_quantity": 200.0,
                "cost_price": 12.5,
                "selling_price": 24.99,
                "status": "active",
                "description": "32-bit low-power IoT microcontroller"
            },
            {
                "product_id": "PROD-103",
                "name": "Hydraulic Valve V-500",
                "category": "Mechanical",
                "sku": "MECH-VAL-500",
                "supplier_id": "SUPP-002",
                "current_stock": 8.0,
                "reorder_threshold": 15.0,
                "reorder_quantity": 50.0,
                "cost_price": 120.0,
                "selling_price": 249.0,
                "status": "active",
                "description": "Heavy-duty brass hydraulic pressure valve"
            }
        ])
    if db.suppliers.count_documents({}) == 0:
        db.suppliers.insert_many([
            {
                "supplier_id": "SUPP-001",
                "name": "Apex Electronics Corp",
                "company_name": "Apex Electronics Corp",
                "contact_email": "orders@apexelectronics.com",
                "contact_phone": "+1-555-0192",
                "lead_time_days": 7,
                "rating": 4.8,
                "status": "active",
                "categories": ["Electronics"]
            },
            {
                "supplier_id": "SUPP-002",
                "name": "Midwest Industrial Supply",
                "company_name": "Midwest Industrial Supply",
                "contact_email": "sales@midwestindustrial.com",
                "contact_phone": "+1-555-0144",
                "lead_time_days": 14,
                "rating": 4.5,
                "status": "active",
                "categories": ["Mechanical"]
            }
        ])
    if db.alerts.count_documents({}) == 0:
        db.alerts.insert_many([
            {
                "alert_id": "ALT-001",
                "type": "low_stock",
                "severity": "high",
                "title": "Low Stock: Industrial Sensor X200",
                "message": "Stock level (18) fell below reorder threshold (25). AI recommends restocking 100 units.",
                "status": "active",
                "product_id": "PROD-101",
                "created_at": datetime.utcnow().isoformat() + "Z"
            }
        ])


def init_db(app):
    """Initialize database connection with offline/mock fallback"""
    global mongo_client, mongo_db
    
    db_name = app.config['MONGO_DB_NAME']
    try:
        mongo_uri = app.config['MONGO_URI']
        mongo_client = MongoClient(mongo_uri, tlsCAFile=certifi.where(), serverSelectionTimeoutMS=2000)
        mongo_db = mongo_client[db_name]
        mongo_client.admin.command('ping')
        logger.info("MongoDB connection established", database=db_name)
    except Exception as e:
        logger.warning("Failed to connect to MongoDB Atlas, running with local mock database fallback", error=str(e))
        import mongomock
        mongo_client = mongomock.MongoClient()
        mongo_db = mongo_client[db_name]
        _seed_sample_data(mongo_db)
    
    app.mongo_client = mongo_client
    app.mongo_db = mongo_db
    
    with app.app_context():
        create_indexes()


def get_db():
    """Get database instance"""
    if 'db' not in g:
        if hasattr(current_app, '_get_current_object'):
            app = current_app._get_current_object()
            if hasattr(app, 'mongo_db') and app.mongo_db is not None:
                g.db = app.mongo_db
            else:
                db_name = current_app.config['MONGO_DB_NAME']
                import mongomock
                g.db = mongomock.MongoClient()[db_name]
                _seed_sample_data(g.db)
    return g.db


def get_collection(collection_name):
    """Get a specific collection"""
    db = get_db()
    return db[collection_name]


def create_indexes():
    """Create database indexes for optimal performance"""
    # Indexes already exist in Atlas - skipping for hackathon
    logger.info("Skipping index creation - indexes already exist in Atlas")
    return


def close_db():
    """Close database connection"""
    global mongo_client
    if mongo_client:
        mongo_client.close()
        logger.info("MongoDB connection closed") 