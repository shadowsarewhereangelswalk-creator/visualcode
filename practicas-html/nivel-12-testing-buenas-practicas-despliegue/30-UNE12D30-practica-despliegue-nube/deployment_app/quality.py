REQUIRED_CHECKS = ("tests", "lint", "format", "coverage", "container", "health")


def evaluate_checks(checks):
    normalized = {name: bool(checks.get(name, False)) for name in REQUIRED_CHECKS}
    failed = [name for name, passed in normalized.items() if not passed]
    return {
        "checks": normalized,
        "passed": len(REQUIRED_CHECKS) - len(failed),
        "total": len(REQUIRED_CHECKS),
        "failed": failed,
        "ready": not failed,
    }
