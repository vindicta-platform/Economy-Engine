"""
Core models for Economy-Engine.

Minimal scaffold for P3 product.
"""

from datetime import datetime
from decimal import Decimal
from enum import Enum, auto
from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class CurrencyType(str, Enum):
    """Types of virtual currency."""
    VINDICTA_CREDITS = "vindicta_credits"
    PREMIUM = "premium"  # Future: paid currency


class TransactionType(str, Enum):
    """Types of transactions."""
    EARN = "earn"
    SPEND = "spend"
    TRANSFER = "transfer"
    REFUND = "refund"


class Currency(BaseModel):
    """Virtual currency definition."""
    
    type: CurrencyType
    name: str
    symbol: str = "VC"
    decimals: int = 0  # Whole units only


class Transaction(BaseModel):
    """A currency transaction."""
    
    id: UUID = Field(default_factory=uuid4)
    user_id: str
    currency: CurrencyType = CurrencyType.VINDICTA_CREDITS
    
    transaction_type: TransactionType
    amount: int
    
    reason: str = ""
    metadata: dict = Field(default_factory=dict)
    
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class Balance(BaseModel):
    """A user's currency balance."""
    
    user_id: str
    currency: CurrencyType = CurrencyType.VINDICTA_CREDITS
    amount: int = 0
    
    last_updated: datetime = Field(default_factory=datetime.utcnow)


class AchievementType(str, Enum):
    """Types of achievements."""
    GAMES_PLAYED = "games_played"
    WINS = "wins"
    STREAK = "streak"
    COLLECTION = "collection"


class Achievement(BaseModel):
    """An unlockable achievement."""
    
    id: str
    name: str
    description: str
    
    achievement_type: AchievementType
    threshold: int  # Number needed to unlock
    
    reward_amount: int = 0
    badge_icon: Optional[str] = None
    
    # Progress tracking
    user_progress: int = 0
    unlocked: bool = False
    unlocked_at: Optional[datetime] = None
