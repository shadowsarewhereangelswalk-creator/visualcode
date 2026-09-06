import pytest

from deployment_app.quality import REQUIRED_CHECKS, evaluate_checks


def test_all_checks_pass():
    result = evaluate_checks(dict.fromkeys(REQUIRED_CHECKS, True))
    assert result["ready"] is True
    assert result["passed"] == 6
    assert result["failed"] == []


@pytest.mark.parametrize("missing", REQUIRED_CHECKS)
def test_each_required_check(missing):
    checks = dict.fromkeys(REQUIRED_CHECKS, True)
    checks[missing] = False
    result = evaluate_checks(checks)
    assert result["ready"] is False
    assert result["failed"] == [missing]
