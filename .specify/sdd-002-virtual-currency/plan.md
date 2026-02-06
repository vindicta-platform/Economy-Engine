# Economy-Engine v0.1.0: Implementation Plan

> **Spec Reference**: [spec.md](./spec.md)  
> **Feature Branch**: `sdd/002-virtual-currency-v0.1.0`

---

## User Review Required

> [!IMPORTANT]
> This plan adds a new SQLite-based ledger storage. Confirm this aligns with the "no standing monthly costs" constitution requirement (SQLite is serverless/free).

---

## Proposed Changes

### Core Models

#### [MODIFY] models.py

Add new models:

```python
class EarningRule(BaseModel):
    """Defines credit earning rates for actions."""
    action: str  # e.g., "game_completion", "daily_login"
    base_amount: int
    multiplier: float = 1.0

class LedgerEntry(BaseModel):
    """Double-entry ledger record."""
    id: UUID
    transaction_id: UUID
    account: str  # "user:{id}" or "system:reserve"
    debit: int = 0
    credit: int = 0
    timestamp: datetime

MAX_BALANCE: int = 1_000_000_000  # 1 billion cap
```

---

### Ledger Service

#### [NEW] ledger.py

Core transaction processing with atomic guarantees:

```python
class LedgerService:
    def __init__(self, db_path: str = ":memory:"):
        """Initialize SQLite-backed ledger."""
    
    async def earn(self, user_id: str, amount: int, reason: str) -> Transaction:
        """Credit user account atomically."""
    
    async def spend(self, user_id: str, amount: int, reason: str) -> Transaction:
        """Debit user account if sufficient balance."""
    
    async def get_balance(self, user_id: str) -> int:
        """Calculate current balance from ledger."""
    
    async def get_transactions(self, user_id: str, limit: int = 50) -> list[Transaction]:
        """Retrieve paginated transaction history."""

class InsufficientBalanceError(Exception):
    """Raised when spend exceeds available balance."""
```

---

### Balance Service

#### [NEW] balance.py

Caching layer for balance queries:

```python
class BalanceService:
    def __init__(self, ledger: LedgerService, cache_ttl: int = 60):
        """Balance queries with optional caching."""
    
    async def get_balance(self, user_id: str) -> Balance:
        """Get cached or computed balance."""
    
    async def invalidate(self, user_id: str) -> None:
        """Clear cache after transaction."""
```

---

### Package Exports

#### [MODIFY] __init__.py

Export new services:

```python
from economy_engine.ledger import LedgerService, InsufficientBalanceError
from economy_engine.balance import BalanceService
```

---

## Verification Plan

### Automated Tests

Run with:
```bash
cd Economy-Engine
uv run pytest tests/ -v
```

| Test File | Coverage |
|-----------|----------|
| `tests/test_models.py` | Existing model validation |
| `tests/test_ledger.py` | [NEW] Earn/spend atomic operations |
| `tests/test_balance.py` | [NEW] Balance calculation and caching |
| `tests/test_concurrency.py` | [NEW] Double-spend prevention |

### Key Test Cases

1. **test_earn_credits**: Verify balance increases after earn
2. **test_spend_sufficient**: Verify balance decreases after valid spend
3. **test_spend_insufficient**: Verify `InsufficientBalanceError` raised
4. **test_no_negative_balance**: Verify balance never goes below 0
5. **test_concurrent_spend**: Verify only one of two concurrent spends succeeds
6. **test_transaction_history**: Verify immutable append-only log

---

*Plan authored by Spec-Bot | SDD Workflow v2.0*
