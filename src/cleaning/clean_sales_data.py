import pandas as pd


SALES_COLUMNS = ["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]


def clean_sales_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean the raw video game sales DataFrame.

    Steps performed:
    1. Drop exact duplicate rows.
    2. Drop rows where Name or Platform is missing (not useful without these).
    3. Coerce Year to numeric; invalid values become NaN.
    4. Fill missing Genre and Publisher with "Unknown".
    5. Coerce all sales columns to float and fill NaN with 0.0.

    Args:
        df: Raw DataFrame from load_raw_data().

    Returns:
        Cleaned DataFrame with reset index.
    """
    df = df.copy()

    # 1. Remove exact duplicates
    df = df.drop_duplicates()

    # 2. Rows without a game name or platform are not useful
    df = df.dropna(subset=["Name", "Platform"])
    df = df[df["Name"].str.strip().str.len() > 0]  # type: ignore[assignment]
    df = df[df["Platform"].str.strip().str.len() > 0]  # type: ignore[assignment]

    # 3. Year: coerce to numeric (some entries are "N/A" strings)
    df["Year"] = pd.to_numeric(df["Year"], errors="coerce")

    # 4. Fill missing categorical fields
    df["Genre"] = df["Genre"].fillna("Unknown").str.strip()
    df["Publisher"] = df["Publisher"].fillna("Unknown").str.strip()

    # 5. Sales columns: coerce to float and fill NaN with 0
    for col in SALES_COLUMNS:
        df[col] = pd.to_numeric(df[col], errors="coerce", downcast="float").fillna(0.0)

    return df.reset_index(drop=True)


def summary_report(df: pd.DataFrame) -> dict:
    """Return a dict summarising data quality metrics of a DataFrame."""
    return {
        "rows": len(df),
        "columns": len(df.columns),
        "missing_values": int(df.isnull().sum().sum()),
        "duplicate_rows": int(df.duplicated().sum()),
        "year_missing": int(df["Year"].isnull().sum()),
    }
