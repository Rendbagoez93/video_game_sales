"""Visualization package for video game sales analysis.

Modules:
    charts    — individual chart functions (static & interactive)
    dashboard — combined HTML dashboard built from charts
"""

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
from visualization.dashboard import build_dashboard

__all__ = [
    "plot_top_games",
    "plot_top_platforms",
    "plot_top_genres",
    "plot_top_publishers",
    "plot_sales_over_time",
    "plot_regional_share",
    "plot_genre_heatmap",
    "plot_blockbuster_scatter",
    "build_dashboard",
]
