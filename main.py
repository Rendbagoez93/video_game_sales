"""main.py — Full video game sales analysis pipeline.

Run this script to execute the entire pipeline end-to-end:
  1. Data ingestion
  2. Data validation
  3. Data cleaning
  4. Feature engineering
  5. Market analysis (printed summary)
  6. Visualization — individual charts + combined dashboard

Usage:
    python main.py              # run full pipeline
    python main.py --no-charts  # skip visualization export
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Ensure the project root is on sys.path when launched directly
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Local imports must come after sys.path is patched  # noqa: E402
from src.analysis.market_analysis import (  # noqa: E402
    peak_sales_year,
    regional_totals,
    sales_over_time,
    top_games_global,
    top_genres,
    top_platforms,
    top_publishers,
)
from src.cleaning.clean_sales_data import (  # noqa: E402
    clean_sales_data,
    summary_report,
)
from src.features.feature_engineering import engineer_features  # noqa: E402
from src.ingestion.load_dataset import load_raw_data  # noqa: E402
from src.validation.schema import validate_raw  # noqa: E402
from visualization.dashboard import build_dashboard, save_all_charts  # noqa: E402

# ---------------------------------------------------------------------------
# Pipeline steps
# ---------------------------------------------------------------------------


def run_ingestion():
    print("[1/6] Loading raw dataset …")
    df = load_raw_data()
    print(f"      Loaded {len(df):,} rows × {len(df.columns)} columns.")
    return df


def run_validation(df):
    print("[2/6] Validating schema …")
    validate_raw(df)
    print("      Schema validation passed.")
    return df


def run_cleaning(df):
    print("[3/6] Cleaning data …")
    df_clean = clean_sales_data(df)
    report = summary_report(df_clean)
    print(
        f"      After cleaning: {report['rows']:,} rows | "
        f"{report['missing_values']} missing values | "
        f"{report['duplicate_rows']} duplicate rows | "
        f"{report['year_missing']} missing years."
    )
    return df_clean


def run_feature_engineering(df):
    print("[4/6] Engineering features …")
    df_feat = engineer_features(df)
    new_cols = [c for c in df_feat.columns if c not in df.columns]
    print(f"      Added columns: {new_cols}")
    return df_feat


def run_analysis(df):
    print("[5/6] Running market analysis …")

    games = top_games_global(df, n=5)
    print("\n  Top 5 best-selling games globally:")
    for _, row in games.iterrows():
        print(f"    {row['Name']:40s}  {row['Global_Sales']:.2f}M  [{row['Platform']}]")

    platforms = top_platforms(df, n=5)
    print("\n  Top 5 platforms by total sales:")
    for _, row in platforms.iterrows():
        print(f"    {row['Platform']:10s}  {row['Global_Sales']:.2f}M")

    genres = top_genres(df, n=5)
    print("\n  Top 5 genres by total sales:")
    for _, row in genres.iterrows():
        print(f"    {row['Genre']:15s}  {row['Global_Sales']:.2f}M")

    publishers = top_publishers(df, n=3)
    print("\n  Top 3 publishers by total sales:")
    for _, row in publishers.iterrows():
        print(f"    {row['Publisher']:30s}  {row['Global_Sales']:.2f}M")

    peak_year = peak_sales_year(df)
    annual = sales_over_time(df)
    peak_sales = float(annual["Global_Sales"].max())
    print(
        f"\n  Peak sales year: {int(peak_year)} "
        f"({peak_sales:.2f}M units sold globally)"
    )

    reg = regional_totals(df)
    print("\n  Regional share of global sales:")
    total = reg.sum()
    for region, val in reg.items():
        print(f"    {region:15s}  {val:.2f}M  ({val / total * 100:.1f}%)")

    print()
    return df


def run_visualization(df, output_dir: Path):
    print("[6/6] Building visualizations …")
    charts = save_all_charts(df, output_dir)
    print(f"      Saved {len(charts)} individual charts to {output_dir}/")
    dashboard_path = build_dashboard(df, output_dir)
    print(f"      Dashboard saved → {dashboard_path}")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Video Game Sales — full analysis pipeline"
    )
    parser.add_argument(
        "--no-charts",
        action="store_true",
        help="Skip chart and dashboard export.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=PROJECT_ROOT / "reports" / "figures",
        help="Directory to save HTML charts (default: reports/figures/).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    print("=" * 60)
    print("  Video Game Sales — Analysis Pipeline")
    print("=" * 60)

    df = run_ingestion()
    df = run_validation(df)
    df = run_cleaning(df)
    df = run_feature_engineering(df)
    run_analysis(df)

    if not args.no_charts:
        run_visualization(df, args.output_dir)
    else:
        print("[6/6] Skipping visualization (--no-charts flag set).")

    print("=" * 60)
    print("  Pipeline complete.")
    print("=" * 60)


if __name__ == "__main__":
    main()
