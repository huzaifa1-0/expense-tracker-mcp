import os
import sqlite3
from typing import List
from pydantic import BaseModel
from fastmcp import FastMCP

# 1. Initialize FastMCP
# We do NOT set dependencies here for remote deployment; we handle that in requirements.txt
mcp = FastMCP("Remote Expense Tracker")

# --- Database Setup (SQLite) ---
# NOTE: On Render Free Tier, this file will reset if the server restarts. 
# For a real app, you would connect to a hosted PostgreSQL database here.
DB_FILE = "expenses.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS expenses 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  category TEXT, 
                  amount REAL, 
                  description TEXT)''')
    conn.commit()
    conn.close()

# Initialize DB on startup
init_db()

# --- Tools ---

@mcp.tool()
def add_expense(category: str, amount: float, description: str) -> str:
    """
    Add a new expense to the tracker.
    Args:
        category: The category of expense (e.g., Food, Travel, Tech)
        amount: The cost of the item.
        description: A brief description of what was bought.
    """
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("INSERT INTO expenses (category, amount, description) VALUES (?, ?, ?)", 
              (category, amount, description))
    conn.commit()
    conn.close()
    return f"Expense added: {description} (${amount}) in {category}"

@mcp.tool()
def list_expenses() -> str:
    """
    List all recorded expenses.
    """
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT * FROM expenses")
    rows = c.fetchall()
    conn.close()
    
    if not rows:
        return "No expenses recorded yet."
    
    report = "Expense Report:\n"
    for r in rows:
        report += f"{r[0]}. {r[1]} - ${r[2]}: {r[3]}\n"
    return report

# --- Server Entry Point ---
if __name__ == "__main__":
    # This is the CRITICAL part for remote deployment.
    # 1. transport="sse": Tells FastMCP to run as a Web Server, not a local stdio script.
    # 2. host="0.0.0.0": Required by Render to listen on all network interfaces.
    # 3. port: We read the PORT env var provided by Render, defaulting to 8000.
    port = int(os.environ.get("PORT", 8000))
    print(f"Starting SSE Server on port {port}...")
    mcp.run(transport="sse", host="0.0.0.0", port=port)