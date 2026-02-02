from strands import tool

@tool
def greet(name: str) -> str:
    """Greet a user by name."""
    return f"Hello, {name}!"


@tool
def get_name() -> str:
    """Return a default name when the user didn't provide one."""
    return "Raphael"
