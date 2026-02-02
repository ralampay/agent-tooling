# Solution: Help Desk with Missing-ID Tool

This solution satisfies the exercise:
- Uses explicit tools, including a new `get_account_id` tool.
- Agent decides and chains tools when needed.
- Tool calls are logged for auditability.

## Run
```
python main.py
```

Example output:
```
Tool #1: classify_issue
Tool #2: get_account_id
Tool #3: lookup_invoice
We found your invoice. Status: Duplicate charge flagged.
```
