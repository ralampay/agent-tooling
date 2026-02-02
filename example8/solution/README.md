# Solution: API Failure Handling + Report

This solution satisfies the exercise:
- Writes a failure report file on API failure.
- Escalates to a human with a clear reason.
- Avoids record updates when the API fails.

## Run
```
python main.py
```

Example output:
```
Tool #1: call_fraud_api
Tool #2: write_failure_report
Tool #3: escalate_to_human
Escalated to human support: timeout
```
