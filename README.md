# Remote Expense Tracker

**Tagline:** A lightweight, SSE-enabled expense management tool for AI agents.

## Overview
The Remote Expense Tracker is a streamlined MCP tool designed for distributed AI workflows. It is deployed as a cloud service, allowing you to track expenses, generate reports, and manage finances directly through your AI assistant without running a local database.

**Deployment Status:** ✅ Live on Render

## Key Features
* **📝 Log Expenses:** Record transactions with category, amount, and description (`add_expense`).
* **📊 View Reports:** Generate formatted spending reports instantly (`list_expenses`).
* **☁️ Cloud-Hosted:** Persistent availability via secure SSE connection.

---

## 🚀 How to Connect (For Users)

Since this tool is hosted remotely, you need a small local "bridge" script to connect it to Claude Desktop.

### Prerequisites
* Python 3.10 or higher installed.
* [Claude Desktop](https://claude.ai/download) installed.

### Step 1: Get the Connection Script
Save the code below as `client_remote.py` on your computer (or clone this repo):

```python
from fastmcp.server import create_proxy

# The URL of the deployed Expense Tracker
RENDER_SSE_URL = "https://<YOUR-APP-NAME>[.onrender.com/sse](https://.onrender.com/sse)" 

# Initialize the proxy
mcp = create_proxy(RENDER_SSE_URL, name="Remote Expense Tracker")

if __name__ == "__main__":
    mcp.run()
