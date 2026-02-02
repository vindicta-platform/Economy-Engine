# Economy Engine

**Free-tier sustainability through smart resource management.**

Economy Engine implements the Gas Tank model — a credit-based system that ensures platform operations never exceed budget.

## The Economic Prime Directive

> No standing monthly costs. The platform MUST run on free tier.

## Components

| Component | Purpose |
|-----------|---------|
| **Gas Tank** | Credit balance tracking |
| **Ledger** | Double-entry transaction log |
| **Meter** | Usage metering |

## Installation

```bash
uv pip install git+https://github.com/vindicta-platform/Economy-Engine.git
```

## Quick Start

```python
from economy_engine import GasTank

tank = GasTank()
tank.consume(10, "dice_roll")
print(f"Balance: {tank.balance}")
```

---

[Full Platform](https://vindicta-platform.github.io/mkdocs/)
