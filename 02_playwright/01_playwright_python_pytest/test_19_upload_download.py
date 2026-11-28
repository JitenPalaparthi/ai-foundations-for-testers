"""Upload and download

Achieve: Provide a local file and verify downloaded content.
Time: 6 minutes
Command: python -m pytest test_19_upload_download.py --browser chromium --browser firefox -v --headed --slowmo 350

Explanation:
set_input_files sets a file input directly without automating the OS picker. expect_download captures the event; save_as persists the temporary download. tmp_path isolates file artifacts. This practice upload displays a filename; it does not send bytes to a backend.

Expected: Filename appears and the downloaded CSV contains TC02,FAIL.

Try it: Clear the selected file and assert No file.
"""

from playwright.sync_api import expect
def test_upload_download(lab, tmp_path):
    evidence = tmp_path / "evidence.txt"
    evidence.write_text("Screenshot notes", encoding="utf-8")
    lab.get_by_label("Upload evidence", exact=True).set_input_files(evidence)
    expect(lab.locator("#upload-result")).to_have_text("evidence.txt")
    with lab.expect_download() as download_info:
        lab.get_by_role("link", name="Download report", exact=True).click()
    download = download_info.value
    assert download.suggested_filename == "report.csv"
    destination = tmp_path / download.suggested_filename
    download.save_as(destination)
    assert "TC02,FAIL" in destination.read_text(encoding="utf-8")
