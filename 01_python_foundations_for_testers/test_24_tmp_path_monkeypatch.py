"""pytest files and dependency replacement

Time: 10 minutes
Goal: Test file output and configuration without shared state.

Explanation:
tmp_path supplies a distinct temporary directory for each test. The file test verifies the observable saved content. monkeypatch changes environment variables for a test and restores them afterward. delenv with raising=False removes an optional setting safely. These tests exercise configuration, not network connectivity.

Expected result:
3 passed; no network requests are made.

Try it:
Save a result with passed=False and check its content. Explain why modifying a real shared result file would cause interference.
"""

import json
from app_under_test import save_result, service_url


def test_save_result(tmp_path):
    destination = tmp_path / "result.json"
    save_result(destination, {"case": "login", "passed": True})
    assert json.loads(destination.read_text(encoding="utf-8")) == {
        "case": "login", "passed": True,
    }


def test_configured_url(monkeypatch):
    monkeypatch.setenv("TEST_SERVICE_URL", "https://staging.example.test")
    assert service_url() == "https://staging.example.test"


def test_default_url(monkeypatch):
    monkeypatch.delenv("TEST_SERVICE_URL", raising=False)
    assert service_url() == "https://example.test"
