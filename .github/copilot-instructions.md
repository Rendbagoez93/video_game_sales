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

│ │ └── video_games_sales.csv

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

├── visualization/

│ ├── __init__.py

│ ├── charts.py

│ └── dashboard.py

├── reports/

│ ├── figures/

│ └── insights/

├── main.py

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
4. How do sales of top games compare to the average sales in their respective genres or platforms?
5. Are there any correlations between game attributes (e.g., genre, platform) and sales performance?
6. How do sales of games released in different decades compare?
7. Are there any trends in the types of games that perform well in different regions (e.g., action games in NA vs. RPGs in JP)?
8. Are there any correlations between the number of platforms a game is released on and its sales performance?

#### Advanced Insights:
These analyses create standout insights for a portfolio project.

1. Can we predict global sales based on game attributes (Genre, Platform, Publisher, Year) using a machine learning model?
2. Are there any emerging trends in the types of games that are becoming more popular over time?
3. Can we identify any clusters of similar games based on their attributes and sales performance?


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

### Notebook Writing Style
When writing Jupyter Notebooks for this project, the following style guidelines will be followed to ensure clarity and readability:

1. **Markdown Cells**: Use markdown cells to provide clear explanations of the code, the analysis process, and the insights being derived. Each section of the notebook should have a descriptive heading.
2. **Code Cells**: Write clean and well-commented code in code cells. Each code cell should perform a specific task, and comments should explain the purpose of the code and any important details.
3. **Visualizations**: Include visualizations to support the analysis and insights. Each visualization should have a descriptive title and axis labels where appropriate.
4. **Narrative Flow**: Ensure that the notebook has a logical flow, with each section building on the previous one. The narrative should guide the reader through the analysis process and lead to clear conclusions.
5. **Reproducibility**: Ensure that the notebook can be run from start to finish without errors, and that all necessary data and dependencies are included or clearly documented. This will allow others to reproduce the analysis and understand the insights derived from the data.
6. **Summary and Conclusions**: At the end of the notebook, include a summary of the key findings and insights derived from the analysis, along with any recommendations or implications for the video game industry based on the data.
7. **Others**: Follow best practices for code style, such as using meaningful variable names, avoiding hard-coded values, and adhering to PEP 8 guidelines for Python code. Make the notebook is kaggle-ready, with a clear and engaging narrative that highlights the insights derived from the data.

