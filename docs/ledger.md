# Ledger

## Overview

Double-entry transaction log for all economic activity.

## Entry Format

```python
class LedgerEntry:
    timestamp: datetime
    operation: str
    debit: int
    credit: int
    balance: int
```

## Querying

```python
ledger = Ledger()
entries = ledger.query(
    start=datetime.now() - timedelta(days=7),
    operation="api_call"
)
```
