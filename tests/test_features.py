"""Tests for src/features/feature_engineering.py"""

import numpy as np
import pandas as pd
import pytest

from src.features.feature_engineering import (
    add_blockbuster_flag,
    add_decade,
    add_dominant_region,
    add_sales_ratios,
    engineer_features,
)


def _base_df() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "Rank": 1,
                "Name": "Game A",
                "Platform": "PS4",
                "Year": 2010.0,
                "Genre": "Action",
                "Publisher": "Pub",
                "NA_Sales": 4.0,
                "EU_Sales": 2.0,
                "JP_Sales": 1.0,
                "Other_Sales": 0.5,
                "Global_Sales": 7.5,
            },
            {
                "Rank": 2,
                "Name": "Game B",
                "Platform": "Wii",
                "Year": 1995.0,
                "Genre": "Sports",
                "Publisher": "Pub2",
                "NA_Sales": 1.0,
                "EU_Sales": 3.0,
                "JP_Sales": 0.5,
                "Other_Sales": 0.2,
                "Global_Sales": 4.7,
            },
        ]
    )


def test_sales_ratios_sum_to_one():
    df = add_sales_ratios(_base_df())
    ratio_cols = ["NA_Sales_Ratio", "EU_Sales_Ratio", "JP_Sales_Ratio", "Other_Sales_Ratio"]
    for _, row in df.iterrows():
        total = sum(row[c] for c in ratio_cols)
        assert abs(total - 1.0) < 1e-6, f"Ratios don't sum to 1: {total}"


def test_sales_ratios_handles_zero_global_sales():
    df = _base_df().copy()
    df.at[0, "Global_Sales"] = 0.0
    result = add_sales_ratios(df)
    # Ratios for a zero-global-sales row should be NaN, not inf
    assert result.at[0, "NA_Sales_Ratio"] != np.inf
    assert pd.isna(result.at[0, "NA_Sales_Ratio"])


def test_add_decade_correct_values():
    df = add_decade(_base_df())
    assert df.at[0, "Decade"] == "2010s"
    assert df.at[1, "Decade"] == "1990s"


def test_add_decade_unknown_for_null_year():
    df = _base_df().copy()
    df.at[0, "Year"] = None
    result = add_decade(df)
    assert result.at[0, "Decade"] == "Unknown"


def test_blockbuster_flag_dtype():
    df = add_blockbuster_flag(_base_df())
    assert df["Is_Blockbuster"].dtype == bool


def test_blockbuster_top_game_flagged():
    df = add_blockbuster_flag(_base_df(), quantile=0.5)
    # At least one row should be flagged
    assert df["Is_Blockbuster"].any()


def test_dominant_region_column_exists():
    df = add_dominant_region(_base_df())
    assert "Dominant_Region" in df.columns


def test_dominant_region_correct():
    df = add_dominant_region(_base_df())
    # Game A: NA_Sales=4 is highest → "NA"
    assert df.at[0, "Dominant_Region"] == "NA"
    # Game B: EU_Sales=3 is highest → "EU"
    assert df.at[1, "Dominant_Region"] == "EU"


def test_engineer_features_adds_all_columns():
    df = engineer_features(_base_df())
    expected = [
        "NA_Sales_Ratio", "EU_Sales_Ratio", "JP_Sales_Ratio", "Other_Sales_Ratio",
        "Decade", "Is_Blockbuster", "Dominant_Region",
    ]
    for col in expected:
        assert col in df.columns, f"Missing column after engineer_features: {col}"


def test_engineer_features_does_not_mutate_input():
    original = _base_df()
    original_cols = list(original.columns)
    engineer_features(original)
    assert list(original.columns) == original_cols
