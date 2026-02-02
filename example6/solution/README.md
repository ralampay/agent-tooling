# Solution: Failure-First Risk Flow

This solution satisfies the exercise:
- Adds a validator tool and blocks downstream calls on failure.
- Escalates on missing files or parse errors.
- Logs tool usage for auditability.

## Run
```
python main.py
```

Example output:
```
Tool #1: validate_msisdn
Tool #2: get_account_profile
Tool #3: get_recent_events
Tool #4: escalate_to_human
Escalated to human support: recent events parse error
```
