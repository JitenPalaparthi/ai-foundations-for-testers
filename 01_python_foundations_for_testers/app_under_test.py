"""Small application functions exercised by the pytest examples."""
import json
import os


def is_acceptable(status_code, response_ms, limit_ms=800):
    """Apply the sample status and latency acceptance rule."""
    return status_code == 200 and response_ms <= limit_ms


def parse_duration(raw):
    """Convert numeric input and reject negative durations."""
    try:
        duration = float(raw)
    except (ValueError, TypeError) as error:
        raise ValueError("Duration must be numeric") from error
    if duration < 0:
        raise ValueError("Duration cannot be negative")
    return duration


def save_result(path, result):
    """Write a serializable result to a caller-provided path."""
    path.write_text(json.dumps(result), encoding="utf-8")


def service_url():
    """Read configuration without contacting the service."""
    return os.environ.get("TEST_SERVICE_URL", "https://example.test")


def summarize_report(report, limit_ms=800):
    """Summarize a valid report without changing the caller's table.

    Assumes known PASS/FAIL statuses and numeric, nonmissing response times.
    Each row represents one execution; this function does not deduplicate.
    """
    total = len(report)
    passed = int(report["status"].eq("PASS").sum())
    return {
        "total": total,
        "failed": int(report["status"].eq("FAIL").sum()),
        "pass_rate_pct": passed / total * 100 if total else 0.0,
        "slow_cases": report.loc[report["response_ms"].gt(limit_ms), "case_id"].tolist(),
    }
