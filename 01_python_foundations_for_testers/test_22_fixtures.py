"""pytest fixtures and isolated test data

Time: 10 minutes
Goal: Share setup while keeping tests independent.

Explanation:
A fixture provides setup by matching its name to a test parameter. The default scope is function, so each test receives a new dictionary. Mutating the roles list in one test cannot affect another. Tests should never depend on execution order.

Expected result:
3 passed in any order.

Try it:
Add an email to the fixture and a test that checks its domain.
"""

import pytest

@pytest.fixture
def user():
    return {"username": "alice", "roles": ["reader"]}


def test_default_role(user):
    assert user["roles"] == ["reader"]


def test_add_role(user):
    user["roles"].append("editor")
    assert "editor" in user["roles"]


def test_user_starts_fresh(user):
    assert "editor" not in user["roles"]
