from seasons import get_delta_days

def test_normal():
    assert get_delta_days("2023-03-21") == 366
