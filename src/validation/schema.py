import pandas as pd
import pandera.pandas as pa
from pandera.pandas import Check, Column, DataFrameSchema

# Pandera schema for the raw video game sales dataset.
# Year and Genre/Publisher are nullable because the raw data contains N/A values.
RAW_SCHEMA = DataFrameSchema(
    {
        "Rank": Column(int, Check.ge(1), nullable=False),
        "Name": Column(str, Check(lambda s: s.str.strip().str.len().gt(0).all()), nullable=False),
        "Platform": Column(str, Check(lambda s: s.str.strip().str.len().gt(0).all()), nullable=False),
        "Year": Column(float, Check(lambda s: s.dropna().between(1970, 2030).all()), nullable=True),
        "Genre": Column(str, nullable=True),
        "Publisher": Column(str, nullable=True),
        "NA_Sales": Column(float, Check.ge(0), nullable=False),
        "EU_Sales": Column(float, Check.ge(0), nullable=False),
        "JP_Sales": Column(float, Check.ge(0), nullable=False),
        "Other_Sales": Column(float, Check.ge(0), nullable=False),
        "Global_Sales": Column(float, Check.ge(0), nullable=False),
    },
    coerce=True,
)

# Schema for cleaned data — Year and Genre/Publisher filled; Year is int-like float.
CLEAN_SCHEMA = DataFrameSchema(
    {
        "Rank": Column(int, Check.ge(1), nullable=False),
        "Name": Column(str, nullable=False),
        "Platform": Column(str, nullable=False),
        "Year": Column(float, Check(lambda s: s.dropna().between(1970, 2030).all()), nullable=True),
        "Genre": Column(str, Check(lambda s: s.str.len().gt(0).all()), nullable=False),
        "Publisher": Column(str, Check(lambda s: s.str.len().gt(0).all()), nullable=False),
        "NA_Sales": Column(float, Check.ge(0), nullable=False),
        "EU_Sales": Column(float, Check.ge(0), nullable=False),
        "JP_Sales": Column(float, Check.ge(0), nullable=False),
        "Other_Sales": Column(float, Check.ge(0), nullable=False),
        "Global_Sales": Column(float, Check.ge(0), nullable=False),
    },
    coerce=True,
)


def validate_raw(df: pd.DataFrame) -> pd.DataFrame:
    """Validate raw DataFrame against RAW_SCHEMA.

    Args:
        df: Raw DataFrame loaded from CSV.

    Returns:
        Validated DataFrame (pandera passes it through unchanged).

    Raises:
        pandera.errors.SchemaErrors: If validation fails (lazy=True collects all errors).
    """
    return RAW_SCHEMA.validate(df, lazy=True)


def validate_clean(df: pd.DataFrame) -> pd.DataFrame:
    """Validate cleaned DataFrame against CLEAN_SCHEMA."""
    return CLEAN_SCHEMA.validate(df, lazy=True)
