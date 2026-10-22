import pytest
from canteen import calculate_total


def test_empty_order_is_zero():
    assert calculate_total([]) == 0.0


def test_gst_only_below_threshold():
    # 100 + 5% GST
    assert calculate_total([(50, 2)]) == 105.00


def test_exactly_300_gets_no_discount():
    # 300 + 5% = 315 (discount is only *above* 300)
    assert calculate_total([(100, 3)]) == 315.00


def test_discount_above_300():
    # 400 -> 360 after 10% -> 378 after GST
    assert calculate_total([(200, 2)]) == 378.00


def test_just_above_threshold():
    # 301 -> 270.9 -> 284.445 -> 284.45
    assert calculate_total([(301, 1)]) == 284.45


def test_multiple_items():
    # 40*2 + 120*3 = 440 -> 396 -> 415.80
    assert calculate_total([(40, 2), (120, 3)]) == 415.80


def test_negative_values_rejected():
    with pytest.raises(ValueError):
        calculate_total([(-10, 1)])
