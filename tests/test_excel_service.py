from pathlib import Path

import pytest
from openpyxl import Workbook

from eventops.services.excel import ExcelError, summarize_excel


def test_summarize_excel_ok(tmp_path: Path):
    xlsx = tmp_path / "sample.xlsx"
    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"
    ws.append(["A", "B", "C"])
    ws.append([1, 2, 3])
    ws.append([4, 5, 6])
    wb.save(xlsx)

    summary = summarize_excel(xlsx, preview_rows=2)

    assert summary.sheet_used == "Sheet1"
    assert summary.rows >= 3
    assert summary.cols == 3
    assert summary.columns[:3] == ["A", "B", "C"]
    assert len(summary.preview) == 3  # cabecera + 2 filas


def test_summarize_excel_missing_file(tmp_path: Path):
    with pytest.raises(ExcelError):
        summarize_excel(tmp_path / "missing.xlsx")


def test_summarize_excel_wrong_extension(tmp_path: Path):
    fake = tmp_path / "bad.csv"
    fake.write_text("x,y\n1,2\n", encoding="utf-8")
    with pytest.raises(ExcelError):
        summarize_excel(fake)
