from strands import tool

# One tool only
@tool
def greet(name: str) -> str:
    """Greet a user by name."""
    return f"Hello, {name}!"
