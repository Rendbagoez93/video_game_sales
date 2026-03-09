from pathlib import Path

import pandas as pd

RAW_DATA_PATH = (
    Path(__file__).resolve().parents[2] / "data" / "raw" / "video_games_sales.csv"
)

EXPECTED_COLUMNS = [
    "Rank",
    "Name",
    "Platform",
    "Year",
    "Genre",
    "Publisher",
    "NA_Sales",
    "EU_Sales",
    "JP_Sales",
    "Other_Sales",
    "Global_Sales",
]


def load_raw_data(path: Path = RAW_DATA_PATH) -> pd.DataFrame:
    """Load the raw video game sales CSV into a DataFrame.

    Args:
        path: Path to the CSV file. Defaults to the project raw data directory.

    Returns:
        DataFrame with the raw dataset.

    Raises:
        FileNotFoundError: If the CSV file does not exist at the given path.
        ValueError: If required columns are missing from the file.
    """
    if not path.exists():
        raise FileNotFoundError(f"Dataset not found at: {path}")

    df = pd.read_csv(path)

    missing = set(EXPECTED_COLUMNS) - set(df.columns)
    if missing:
        raise ValueError(f"Missing expected columns: {missing}")

    return df
