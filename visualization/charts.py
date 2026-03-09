"""Chart functions for the video game sales analysis.

Each function accepts a pre-computed DataFrame (produced by src/analysis/market_analysis.py)
and returns a Plotly Figure so callers can either display or export the chart.
"""

from __future__ import annotations

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# ---------------------------------------------------------------------------
# Colour palette shared across charts
# ---------------------------------------------------------------------------
_PALETTE = px.colors.qualitative.Bold


# ---------------------------------------------------------------------------
# Core insight charts
# ---------------------------------------------------------------------------


def plot_top_games(top_games_df: pd.DataFrame, n: int = 10) -> go.Figure:
    """Bar chart of the top n best-selling games globally.
    """
    
    df = top_games_df.head(n).sort_values("Global_Sales")
    fig = px.bar(
        df,
        x="Global_Sales",
        y="Name",
        orientation="h",
        color="Platform",
        color_discrete_sequence=_PALETTE,
        title=f"Top {n} Best-Selling Video Games Globally (millions of units)",
        labels={"Global_Sales": "Global Sales (M)", "Name": "Game"},
        text="Global_Sales",
    )
    fig.update_traces(texttemplate="%{text:.1f}M", textposition="outside")
    fig.update_layout(
        yaxis={"categoryorder": "total ascending"},
        legend_title="Platform",
        margin={"l": 200},
    )
    return fig


def plot_top_platforms(top_platforms_df: pd.DataFrame, n: int = 10) -> go.Figure:
    """Horizontal bar chart of platforms by cumulative global sales.
    """
    
    df = top_platforms_df.head(n).sort_values("Global_Sales")
    fig = px.bar(
        df,
        x="Global_Sales",
        y="Platform",
        orientation="h",
        color="Platform",
        color_discrete_sequence=_PALETTE,
        title=f"Top {n} Platforms by Global Sales (millions of units)",
        labels={"Global_Sales": "Total Sales (M)", "Platform": "Platform"},
        text="Global_Sales",
    )
    fig.update_traces(texttemplate="%{text:.1f}M", textposition="outside")
    fig.update_layout(
        yaxis={"categoryorder": "total ascending"},
        showlegend=False,
    )
    return fig


def plot_top_genres(top_genres_df: pd.DataFrame, n: int = 10) -> go.Figure:
    """Pie chart of genre share in global sales.

    Args:
        top_genres_df: Output of market_analysis.top_genres().
        n: Number of genres to display (remaining grouped as 'Other').
    """
    df = top_genres_df.head(n).copy()
    remainder = top_genres_df.iloc[n:]["Global_Sales"].sum()
    if remainder > 0:
        extra = pd.DataFrame([{"Genre": "Other", "Global_Sales": remainder}])
        df = pd.concat([df, extra], ignore_index=True)

    fig = px.pie(
        df,
        names="Genre",
        values="Global_Sales",
        title="Global Sales by Genre",
        color_discrete_sequence=_PALETTE,
        hole=0.35,
    )
    fig.update_traces(textposition="inside", textinfo="percent+label")
    return fig


def plot_top_publishers(top_publishers_df: pd.DataFrame, n: int = 10) -> go.Figure:
    """Bar chart of the top n publishers by total global sales.
    """
    
    df = top_publishers_df.head(n).sort_values("Global_Sales")
    fig = px.bar(
        df,
        x="Global_Sales",
        y="Publisher",
        orientation="h",
        color="Publisher",
        color_discrete_sequence=_PALETTE,
        title=f"Top {n} Publishers by Global Sales (millions of units)",
        labels={"Global_Sales": "Total Sales (M)", "Publisher": "Publisher"},
        text="Global_Sales",
    )
    fig.update_traces(texttemplate="%{text:.1f}M", textposition="outside")
    fig.update_layout(
        yaxis={"categoryorder": "total ascending"},
        showlegend=False,
    )
    return fig


def plot_sales_over_time(sales_over_time_df: pd.DataFrame) -> go.Figure:
    """Line chart of annual global video game sales.
    """
    
    fig = px.line(
        sales_over_time_df,
        x="Year",
        y="Global_Sales",
        markers=True,
        title="Annual Global Video Game Sales (1980–present)",
        labels={"Global_Sales": "Total Sales (M)", "Year": "Year"},
        color_discrete_sequence=[_PALETTE[0]],
    )
    fig.update_layout(hovermode="x unified")
    return fig


def plot_regional_share(regional_totals: pd.Series) -> go.Figure:
    """Donut chart of regional sales contribution.

    Args:
        regional_totals: Output of market_analysis.regional_totals().
    """
    fig = px.pie(
        names=regional_totals.index,
        values=regional_totals.values,
        title="Regional Contribution to Global Sales",
        color_discrete_sequence=_PALETTE,
        hole=0.4,
    )
    fig.update_traces(textposition="inside", textinfo="percent+label")
    return fig


# ---------------------------------------------------------------------------
# Supporting insight charts
# ---------------------------------------------------------------------------


def plot_genre_heatmap(genre_region_df: pd.DataFrame) -> go.Figure:
    """Heatmap of genre sales across regions.

    Args:
        genre_region_df: Output of market_analysis.genre_sales_by_region().
    """
    region_cols = ["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]
    region_labels = ["North America", "Europe", "Japan", "Other"]

    z = genre_region_df[region_cols].values
    fig = go.Figure(
        data=go.Heatmap(
            z=z,
            x=region_labels,
            y=genre_region_df["Genre"].tolist(),
            colorscale="Blues",
            hovertemplate="Genre: %{y}<br>Region: %{x}<br>Sales: %{z:.1f}M<extra></extra>",
        )
    )
    fig.update_layout(
        title="Genre Sales Heatmap by Region (millions of units)",
        xaxis_title="Region",
        yaxis_title="Genre",
    )
    return fig


def plot_blockbuster_scatter(df: pd.DataFrame) -> go.Figure:
    """Scatter plot of NA vs EU sales, highlighting blockbuster titles.

    Args:
        df: Feature-engineered DataFrame containing 'NA_Sales', 'EU_Sales',
            'Is_Blockbuster', 'Name', and 'Genre' columns.
    """
    plot_df = df[df["Global_Sales"] > 0].copy()
    plot_df["Label"] = plot_df["Is_Blockbuster"].map({True: "Blockbuster", False: "Regular"})

    fig = px.scatter(
        plot_df,
        x="NA_Sales",
        y="EU_Sales",
        color="Label",
        color_discrete_map={"Blockbuster": _PALETTE[1], "Regular": "#cccccc"},
        hover_name="Name",
        hover_data={"Genre": True, "Global_Sales": ":.2f"},
        opacity=0.7,
        title="NA vs EU Sales — Blockbuster Games Highlighted",
        labels={"NA_Sales": "NA Sales (M)", "EU_Sales": "EU Sales (M)"},
    )
    fig.update_traces(marker_size=6)
    return fig
