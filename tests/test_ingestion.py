"""Tests for src/ingestion/load_dataset.py"""

from pathlib import Path

import pandas as pd
import pytest

from src.ingestion.load_dataset import EXPECTED_COLUMNS, load_raw_data


def test_load_raw_data_returns_dataframe():
    df = load_raw_data()
    assert isinstance(df, pd.DataFrame)


def test_load_raw_data_has_expected_columns():
    df = load_raw_data()
    for col in EXPECTED_COLUMNS:
        assert col in df.columns, f"Missing column: {col}"


def test_load_raw_data_not_empty():
    df = load_raw_data()
    assert len(df) > 0


def test_load_raw_data_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_raw_data(Path("/nonexistent/path/data.csv"))


def test_load_raw_data_missing_column(tmp_path):
    """Loading a CSV that is missing a required column should raise ValueError."""
    bad_csv = tmp_path / "bad.csv"
    bad_csv.write_text("Rank,Name,Platform\n1,TestGame,PC\n")
    with pytest.raises(ValueError, match="Missing expected columns"):
        load_raw_data(bad_csv)
