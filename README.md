# Video Game Sales Analysis

An exploratory data analysis and data pipeline project using historical video game sales data. Built as a Kaggle-style portfolio piece demonstrating practical data engineering and analytical skills.

## Overview

This project analyzes the global video game market to uncover patterns that explain commercial success. It covers top-performing games, platforms, genres, and publishers, as well as regional differences and historical sales trends.

**Key questions answered:**
- What are the top-selling games, platforms, genres, and publishers globally?
- How do regional markets (NA, EU, JP) differ in preferences?
- How have video game sales evolved over time?
- What drives success in the global video game market?

## Project Structure

```
video_game_sales/
├── data/
│   ├── raw/                  # Source dataset (video_games_sales.csv)
│   └── processed/            # Cleaned output (gitignored)
├── notebooks/
│   ├── 01_data_overview.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda.ipynb
│   └── 04_analysis.ipynb
├── src/
│   ├── ingestion/            # Data loading
│   ├── validation/           # Pandera schema checks
│   ├── cleaning/             # Data cleaning functions
│   ├── features/             # Feature engineering
│   └── analysis/             # Market analysis
├── visualization/            # Chart and dashboard builders
├── tests/                    # Pytest test suite
├── reports/
│   ├── figures/              # Generated HTML charts (gitignored)
│   └── insights/
├── main.py
└── pyproject.toml
```

## Tech Stack

| Area | Tools |
|---|---|
| Language | Python 3.14+ |
| Dependency management | uv + pyproject.toml |
| Data processing | Pandas, NumPy, PyArrow |
| Visualization | Matplotlib, Seaborn, Plotly |
| Data validation | Pandera |
| Testing | pytest, pytest-cov |
| Notebooks | JupyterLab, ipykernel |
| Code quality | Ruff, Black, Pyright |

## Getting Started

**Prerequisites:** Python 3.14+, [uv](https://docs.astral.sh/uv/)

```bash
# Clone the repository
git clone <repo-url>
cd video_game_sales

# Install dependencies
uv sync

# Run the full pipeline
uv run python main.py
```

To launch notebooks:

```bash
uv run jupyter lab
```

To run tests:

```bash
uv run pytest --cov=src tests/
```

## Dataset

Historical video game sales sourced from Kaggle. Fields: `Rank`, `Name`, `Platform`, `Year`, `Genre`, `Publisher`, `NA_Sales`, `EU_Sales`, `JP_Sales`, `Other_Sales`, `Global_Sales`.

## Pipeline Stages

1. **Ingestion** — Load raw CSV and perform initial checks
2. **Validation** — Schema and data quality checks via Pandera
3. **Cleaning** — Handle missing values, fix types, remove duplicates
4. **Feature Engineering** — Sales ratios, regional share, decade bucketing
5. **EDA** — Statistical summaries and visualizations
6. **Analysis** — Market insights and storytelling
