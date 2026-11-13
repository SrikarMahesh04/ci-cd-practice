from app.security import hasher, verify
from app.passwords import password_strength


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
