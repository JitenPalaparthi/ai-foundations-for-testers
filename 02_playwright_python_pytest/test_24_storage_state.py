"""Reuse storage state

Achieve: Save and load browser storage into an isolated context.
Time: 8 minutes
Command: python -m pytest test_24_storage_state.py --browser chromium --browser firefox -v --headed --slowmo 350

Explanation:
storage_state saves cookies and local storage. It does not include sessionStorage. This lab demonstrates persistence of a demo flag, not real server-side authentication. The plugin new_context fixture creates the restored context in whichever engine is selected and manages teardown and artifacts. The test also closes it explicitly once it is finished. Real authentication-state files can contain secrets and should not be committed.

Expected: A second context restores tester from saved local storage.

Try it: Create the second context without storage_state and expect No saved session.
"""

from playwright.sync_api import expect
def test_storage_state(lab, new_context, lab_url, tmp_path):
    lab.get_by_label("Username", exact=True).fill("tester")
    lab.get_by_label("Password", exact=True).fill("secret123")
    lab.get_by_role("button", name="Sign in", exact=True).click()
    expect(lab.get_by_role("status")).to_have_text("Welcome, tester!")
    state_file = tmp_path / "demo-state.json"
    lab.context.storage_state(path=str(state_file))
    # Uses the same browser engine as the current test case.
    context = new_context(storage_state=str(state_file))
    try:
        restored = context.new_page()
        restored.goto(lab_url)
        restored.get_by_role("button", name="Restore session", exact=True).click()
        expect(restored.locator("#session-message")).to_have_text("Session restored for tester")
    finally:
        context.close()
