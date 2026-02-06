# Economy-Engine Constraints

> Critical rules agents MUST follow when modifying this repository.

## ⛔ Hard Constraints

1. **Atomic Transactions** - All debits/credits in transactions
2. **No Negative Balances** - Debit fails if insufficient
3. **Audit Trail Required** - All changes logged
4. **SQLAlchemy 2.0 Only** - Use new-style async patterns

## 💰 Economic Rules

### Credit Operations
```python
# All operations must be atomic
async with session.begin():
    tank.debit(amount)
    ledger.record(operation)
```

### Pricing Model
```python
COSTS = {
    "debate": 10,      # Meta-Oracle debate
    "grade": 5,        # List grading
    "parse": 2,        # Roster parsing
    "roll": 0,         # Free (no AI)
}
```

### Refill Rules
- Daily refill: 100 credits (free tier)
- No rollover: unused credits expire
- Bonus credits: never expire

## 🔒 Data Integrity

- All balances are `INTEGER` (no floats)
- Ledger is append-only
- Balance = sum(ledger entries)

## 🧪 Testing Requirements

Before merging:
- [ ] `pytest` passes
- [ ] Transaction isolation tests pass
- [ ] Concurrent access tests pass
- [ ] Ledger integrity verification passes
