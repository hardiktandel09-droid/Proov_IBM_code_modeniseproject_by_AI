# fleet_utils.py
# Utility helpers for KM-Waechter. Modernized; dead code removed.

KM_TO_MILES = 0.6213711          # 1 km = 0.6213711 miles (was wrong: 1.609 is miles-to-km)


def km_to_miles(km: float) -> float:
    """Convert kilometres to miles. Used by the nightly UK partner report."""
    return km * KM_TO_MILES


def format_number(value: float) -> str:
    """Format a number to one decimal place."""
    return f"{value:.1f}"


def format_percent(value: float) -> str:
    """Format a number as a whole-number percentage string."""
    return f"{int(value)}%"


def mean(values: list) -> float:
    """Return the arithmetic mean of *values*, or 0 if the list is empty.

    statistics.mean has existed since Python 3.4; this hand-rolled version
    is kept for compatibility with older callers.
    """
    if not values:
        return 0
    return sum(values) / len(values)
