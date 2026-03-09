"""Tests for src/cleaning/clean_sales_data.py"""

import pandas as pd
import pytest

from src.cleaning.clean_sales_data import SALES_COLUMNS, clean_sales_data, summary_report


def _make_df(rows: list[dict]) -> pd.DataFrame:
    defaults = {
        "Rank": 1,
        "Name": "Test Game",
        "Platform": "PS4",
        "Year": 2015.0,
        "Genre": "Action",
        "Publisher": "Pub",
        "NA_Sales": 1.0,
        "EU_Sales": 0.5,
        "JP_Sales": 0.2,
        "Other_Sales": 0.1,
        "Global_Sales": 1.8,
    }
    return pd.DataFrame([{**defaults, **r} for r in rows])


def test_clean_removes_exact_duplicates():
    row = {}
    df = _make_df([row, row])
    cleaned = clean_sales_data(df)
    assert len(cleaned) == 1


def test_clean_drops_missing_name():
    df = _make_df([{"Name": None}, {}])
    cleaned = clean_sales_data(df)
    assert len(cleaned) == 1
    assert cleaned["Name"].notna().all()


def test_clean_drops_missing_platform():
    df = _make_df([{"Platform": None}, {}])
    cleaned = clean_sales_data(df)
    assert len(cleaned) == 1


def test_clean_fills_missing_genre():
    df = _make_df([{"Genre": None}])
    cleaned = clean_sales_data(df)
    assert cleaned["Genre"].iloc[0] == "Unknown"


def test_clean_fills_missing_publisher():
    df = _make_df([{"Publisher": None}])
    cleaned = clean_sales_data(df)
    assert cleaned["Publisher"].iloc[0] == "Unknown"


def test_clean_coerces_year_string_to_nan():
    df = _make_df([{"Year": "N/A"}])
    cleaned = clean_sales_data(df)
    assert pd.isna(cleaned["Year"].iloc[0])


def test_clean_sales_non_negative():
    df = _make_df([{}])
    cleaned = clean_sales_data(df)
    for col in SALES_COLUMNS:
        assert (cleaned[col] >= 0).all(), f"{col} has negative values after cleaning"


def test_clean_fills_nan_sales_with_zero():
    df = _make_df([{"NA_Sales": None}])
    cleaned = clean_sales_data(df)
    assert cleaned["NA_Sales"].iloc[0] == 0.0


def test_clean_resets_index():
    df = _make_df([{}, {}])
    df = df.iloc[1:]  # index starts at 1
    cleaned = clean_sales_data(df)
    assert list(cleaned.index) == list(range(len(cleaned)))


def test_summary_report_keys():
    df = _make_df([{}])
    report = summary_report(df)
    expected_keys = {"rows", "columns", "missing_values", "duplicate_rows", "year_missing"}
    assert expected_keys == set(report.keys())


def test_clean_real_data_no_negative_sales():
    """Integration-style test against the real dataset."""
    from src.ingestion.load_dataset import load_raw_data
    df = load_raw_data()
    cleaned = clean_sales_data(df)
    for col in SALES_COLUMNS:
        assert (cleaned[col] >= 0).all()
