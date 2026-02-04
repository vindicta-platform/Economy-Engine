"""Unit tests for Economy-Engine models."""

import pytest
from economy_engine.models import (
    Currency, CurrencyType, Transaction, TransactionType, Balance, Achievement, AchievementType
)


class TestCurrency:
    def test_currency_creation(self):
        currency = Currency(type=CurrencyType.VINDICTA_CREDITS, name="Vindicta Credits")
        assert currency.symbol == "VC"


class TestTransaction:
    def test_transaction_creation(self):
        tx = Transaction(
            user_id="user123",
            transaction_type=TransactionType.EARN,
            amount=100,
            reason="Game completed"
        )
        assert tx.amount == 100


class TestBalance:
    def test_balance_creation(self):
        balance = Balance(user_id="user123", amount=500)
        assert balance.amount == 500


class TestAchievement:
    def test_achievement_creation(self):
        achievement = Achievement(
            id="first_win",
            name="First Victory",
            description="Win your first game",
            achievement_type=AchievementType.WINS,
            threshold=1
        )
        assert achievement.threshold == 1
