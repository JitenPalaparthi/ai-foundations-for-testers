"""Shared pytest fixtures. No separate server command is needed for tests."""
from threading import Thread
import pytest
from server import make_server



def pytest_addoption(parser):
    parser.addoption("--run-public", action="store_true", default=False,
                     help="Include optional internet-dependent public-site tests")


def pytest_collection_modifyitems(config, items):
    if not config.getoption("--run-public"):
        skip = pytest.mark.skip(reason="Use --run-public to enable internet examples")
        for item in items:
            if "public" in item.keywords:
                item.add_marker(skip)


@pytest.fixture(scope="session")
def lab_url():
    server = make_server()
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    yield f"http://127.0.0.1:{server.server_port}"
    server.shutdown()
    server.server_close()
    thread.join(timeout=5) # join the thead is nothing but , make sure that the thread has completed its execution and jioines with main thread


@pytest.fixture
def lab(page, lab_url):
    page.goto(lab_url)
    return page


@pytest.fixture
def logged_in_page(lab):
    lab.get_by_label("Username", exact=True).fill("tester")
    lab.get_by_label("Password", exact=True).fill("secret123")
    lab.get_by_role("button", name="Sign in", exact=True).click()
    return lab
