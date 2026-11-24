from django.conf import settings
from django.db import models


class Side(models.TextChoices):
    BUY = "B", "Buy"
    SELL = "S", "Sell"
    # BUY, SELL
    ...


class OrderStatus(models.TextChoices):
    OPEN = "O", "Open"
    PARTIAL = "P", "Partial"
    FILLED = "F", "Filled"
    CANCELLED = "C", "Cancelled"
    # OPEN, PARTIAL, FILLED, CANCELLED
    ...


class Instrument(models.Model):
    symbol = models.CharField(max_length = 10, primary_key=True)
    shares_outstanding = models.PositiveIntegerField()
    # symbol              (unique ticker)
    # shares_outstanding  (fixed total; trades only move shares around)
    ...


class Account(models.Model):
    owner = models.OneToOneField()
    # owner          -> one-to-one with the user model
    # cash
    # reserved_cash  (cash locked up by open buy orders)
    ...


class Position(models.Model):
    # account        -> Account
    # instrument     -> Instrument
    # quantity
    # reserved_quantity  (shares locked up by open sell orders)
    # one row per (account, instrument)
    ...


class Order(models.Model):
    # account, instrument
    # side, status
    # price
    # quantity   (original size)
    # remaining  (unfilled size)
    # created_at (needed for price-time priority)
    ...


class Trade(models.Model):
    # instrument
    # buy_order, sell_order  (two FKs to Order, so each needs a related_name)
    # price, quantity
    # executed_at
    ...