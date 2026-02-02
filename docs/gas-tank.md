# Gas Tank

## Overview

The Gas Tank tracks credit balance with hard limits.

## Rules

1. **No Debt** — Operations fail when balance is 0
2. **Daily Refill** — Credits reset daily
3. **Soft Warnings** — Alerts at 20% remaining

## API

```python
class GasTank:
    balance: int
    
    def consume(self, credits: int, operation: str) -> bool
    def refill(self, credits: int) -> None
    def check_available(self, credits: int) -> bool
```
