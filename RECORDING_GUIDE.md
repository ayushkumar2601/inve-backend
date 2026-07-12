# InventoryPulse AI — Production Recording & Studio Execution Guide

This guide defines exact desktop, browser, mouse, and audio configurations required to record a flawless, studio-grade 1-minute 50-second demo walkthrough.

---

## 1. Technical Screen & Browser Configuration

* **Display Resolution**: Record at native **1920x1080 (Full HD 1080p 60fps)** or **2560x1440 (1440p 60fps)**. Never record at 30fps.
* **Window Size & Chrome**:
  * Run Google Chrome or Safari in clean full window mode (`1920x1080`).
  * Hide bookmarks bar (`Cmd+Shift+B`).
  * Disable all distracting browser extensions (Grammarly, ad blockers, notification badges).
* **Browser Zoom Level**: Set browser zoom to **100%** (default Apple Enterprise layout is precision-tuned for crisp 14px/16px SF Pro typography).
* **Operating System Cleanliness**:
  * Enable **Do Not Disturb / Focus Mode** on macOS/Windows to prevent Slack, calendar, or email notifications.
  * Hide desktop icons if recording full screen.

---

## 2. Cursor Pacing & Mouse Choreography

* **Cursor Speed**: Smooth, deliberate, executive pacing. Avoid rapid, jerky, or nervous mouse twitching.
* **Hover Dwell Time**: When pointing to a KPI card (e.g., **$378,046 Revenue at Risk** or **94.8% Confidence**), pause for **1.5 to 2 seconds** so judges can read the metric.
* **Click Feedback**: Ensure mouse click visual highlights are subtle or rely on our built-in Framer Motion button press animations.
* **Scrolling Speed**: Use smooth trackpad or inertia scrolling. Never yank the scrollbar rapidly.

---

## 3. The 3 "WOW MOMENTS" Choreography Checklist

Judges make their scoring decisions during three high-impact visual spikes. Execute these exact actions:

### Wow Moment #1: One-Click Autonomous PO Execution (AI War Room @ 0:22)
* **What to do**: On `/war-room`, point to the red **4d to Stockout** badge on **Industrial Sensor X200** (`$18,400 Revenue Exposure`).
* **The Wow Action**: Click the blue **[Approve PO]** button.
* **Why Judges Wow**: Demonstrates immediate transition from *passive alert* to *autonomous capital execution*.

### Wow Moment #2: Executive Copilot Decision Synthesis (Copilot @ 0:48)
* **What to do**: On `/copilot`, click the preset chip: `"What should I reorder today?"`.
* **The Wow Action**: Highlight the structured 3-part synthesis brief showing diagnostic root cause, quantified dollar impact, and pre-authorized EDI action plan.
* **Why Judges Wow**: Proves this is an **Executive AI Analyst**, not a wrapper around a generic chatbot.

### Wow Moment #3: Live Stochastic Slider Recalculation (Digital Twin @ 1:24)
* **What to do**: On `/simulation`, click **Supplier Failure** preset.
* **The Wow Action**: Drag the **Supplier SLA Delay** slider smoothly from `4 Days` to **20 Days** and watch the Recharts Area Chart and Revenue Delta scorecard recalculate in real time.
* **Why Judges Wow**: Proves enterprise-grade Monte Carlo stochastic modeling and forward what-if risk management.

---

## 4. Pre-Flight Verification Checklist (Do Right Before Clicking Record)

- [x] Backend Flask API running cleanly on port `5500` (`python run.py`)
- [x] Frontend Vite server running cleanly on port `5173` (`npm run dev` or production preview)
- [x] Initial URL set to `http://localhost:5173/`
- [x] Test `⌘K` Command Palette opens instantly
- [x] Microphone level checked (clear vocal tone, zero background fan hum)
