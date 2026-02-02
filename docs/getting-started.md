# Getting Started

## Installation

```bash
uv pip install git+https://github.com/vindicta-platform/Economy-Engine.git
```

## Basic Usage

```python
from economy_engine import GasTank, Ledger

# Check balance
tank = GasTank()
print(tank.balance)

# Record usage
tank.consume(credits=10, operation="api_call")

# View history
ledger = Ledger()
for entry in ledger.recent(10):
    print(entry)
```
