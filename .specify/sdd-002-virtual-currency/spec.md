# Economy-Engine v0.1.0: Virtual Currency Specification

> **Version**: 0.1.0-draft  
> **Status**: Draft  
> **Last Updated**: 2026-02-05  
> **Feature Branch**: `sdd/002-virtual-currency-v0.1.0`

---

## 1. Overview

Implement the foundational virtual currency system for the Vindicta Platform, enabling users to earn and spend **Vindicta Credits** through platform engagement.

### 1.1 Problem Statement

The Vindicta Platform lacks a gamification layer to drive user engagement and retention. Without a reward mechanism, users have no incentive to return after initial use.

### 1.2 Solution

A credit-based economy where users:
- **Earn** credits by completing games, achieving milestones, and daily login
- **Spend** credits on cosmetics, premium features, or tournament entries
- **Track** their balance with full transaction transparency

---

## 2. User Stories

### US-001: Earning Credits
> **As a** player  
> **I want to** earn Vindicta Credits when I complete a game  
> **So that** I feel rewarded for platform engagement

**Acceptance Criteria:**
- [ ] User receives credits upon game completion
- [ ] Credit amount scales with game duration/complexity
- [ ] Transaction is logged with reason and timestamp
- [ ] User sees notification of credits earned

### US-002: Viewing Balance
> **As a** player  
> **I want to** see my current credit balance  
> **So that** I know how much I can spend

**Acceptance Criteria:**
- [ ] Balance displays current credit amount
- [ ] Balance updates in real-time after transactions
- [ ] Balance cannot go negative (Constitution: no debt)

### US-003: Spending Credits
> **As a** player  
> **I want to** spend credits on platform rewards  
> **So that** my credits have tangible value

**Acceptance Criteria:**
- [ ] User can initiate spend transactions
- [ ] Transaction fails if insufficient balance (no debt)
- [ ] Successful spend deducts from balance atomically
- [ ] Transaction logged with item/reason

### US-004: Transaction History
> **As a** player  
> **I want to** view my transaction history  
> **So that** I can track my earning and spending

**Acceptance Criteria:**
- [ ] User can view paginated transaction list
- [ ] Each transaction shows: type, amount, reason, timestamp
- [ ] Transactions are immutable (append-only ledger)

---

## 3. Acceptance Scenarios

### Scenario 1: Successful Credit Earning
```gherkin
Given a user "player_123" with 100 credits
When they complete a standard game
Then their balance should be 110 credits
And a transaction of type "EARN" for 10 credits should exist
And the transaction reason should include "game_completion"
```

### Scenario 2: Spend with Sufficient Balance
```gherkin
Given a user "player_123" with 100 credits
When they purchase an item costing 50 credits
Then their balance should be 50 credits
And a transaction of type "SPEND" for 50 credits should exist
```

### Scenario 3: Spend with Insufficient Balance (No Debt)
```gherkin
Given a user "player_123" with 30 credits
When they attempt to purchase an item costing 50 credits
Then the transaction should fail with "InsufficientBalance" error
And their balance should remain 30 credits
And no transaction should be created
```

### Scenario 4: Atomic Transaction Guarantee
```gherkin
Given two concurrent spend requests for the same user
When both attempt to spend the full balance
Then only one transaction should succeed
And the other should fail with "InsufficientBalance"
And the ledger should remain balanced
```

---

## 4. Non-Functional Requirements

| Requirement | Target | Rationale |
|------------|--------|----------|
| **Transaction Speed** | <100ms | UX responsiveness |
| **Ledger Accuracy** | 100% balanced | Financial integrity |
| **Concurrency** | Thread-safe | Multi-request handling |
| **Auditability** | Full history | Dispute resolution |

---

## 5. Out of Scope (v0.1.0)

- Premium/paid currency (deferred to v0.2.0+)
- Achievements and badges (v0.2.0)
- Leaderboards (v0.2.0)
- Reward store UI (v1.0.0)
- Anti-fraud measures (v1.0.0)

---

## 6. Constitutional Constraints

Per `.specify/memory/constitution.md`:

1. **No Debt Accrual**: Balance cannot go negative
2. **Atomic Transactions**: All credit operations must be atomic
3. **Free Tier Compliance**: No standing monthly costs

---

## 7. Clarification Log

### Cycle 1: Ambiguity Search
| Term | Clarification |
|------|---------------|
| "game completion" | Any recorded match via WARScribe transcripts |
| "standard game" | Base earning rate (vs. ranked/tournament) |
| "real-time updates" | Within 1 second of transaction commit |
| "atomically" | Using database transactions with rollback |

### Cycle 2: Component Impact
| Component | Impact |
|-----------|--------|
| `models.py` | Extend with `Ledger`, `EarningRule` models |
| NEW: `ledger.py` | Core transaction processing service |
| NEW: `balance.py` | Balance query and caching service |
| `Vindicta-API` | Expose `/economy/` endpoints |
| `Vindicta-Portal` | Display balance widget |

### Cycle 3: Edge Cases & Failure Modes
| Scenario | Handling |
|----------|----------|
| Negative amount input | Validation error at model level |
| Concurrent double-spend | Database-level locking |
| Service crash mid-transaction | Rollback (uncommitted) |
| Invalid user_id | 404 error, no transaction |
| Earning overflow (max int) | Cap at MAX_BALANCE constant |

---

*Specification authored by Spec-Bot | SDD Workflow v2.0*
