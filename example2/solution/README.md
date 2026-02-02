# Solution: Order Status with Fallback ID

This solution satisfies the exercise:
- Uses explicit tools (`get_default_order_id`, `get_order_status`).
- Agent decides and chains tools when needed.
- Tool calls are logged for auditability.

## Run
```
python main.py
```

Example output:
```
Tool #1: get_default_order_id
Tool #2: get_order_status
Shipped
```
