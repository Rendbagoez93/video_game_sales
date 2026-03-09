import numpy as np
import pandas as pd


def add_sales_ratios(df: pd.DataFrame) -> pd.DataFrame:
    """Add regional sales ratio columns (share of global sales per region)."""
    df = df.copy()
    global_safe = df["Global_Sales"].replace(0, np.nan)
    df["NA_Sales_Ratio"] = df["NA_Sales"] / global_safe
    df["EU_Sales_Ratio"] = df["EU_Sales"] / global_safe
    df["JP_Sales_Ratio"] = df["JP_Sales"] / global_safe
    df["Other_Sales_Ratio"] = df["Other_Sales"] / global_safe
    return df


def add_decade(df: pd.DataFrame) -> pd.DataFrame:
    """Derive a Decade column from Year (e.g. '1990s'). Unknown for missing Year."""
    df = df.copy()
    decade_num = (df["Year"] // 10 * 10).astype("Int64")
    df["Decade"] = decade_num.astype(str).str.replace("<NA>", "Unknown") + "s"
    df.loc[df["Year"].isna(), "Decade"] = "Unknown"
    return df


def add_blockbuster_flag(df: pd.DataFrame, quantile: float = 0.90) -> pd.DataFrame:
    """Flag games in the top `quantile` percentile of global sales as blockbusters."""
    df = df.copy()
    threshold = df["Global_Sales"].quantile(quantile)
    df["Is_Blockbuster"] = df["Global_Sales"] >= threshold
    return df


def add_dominant_region(df: pd.DataFrame) -> pd.DataFrame:
    """Add a column indicating which region contributes the most sales for each game."""
    df = df.copy()
    region_cols = ["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]
    region_labels = ["NA", "EU", "JP", "Other"]
    label_map = dict(zip(region_cols, region_labels))
    df["Dominant_Region"] = df[region_cols].idxmax(axis=1).map(label_map)
    return df


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """Apply all feature engineering steps in sequence.

    Args:
        df: Cleaned DataFrame from clean_sales_data().

    Returns:
        DataFrame enriched with derived feature columns.
    """
    df = add_sales_ratios(df)
    df = add_decade(df)
    df = add_blockbuster_flag(df)
    df = add_dominant_region(df)
    return df
