# test_km_wachter.py
from km_wachter import needs_service, wear_percent, SERVICE_INTERVAL_KM, WARN_AT_PERCENT


def test_almost_due_car_is_flagged():
    # A car at 14,900 of its 15,000 km window is about 99% worn and MUST be flagged.
    assert needs_service({"id": "VOS-4471", "odometer": 14900, "last_service_km": 0}) is True


def test_missing_reading_is_not_treated_as_zero():
    # A car with NO last-service reading must not be treated as fully worn.
    assert needs_service({"id": "VOS-7788", "odometer": 92000}) is False


# ── Wear-math verification tests ──────────────────────────────────────────────

def test_wear_percent_uses_true_division():
    # 14,900 / 15,000 = 0.9933... → ~99.33%, NOT 0% (which floor division produced).
    pct = wear_percent(14900, SERVICE_INTERVAL_KM)
    assert 99.0 <= pct <= 100.0, f"Expected ~99.3% but got {pct:.2f}%"


def test_wear_percent_at_exact_interval_is_100():
    # Exactly one full interval = 100% worn.
    assert wear_percent(SERVICE_INTERVAL_KM, SERVICE_INTERVAL_KM) == 100.0


def test_wear_percent_at_zero_km_is_zero():
    # Freshly serviced car = 0% worn.
    assert wear_percent(0, SERVICE_INTERVAL_KM) == 0.0


def test_warn_threshold_is_80_percent():
    # The threshold constant must stay at 80 — do not change it.
    assert WARN_AT_PERCENT == 80


def test_service_interval_is_15000_km():
    # The service interval constant must stay at 15000 — do not change it.
    assert SERVICE_INTERVAL_KM == 15000


def test_car_exactly_at_80_percent_is_flagged():
    # A car exactly at 80% (12,000 km since service) must be flagged (≥ 80, not > 80).
    assert needs_service({"id": "VOS-TEST", "odometer": 12000, "last_service_km": 0}) is True


def test_car_just_below_80_percent_is_not_flagged():
    # A car just below 80% (11,999 km since service) must NOT be flagged.
    assert needs_service({"id": "VOS-TEST", "odometer": 11999, "last_service_km": 0}) is False
