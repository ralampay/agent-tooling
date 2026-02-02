# Solution: Human-in-the-Loop Review + Audit

This solution satisfies the exercise:
- Always builds a review packet and writes an audit log.
- Creates and routes tickets for high/unknown risk.
- Logs tool usage for auditability.

## Run
```
python main.py
```

Example output:
```
Tool #1: get_account_profile
Tool #2: get_recent_events
Tool #3: score_risk
Tool #4: build_review_summary
Tool #5: append_audit_log
Tool #6: create_review_ticket
Tool #7: route_to_queue
Review ticket created: R-1001
```
