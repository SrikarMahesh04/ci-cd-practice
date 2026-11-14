from datetime import time
from app.security import hasher, verify
from app.passwords import password_strength
from app.domain import distance_m, expected_shift_minutes


def test_password_hashing():
    raw_secret = "SecurePassword123!"
    hashed = hasher.hash(raw_secret)
    assert hashed != raw_secret
    assert verify(hashed, raw_secret) is True
    assert verify(hashed, "WrongPassword!") is False


def test_password_strength():
    assert password_strength("12345") == "Weak"
    assert password_strength("WeakPass1!") == "Medium"
    assert password_strength("VeryLongSecurePassword2026!#") == "Strong"


def test_expected_shift_minutes_deduction():
    # 9:00 AM to 6:00 PM = 9 hours (540 mins) minus 60 mins lunch deduction = 480 mins (8 hours)
    shift_start = time(9, 0)
    shift_end = time(18, 0)
    assert expected_shift_minutes(shift_start, shift_end) == 480


def test_distance_calculation_same_point():
    # Distance between identical coordinates is 0
    assert distance_m(17.3850, 78.4867, 17.3850, 78.4867) == 0.0
