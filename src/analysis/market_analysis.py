"""Market analysis functions answering the core and supporting analytical questions."""

import pandas as pd


# ---------------------------------------------------------------------------
# Core insights
# ---------------------------------------------------------------------------


def top_games_global(df: pd.DataFrame, n: int = 10) -> pd.DataFrame:
    """Q1: Top n best-selling video games globally."""
    return (
        df.nlargest(n, "Global_Sales")[["Rank", "Name", "Platform", "Publisher", "Genre", "Global_Sales"]]
        .reset_index(drop=True)
    )


def top_platforms(df: pd.DataFrame, n: int = 10) -> pd.DataFrame:
    """Q2: Platforms with the highest cumulative global sales."""
    return (
        df.groupby("Platform", as_index=False)["Global_Sales"]
        .sum()
        .nlargest(n, "Global_Sales")
        .reset_index(drop=True)
    )


def top_genres(df: pd.DataFrame, n: int = 10) -> pd.DataFrame:
    """Q3: Genres that dominate global sales."""
    return (
        df.groupby("Genre", as_index=False)["Global_Sales"]
        .sum()
        .nlargest(n, "Global_Sales")
        .reset_index(drop=True)
    )


def top_publishers(df: pd.DataFrame, n: int = 10) -> pd.DataFrame:
    """Q4: Publishers with the most cumulative global revenue."""
    return (
        df.groupby("Publisher", as_index=False)["Global_Sales"]
        .sum()
        .nlargest(n, "Global_Sales")
        .reset_index(drop=True)
    )


def sales_over_time(df: pd.DataFrame) -> pd.DataFrame:
    """Q5 & Q6: Annual global sales totals, sorted by year."""
    return (
        df.dropna(subset=["Year"])
        .groupby("Year", as_index=False)["Global_Sales"]
        .sum()
        .sort_values("Year")
        .reset_index(drop=True)
    )


def peak_sales_year(df: pd.DataFrame) -> int:
    """Q6: The year with the highest total global sales."""
    annual = sales_over_time(df)
    return int(annual.loc[annual["Global_Sales"].idxmax(), "Year"])


def regional_totals(df: pd.DataFrame) -> pd.Series:
    """Q7: Total sales contribution per region."""
    cols = ["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]
    totals = df[cols].sum()
    totals.index = ["North America", "Europe", "Japan", "Other"]
    return totals


def top_games_by_region(df: pd.DataFrame, region: str, n: int = 10) -> pd.DataFrame:
    """Q8: Top n games in a specific region.

    Args:
        df: DataFrame with sales data.
        region: One of 'NA', 'EU', 'JP', 'Other'.
        n: Number of top games to return.
    """
    col_map = {"NA": "NA_Sales", "EU": "EU_Sales", "JP": "JP_Sales", "Other": "Other_Sales"}
    if region not in col_map:
        raise ValueError(f"region must be one of {list(col_map.keys())}")
    col = col_map[region]
    return (
        df.nlargest(n, col)[["Name", "Platform", "Publisher", "Genre", col]]
        .reset_index(drop=True)
    )


# ---------------------------------------------------------------------------
# Supporting insights
# ---------------------------------------------------------------------------


def genre_sales_by_region(df: pd.DataFrame) -> pd.DataFrame:
    """Regional genre preferences: total sales per genre per region."""
    region_cols = ["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]
    return df.groupby("Genre")[region_cols].sum().reset_index()


def platform_sales_over_time(df: pd.DataFrame) -> pd.DataFrame:
    """Sales per platform per year for trend analysis."""
    return (
        df.dropna(subset=["Year"])
        .groupby(["Year", "Platform"], as_index=False)["Global_Sales"]
        .sum()
        .sort_values(["Platform", "Year"])
        .reset_index(drop=True)
    )


def detect_outliers(df: pd.DataFrame, column: str = "Global_Sales") -> pd.DataFrame:
    """Return rows where column value lies beyond 3 standard deviations from the mean."""
    mean = df[column].mean()
    std = df[column].std()
    return df[df[column] > mean + 3 * std].reset_index(drop=True)


def genre_correlations(df: pd.DataFrame) -> pd.DataFrame:
    """Return the correlation matrix of regional and global sales columns."""
    cols = ["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]
    return df[cols].corr()


def sales_by_decade(df: pd.DataFrame) -> pd.DataFrame:
    """Total global sales grouped by decade."""
    if "Decade" not in df.columns:
        decade_num = (df["Year"] // 10 * 10).astype("Int64")
        df = df.copy()
        df["Decade"] = decade_num.astype(str).str.replace("<NA>", "Unknown") + "s"
    return (
        df[df["Decade"] != "Unknowns"]
        .groupby("Decade", as_index=False)["Global_Sales"]
        .sum()
        .sort_values("Decade")
        .reset_index(drop=True)
    )


def sales_by_decade(df: pd.DataFrame) -> pd.DataFrame:
    """Total global sales grouped by decade (requires 'Decade' feature column)."""
    if "Decade" not in df.columns:
        raise KeyError("'Decade' column not found. Run engineer_features() first.")
    return (
        df[df["Decade"] != "Unknown"]
        .groupby("Decade", as_index=False)["Global_Sales"]
        .sum()
        .sort_values("Decade")
        .reset_index(drop=True)
    )


def genre_correlations(df: pd.DataFrame) -> pd.DataFrame:
    """Correlation matrix between sales columns."""
    sales_cols = ["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]
    return df[sales_cols].corr()
