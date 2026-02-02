# Solution: Risk Scoring with New Signal

This solution satisfies the exercise:
- Adds a new tool `get_network_risk`.
- Updates scoring to incorporate the new signal.
- Logs tool usage for auditability.
 - Reads signals from files in `data/`.

## Run
```
python main.py
```

Example output:
```
Tool #1: get_account_profile
Tool #2: get_recent_events
Tool #3: get_network_risk
Tool #4: score_risk
Escalated to human support: High risk (score 90) for SIM swap.
```
