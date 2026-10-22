"""Billing logic for the Campus Canteen Pre-Order System."""
from decimal import Decimal, ROUND_HALF_UP

GST_RATE = Decimal("0.05")          # 5% GST
DISCOUNT_RATE = Decimal("0.10")     # 10% discount
DISCOUNT_THRESHOLD = Decimal("300") # discount applies strictly above Rs.300


def calculate_total(items):
    """Return the payable total in rupees (float, 2 decimals).

    items: iterable of (unit_price, quantity) tuples.
    Rules:
      1. subtotal = sum(price * quantity)
      2. if subtotal > 300 -> 10% discount on the subtotal
      3. 5% GST is charged on the discounted amount
    """
    subtotal = Decimal("0")
    for price, qty in items:
        price, qty = Decimal(str(price)), int(qty)
        if price < 0 or qty < 0:
            raise ValueError("price and quantity must not be negative")
        subtotal += price * qty

    if subtotal > DISCOUNT_THRESHOLD:
        subtotal -= subtotal * DISCOUNT_RATE

    total = subtotal * (1 + GST_RATE)
    return float(total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))
