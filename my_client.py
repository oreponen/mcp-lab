import asyncio

from fastmcp import Client

client = Client("http://localhost:8000/mcp")


async def call_tool(supplier_id: str):
    async with client:
        result = await client.call_tool("get_supplier", {"supplier_id": supplier_id})
        print(result)


asyncio.run(call_tool("SUP001"))
