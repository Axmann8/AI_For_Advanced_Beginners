"""
Smoke test: launch server.py over stdio, list its tools, and call a couple.

    python smoke_test.py

If you see the dice roll and fortune printed, your MCP server works. 🎉
"""

import asyncio
import sys
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

SERVER = Path(__file__).parent / "server.py"


async def main() -> None:
    params = StdioServerParameters(command=sys.executable, args=[str(SERVER)])
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await session.list_tools()
            print("Tools:", ", ".join(t.name for t in tools.tools))

            for name, args in [("roll_dice", {"notation": "3d6+2"}), ("random_fortune", {})]:
                result = await session.call_tool(name, args)
                print(f"{name} ->", result.content[0].text)


if __name__ == "__main__":
    asyncio.run(main())
