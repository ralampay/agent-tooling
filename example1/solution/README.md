# Solution: Two-Step Greeting

This solution follows the exercise requirements:
- Uses tools as contracts (`get_name`, `greet`).
- Agent decides which tool(s) to call.
- Tool calls are logged for auditability.
- If no name is provided, the agent calls `get_name` first, then `greet`.

## Run
```
python main.py
```

Example output:
```
Tool #1: get_name
Tool #2: greet
Hello, Raphael!
```
