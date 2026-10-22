from fastmcp import FastMCP

mcp = FastMCP("Demo")

suppliers = {
    "SUP001": {"name": "Ibeco", "location": "Sweden", "currency": "SEK"},
    "SUP002": {"name": "Bevent", "location": "Norway", "currency": "NOK"},
}


@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


@mcp.tool
def greet(name: str) -> str:
    """Greet a person by name."""
    return f"Hello, {name}!"


@mcp.tool
def get_supplier(supplier_id: str) -> dict:
    """Get supplier information by ID."""
    return suppliers.get(supplier_id, {"error": "Supplier not found."})


"""
Sen, när detta fungerar, kan vi byta ut dictionaryn mot exempelvis ett API-anrop utan att ändra själva idén med tool:et:
@mcp.tool
def get_supplier(supplier_id: str):
    # istället för suppliers.get(...)
    # hämtar vi från extern datakälla
"""


if __name__ == "__main__":
    mcp.run(transport="http", port=8000)

"""Why do we need the if __name__ == "__main__": block?
The __main__ block is recommended for consistency and compatibility, ensuring your server works with
all MCP clients that execute your server file as a script.
Users who will exclusively run their server with the FastMCP CLI can omit it, as the CLI imports the
server object directly."""
