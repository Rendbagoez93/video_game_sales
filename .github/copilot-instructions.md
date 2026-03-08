## Video Game Sales Dataset — Analysis Plan

This project aims to analyze the global video game market using historical sales data. The goal is to uncover patterns that explain commercial success in the gaming industry.

### Primary objectives:
- Identify which games, platforms, genres, and publishers dominate global sales
- Understand regional market differences between North America, Europe, Japan, and other regions
- Analyze historical trends in video game releases and sales over time
- Detect market outliers, such as blockbuster titles or region-specific successes
- Produce clear data visualizations and insights suitable for a Kaggle portfolio project

### The analysis demonstrates practical skills in:
- Data Ingestion
- Data Validation
- Data Cleaning
- Feature Engineering
- Exploratory Data Analysis (EDA)
- Analytical Storytelling

### Dataset:
The dataset contains historical sales data for video games, including attributes such as:
Rank, Name, Platform, Year, Genre, Publisher, NA_Sales, EU_Sales, JP_Sales, Other_Sales, Global_Sales

### Methodology:
1. **Data Ingestion**: Load the dataset into a suitable data analysis environment (e.g., Python with pandas).
2. **Data Validation**: Check for missing values, data types, and consistency in the dataset.
3. **Data Cleaning**: Handle missing values, correct data types, and remove duplicates if necessary.
4. **Feature Engineering**: Create new features such as total sales, sales ratios, or categorize genres and platforms.
5. **Exploratory Data Analysis (EDA)**: Use statistical summaries and visualizations to explore relationships between variables and identify trends.
6. **Analytical Storytelling**: Summarize findings in a clear and compelling way, using visualizations to support insights and conclusions.

### Expected Outcomes:
At the completion of this project, the following outcomes are expected:

#### Analytical Outcomes

- Identification of the top-performing games, genres, platforms, and publishers in the global video game market.
- Clear understanding of regional differences in gaming preferences between North America, Europe, Japan, and other regions.
- Discovery of historical market trends, including the rise and decline of platforms and genres.
- Identification of blockbuster games and outliers that significantly outperform market averages.

#### Data Engineering Outcomes
- A reproducible data pipeline including ingestion, validation, cleaning, feature engineering, and analysis.
- Implementation of schema validation and data quality checks.
- A lightweight automated testing suite ensuring pipeline reliability.

#### Portfolio Outcomes
- A well-structured GitHub repository demonstrating clean project organization.
- A clear Kaggle-style analytical narrative supported by data visualizations.
- Reusable Python modules for data processing and analysis.
- High-quality visualizations explaining market insights.

#### Learning Outcomes
This project demonstrates practical capabilities in:
- Exploratory Data Analysis (EDA)
- Data Pipeline Design
- Data Validation and Testing
- Feature Engineering
- Analytical Storytelling
- Working with modern Python data tools

These outcomes position the project as a strong portfolio piece for data analyst or data engineer roles. 

### Tech Stack:
- Languages: Python 3.14+
- Dependency Management: uv with pyproject.toml
- Data Processing: Pandas, NumPy, Pyarrow
- Data Visualization: Matplotlib, Seaborn, Plotly
- Testing: pytest, pytest-cov
- Data Validation: pandera
- Notebook / Exploration: JupyterLab, IPYKernel
- Version Control: Git, GitHub
- Documentation: Markdown, Jupyter Notebooks
- Code Quality: Ruff, Black, Pyright
- Optional: Scikit-learn, Streamlit, Statsmodels

### Project Structure:
```A clean project structure improves readability and reproducibility.```

video-game-sales-analysis/

├── data/

│ ├── raw/

│ │ └── vgsales.csv

│ ├── processed/

│ └── external/

├── notebooks/

│ ├── 01_data_overview.ipynb

│ ├── 02_data_cleaning.ipynb

│ ├── 03_eda.ipynb

│ └── 04_analysis.ipynb

├── src/

│ ├── ingestion/

│ │ └── load_dataset.py

│ ├── validation/

│ │ └── [schema.py](http://schema.py)

│ ├── cleaning/

│ │ └── clean_sales_data.py

│ ├── features/

│ │ └── feature_engineering.py

│ └── analysis/

│ └── market_analysis.py

├── reports/

│ ├── figures/

│ └── insights/

├── pyproject.toml

└── [README.md](http://README.md)

### Analytical Questions:
#### Core Insights:
These questions form the main story of the analysis.

1. What are the top 10 best-selling video games globally?
2. Which platforms generate the highest global sales?
3. Which genres dominate global video game sales?
4. Which publishers generate the most global revenue?
5. How have video game sales evolved over time?
6. Which year recorded the highest global sales?
7. Which regions contribute the most to global sales?
8. What are the top-performing games in each region (NA, EU, JP)?

Key narrative question:
What drives success in the global video game market?

#### Supporting Insights:
These questions provide additional context and depth to the analysis.

1. Are there any significant differences in genre preferences between regions?
2. How do sales trends differ between platforms over time?
3. Are there any outliers in the dataset, such as games that significantly outperform others?
4. How do sales of top games compare to the average sales in their respective genres or platforms
5. What is the distribution of sales across different price points (if price data is available)?
6. Are there any correlations between game attributes (e.g., genre, platform) and sales performance?
7. How do sales of games released in different decades compare?
8. Are there any seasonal trends in video game sales (e.g., holiday releases)?
9. How do sales of physical copies compare to digital sales (if data is available)?
10. What is the impact of critical reception (e.g., review scores) on sales performance (if data is available)?
11. Are there any notable differences in sales performance between indie games and AAA titles (if data is available)?
12. How do sales of games with different age ratings (e.g., E, T, M) compare (if data is available)?
13. Are there any trends in the types of games that perform well in different regions (e.g., action games in NA vs. RPGs in JP)?
14. How do sales of games with different multiplayer features compare (if data is available)?
15. Are there any correlations between the number of platforms a game is released on and its sales performance?
16. How do sales of games with different marketing budgets compare (if data is available)?

#### Advanced Insights:
These analyses create standout insights for a portfolio project.

1. Can we predict global sales based on game attributes using a machine learning model (if data is available)?
2. Are there any emerging trends in the types of games that are becoming more popular over time?
3. How do sales of games with different monetization models (e.g., free-to-play vs. premium) compare (if data is available)?
4. Can we identify any clusters of similar games based on their attributes and sales performance?
5. How do sales of games with different levels of critical acclaim (e.g., Metacritic scores) compare (if data is available)?
6. Are there any significant differences in sales performance between games developed by different studios (if data is available)?
7. Can we identify any patterns in the release dates of successful games (e.g., do certain months or days of the week correlate with higher sales)?
8. How do sales of games with different types of content (e.g., single-player vs. multiplayer) compare (if data is available)?
9. Are there any correlations between the number of platforms a game is released on and its sales performance?
10. Can we identify any trends in the types of games that perform well in different regions (e.g., action games in NA vs. RPGs in JP)?
11. How do sales of games with different levels of marketing spend compare (if data is available)?
12. Can we identify any patterns in the release dates of successful games (e.g., do certain months or days of the week correlate with higher sales)?
13. Are there any significant differences in sales performance between games developed by different studios (if data is available)?
14. Can we identify any clusters of similar games based on their attributes and sales performance?
15. How do sales of games with different monetization models (e.g., free-to-play vs. premium) compare (if data is available)?
16. Can we predict global sales based on game attributes using a machine learning model (if data is available)?


### EDA Checkpoints
Exploratory data analysis (EDA) will be performed in structured stages.

1. **Initial Data Overview**: Load the dataset and perform basic checks for data types, missing values, and summary statistics.
2. **Data Cleaning**: Handle missing values, correct data types, and remove duplicates if necessary.
3. **Feature Engineering**: Create new features such as total sales, sales ratios, or categorize genres and platforms.
4. **Univariate Analysis**: Analyze the distribution of individual variables (e.g., sales, genres, platforms) using histograms, box plots, and summary statistics.
5. **Bivariate Analysis**: Explore relationships between pairs of variables (e.g., sales vs. genre, sales vs. platform) using scatter plots, bar charts, and correlation analysis.
6. **Multivariate Analysis**: Analyze interactions between multiple variables (e.g., sales vs. genre and platform) using heatmaps, pair plots, and advanced visualizations.
7. **Time Series Analysis**: Analyze sales trends over time using line plots and time series analysis techniques.
8. **Regional Analysis**: Compare sales performance across different regions using grouped bar charts, pie charts, and geographic visualizations if possible.
9. **Outlier Detection**: Identify and analyze outliers in the dataset using box plots and statistical methods.
10. **Advanced Analysis**: Perform any additional analyses that may provide deeper insights, such as clustering, predictive modeling, or sentiment analysis if relevant data is available.

### Data Pipeline Checkpoints
The data pipeline will be developed in stages to ensure reliability and reproducibility.

1. **Data Ingestion**: Implement a function to load the dataset from the raw data directory and perform initial validation checks.
2. **Data Validation**: Define a schema using pandera to validate the structure and types of the data, and implement checks for missing values and consistency.
3. **Data Cleaning**: Implement functions to handle missing values, correct data types, and remove duplicates if necessary.
4. **Feature Engineering**: Implement functions to create new features such as total sales, sales ratios, or categorize genres and platforms.
5. **Testing**: Develop a suite of tests using pytest to ensure the reliability of the data pipeline, including tests for data ingestion, validation, cleaning, and feature engineering.
6. **Documentation**: Document the data pipeline functions and processes in the README.md and Jupyter Notebooks to ensure clarity and reproducibility for future users or employers.
7. **Automation**: Optionally, set up a lightweight automation framework (e.g., using Makefile or a simple Python script) to run the entire data pipeline from ingestion to analysis with a single command.

### Data Schema and Validation
To ensure data quality and consistency, a schema will be defined using the pandera library. This schema will specify the expected structure and types of the data, as well as any constraints on the values.

The schema will include the following fields:
- Rank: Integer, non-negative
- Name: String, non-empty
- Platform: String, non-empty
- Year: Integer, valid year (e.g., between 1970 and the current year)
- Genre: String, non-empty
- Publisher: String, non-empty
- NA_Sales: Float, non-negative
- EU_Sales: Float, non-negative
- JP_Sales: Float, non-negative
- Other_Sales: Float, non-negative
- Global_Sales: Float, non-negative

The validation process will include checks for missing values, data types, and consistency in the dataset. Any issues identified during validation will be addressed in the data cleaning stage to ensure that the analysis is based on high-quality data.


