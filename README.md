# Remote Expense Tracker Tagline: A lightweight, SSE-enabled expense management tool for AI agents.

Overview: The Remote Expense Tracker is a streamlined MCP tool built with FastMCP that allows users to manage their personal finances directly through their AI assistant. Designed for remote deployment, this tool operates as a web server using Server-Sent Events (SSE), making it easy to integrate into distributed workflows. It uses a lightweight SQLite database to store and retrieve transaction details instantly.

Key Features:

📝 Log Expenses: Quickly record new transactions with a category, amount, and custom description using the add_expense tool.

📊 View Reports: Retrieve a complete history of your spending with the list_expenses tool, which generates a formatted report of all recorded items.

🌐 Remote-Ready: Pre-configured to run as an SSE server (host 0.0.0.0), making it compatible with cloud hosting platforms like Render.

⚡ Lightweight Architecture: Built on FastMCP for minimal overhead and fast response times.
