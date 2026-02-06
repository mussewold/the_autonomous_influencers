#!/usr/bin/env python3
"""Verify MCP tools (filesystem, git, postgres) are exposed to the MCP client.

This script uses the MCP SDK to call `list_tools` and checks for required tools.
"""
import os
import sys
try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass

try:
    # Placeholder import for MCP SDK client - adapt to your project's SDK
    from mcp import Client as MCPClient
except Exception:
    print("mcp SDK not installed or import path different. Install or adjust import.")
    sys.exit(2)


def main():
    # Attempt to connect via stdio (default/local). Adjust per your MCP runtime.
    try:
        client = MCPClient(transport='stdio')
    except TypeError:
        # Fallback if SDK expects no args
        client = MCPClient()

    try:
        tools = client.list_tools()
    except Exception as e:
        print(f"Failed to list tools: {e}")
        sys.exit(2)

    required = ['filesystem', 'git', 'postgres']
    found = {r: False for r in required}

    for t in tools:
        name = t.get('name') if isinstance(t, dict) else str(t)
        lname = name.lower() if name else ''
        for r in required:
            if r in lname:
                found[r] = True

    all_ok = True
    for r, ok in found.items():
        print(f"{r}: {'FOUND' if ok else 'MISSING'}")
        if not ok:
            all_ok = False

    sys.exit(0 if all_ok else 3)


if __name__ == '__main__':
    main()
