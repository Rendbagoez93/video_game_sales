"""Dashboard builder for the video game sales analysis.

Combines all charts into a single self-contained HTML file using Plotly's
subplot layout and HTML export utilities.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go

from src.analysis.market_analysis import (
    top_games_global,
    top_platforms,
    top_genres,
    top_publishers,
    sales_over_time,
    regional_totals,
    genre_sales_by_region,
)
from visualization.charts import (
    plot_top_games,
    plot_top_platforms,
    plot_top_genres,
    plot_top_publishers,
    plot_sales_over_time,
    plot_regional_share,
    plot_genre_heatmap,
    plot_blockbuster_scatter,
)

_FIGURES_DIR = Path(__file__).resolve().parents[1] / "reports" / "figures"


# ---------------------------------------------------------------------------
# Individual chart exports
# ---------------------------------------------------------------------------


def save_chart(fig: go.Figure, filename: str, output_dir: Path = _FIGURES_DIR) -> Path:
    """Save a Plotly figure as a self-contained HTML file.

    Args:
        fig: Plotly Figure object.
        filename: Target filename (without extension).
        output_dir: Directory to write the file into.

    Returns:
        Absolute Path to the saved HTML file.
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    out_path = output_dir / f"{filename}.html"
    fig.write_html(str(out_path), include_plotlyjs="cdn")
    return out_path


# ---------------------------------------------------------------------------
# Main dashboard
# ---------------------------------------------------------------------------


def build_dashboard(df: pd.DataFrame, output_dir: Path = _FIGURES_DIR) -> Path:
    """Build and save a single HTML dashboard combining all key charts.

    The dashboard contains:
      - Top 10 best-selling games (horizontal bar)
      - Top 10 platforms by sales (horizontal bar)
      - Genre share (pie / donut)
      - Regional contribution (donut)
      - Annual sales trend (line)
      - Genre × Region heatmap
      - Blockbuster scatter (NA vs EU)
      - Top 10 publishers (horizontal bar)

    Args:
        df: Feature-engineered DataFrame (output of engineer_features()).
        output_dir: Directory to write the dashboard HTML file.

    Returns:
        Absolute Path to the saved dashboard HTML file.
    """
    # --- Compute analysis DataFrames ---
    games_df = top_games_global(df)
    platforms_df = top_platforms(df)
    genres_df = top_genres(df)
    publishers_df = top_publishers(df)
    annual_df = sales_over_time(df)
    reg_totals = regional_totals(df)
    genre_region_df = genre_sales_by_region(df)

    # --- Build individual figures ---
    fig_games = plot_top_games(games_df)
    fig_platforms = plot_top_platforms(platforms_df)
    fig_genres = plot_top_genres(genres_df)
    fig_publishers = plot_top_publishers(publishers_df)
    fig_time = plot_sales_over_time(annual_df)
    fig_region = plot_regional_share(reg_totals)
    fig_heatmap = plot_genre_heatmap(genre_region_df)
    fig_scatter = plot_blockbuster_scatter(df)

    # --- Compose into a single dashboard figure using subplots ---
    dashboard = make_subplots(
        rows=4,
        cols=2,
        subplot_titles=(
            "Top 10 Best-Selling Games",
            "Top 10 Platforms by Sales",
            "Genre Share",
            "Regional Contribution",
            "Annual Sales Trend",
            "Genre × Region Heatmap",
            "NA vs EU Sales (Blockbusters)",
            "Top 10 Publishers by Sales",
        ),
        specs=[
            [{"type": "bar"}, {"type": "bar"}],
            [{"type": "pie"}, {"type": "pie"}],
            [{"type": "scatter"}, {"type": "heatmap"}],
            [{"type": "scatter"}, {"type": "bar"}],
        ],
        vertical_spacing=0.10,
        horizontal_spacing=0.08,
    )

    # Row 1 — bar charts
    for trace in fig_games.data:
        dashboard.add_trace(trace, row=1, col=1)
    for trace in fig_platforms.data:
        dashboard.add_trace(trace, row=1, col=2)

    # Row 2 — pie charts
    for trace in fig_genres.data:
        dashboard.add_trace(trace, row=2, col=1)
    for trace in fig_region.data:
        dashboard.add_trace(trace, row=2, col=2)

    # Row 3 — line + heatmap
    for trace in fig_time.data:
        dashboard.add_trace(trace, row=3, col=1)
    for trace in fig_heatmap.data:
        dashboard.add_trace(trace, row=3, col=2)

    # Row 4 — scatter + publishers bar
    for trace in fig_scatter.data:
        dashboard.add_trace(trace, row=4, col=1)
    for trace in fig_publishers.data:
        dashboard.add_trace(trace, row=4, col=2)

    dashboard.update_layout(
        title_text="Video Game Sales — Global Market Dashboard",
        title_font_size=22,
        height=2000,
        showlegend=False,
        template="plotly_white",
    )

    # --- Save ---
    output_dir.mkdir(parents=True, exist_ok=True)
    out_path = output_dir / "00_dashboard.html"
    dashboard.write_html(str(out_path), include_plotlyjs="cdn")
    return out_path


def save_all_charts(df: pd.DataFrame, output_dir: Path = _FIGURES_DIR) -> list[Path]:
    """Export every chart as a separate HTML file.

    Args:
        df: Feature-engineered DataFrame.
        output_dir: Directory to write the HTML files.

    Returns:
        List of Paths to saved HTML files.
    """
    charts_map = {
        "01_top_games": plot_top_games(top_games_global(df)),
        "02_top_platforms": plot_top_platforms(top_platforms(df)),
        "03_top_genres": plot_top_genres(top_genres(df)),
        "04_top_publishers": plot_top_publishers(top_publishers(df)),
        "05_sales_over_time": plot_sales_over_time(sales_over_time(df)),
        "06_regional_share": plot_regional_share(regional_totals(df)),
        "07_genre_heatmap": plot_genre_heatmap(genre_sales_by_region(df)),
        "08_blockbuster_scatter": plot_blockbuster_scatter(df),
    }
    saved: list[Path] = []
    for name, fig in charts_map.items():
        saved.append(save_chart(fig, name, output_dir))
    return saved
