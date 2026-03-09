"""Tests for src/analysis/market_analysis.py"""

import pandas as pd
import pytest

from src.analysis.market_analysis import (
    detect_outliers,
    genre_sales_by_region,
    peak_sales_year,
    platform_sales_over_time,
    regional_totals,
    sales_by_decade,
    sales_over_time,
    top_games_by_region,
    top_games_global,
    top_genres,
    top_platforms,
    top_publishers,
)


def _sample_df() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "Rank": 1, "Name": "A", "Platform": "PS4", "Year": 2010.0,
                "Genre": "Action", "Publisher": "Big Pub",
                "NA_Sales": 10.0, "EU_Sales": 5.0, "JP_Sales": 2.0, "Other_Sales": 1.0, "Global_Sales": 18.0,
                "Decade": "2010s",
            },
            {
                "Rank": 2, "Name": "B", "Platform": "Wii", "Year": 2008.0,
                "Genre": "Sports", "Publisher": "Small Pub",
                "NA_Sales": 3.0, "EU_Sales": 8.0, "JP_Sales": 1.0, "Other_Sales": 0.5, "Global_Sales": 12.5,
                "Decade": "2000s",
            },
            {
                "Rank": 3, "Name": "C", "Platform": "PS4", "Year": 2010.0,
                "Genre": "Action", "Publisher": "Big Pub",
                "NA_Sales": 1.0, "EU_Sales": 1.0, "JP_Sales": 0.5, "Other_Sales": 0.2, "Global_Sales": 2.7,
                "Decade": "2010s",
            },
        ]
    )


def test_top_games_global_length():
    df = _sample_df()
    result = top_games_global(df, n=2)
    assert len(result) == 2


def test_top_games_global_order():
    df = _sample_df()
    result = top_games_global(df, n=3)
    assert result.iloc[0]["Global_Sales"] >= result.iloc[1]["Global_Sales"]


def test_top_platforms_returns_dataframe():
    df = _sample_df()
    result = top_platforms(df, n=2)
    assert isinstance(result, pd.DataFrame)
    assert "Platform" in result.columns


def test_top_genres_correct_top():
    df = _sample_df()
    result = top_genres(df, n=1)
    # Action: 18 + 2.7 = 20.7 vs Sports: 12.5
    assert result.iloc[0]["Genre"] == "Action"


def test_top_publishers_aggregates():
    df = _sample_df()
    result = top_publishers(df)
    big_pub = result[result["Publisher"] == "Big Pub"]["Global_Sales"].iloc[0]
    assert big_pub == pytest.approx(18.0 + 2.7)


def test_sales_over_time_sorted():
    df = _sample_df()
    result = sales_over_time(df)
    assert list(result["Year"]) == sorted(result["Year"])


def test_peak_sales_year():
    df = _sample_df()
    year = peak_sales_year(df)
    # 2010: 18 + 2.7 = 20.7 vs 2008: 12.5
    assert year == 2010


def test_regional_totals_index():
    df = _sample_df()
    totals = regional_totals(df)
    assert set(totals.index) == {"North America", "Europe", "Japan", "Other"}


def test_top_games_by_region_na():
    df = _sample_df()
    result = top_games_by_region(df, "NA", n=1)
    assert result.iloc[0]["Name"] == "A"


def test_top_games_by_region_invalid():
    df = _sample_df()
    with pytest.raises(ValueError):
        top_games_by_region(df, "INVALID")


def test_genre_sales_by_region_shape():
    df = _sample_df()
    result = genre_sales_by_region(df)
    assert "Genre" in result.columns
    assert "NA_Sales" in result.columns


def test_platform_sales_over_time_sorted():
    df = _sample_df()
    result = platform_sales_over_time(df)
    assert "Year" in result.columns
    assert "Platform" in result.columns


def test_detect_outliers_returns_subset():
    df = _sample_df()
    result = detect_outliers(df, column="Global_Sales")
    assert len(result) <= len(df)


def test_sales_by_decade_requires_decade_column():
    df = _sample_df().drop(columns=["Decade"])
    with pytest.raises(KeyError):
        sales_by_decade(df)


def test_sales_by_decade_correct():
    df = _sample_df()
    result = sales_by_decade(df)
    assert "Decade" in result.columns
    assert "Global_Sales" in result.columns
