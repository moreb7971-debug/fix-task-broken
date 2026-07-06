import json
from pathlib import Path

# Checks that the report.json file exists
def test_report_exists():
    assert Path("/app/report.json").exists(), "report.json not found"

# Checks that the report.json file is not empty and has the expected content
def test_report_nonempty():
    with open("/app/report.json") as f:
        report = json.load(f)

    assert report == {
        "total_requests": 6,
        "unique_ips": 3,
        "top_path": "/index.html",
    }