"""Tests for src/validation/schema.py"""

import pandas as pd
import pandera.errors
import pytest

from src.validation.schema import validate_clean, validate_raw


def _make_raw_row(**overrides) -> dict:
    base = {
        "Rank": 1,
        "Name": "Test Game",
        "Platform": "PS4",
        "Year": 2015.0,
        "Genre": "Action",
        "Publisher": "Test Publisher",
        "NA_Sales": 1.0,
        "EU_Sales": 0.5,
        "JP_Sales": 0.2,
        "Other_Sales": 0.1,
        "Global_Sales": 1.8,
    }
    base.update(overrides)
    return base


def _single_row_df(**overrides) -> pd.DataFrame:
    return pd.DataFrame([_make_raw_row(**overrides)])


def test_validate_raw_passes_valid_row():
    df = _single_row_df()
    result = validate_raw(df)
    assert len(result) == 1


def test_validate_raw_fails_negative_sales():
    df = _single_row_df(NA_Sales=-1.0)
    with pytest.raises(pandera.errors.SchemaErrors):
        validate_raw(df)


def test_validate_raw_fails_invalid_year():
    df = _single_row_df(Year=1800.0)
    with pytest.raises(pandera.errors.SchemaErrors):
        validate_raw(df)


def test_validate_raw_allows_null_year():
    df = _single_row_df(Year=None)
    result = validate_raw(df)
    assert len(result) == 1


def test_validate_clean_passes_valid_row():
    df = _single_row_df()
    result = validate_clean(df)
    assert len(result) == 1


def test_validate_clean_fails_empty_genre():
    df = _single_row_df(Genre="")
    with pytest.raises(pandera.errors.SchemaErrors):
        validate_clean(df)
