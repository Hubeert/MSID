# Oral Cancer Data Analysis (Projekt MSiD Część Pierwsza)

## Project Overview

This project aims to analyze and visualize oral cancer data using Python. The main objectives are:

- Setting up a Python development environment.
- Performing exploratory data analysis (EDA).
- Computing descriptive statistics for numerical and categorical features.
- Identifying missing values.
- Visualizing data distributions and relationships.

## Installation

To set up the project, follow these steps:

### 1. Clone the Repository

```sh
 git clone <repository_url>
 cd <repository_folder>
```

### 2. Create and Activate a Virtual Environment

```sh
python -m venv venv
venv\Scripts\activate
```

### 3. Install Required Packages

```sh
pip install -r requirements.txt
```

## Project Structure

```
├── data/              # Contains the dataset (oral.csv)
├── pngs/              # Contains the results of the analysis
├── scripts/           # Python scripts for analysis and visualization
├── notebooks/         # (Currently unused) Jupyter Notebooks for further exploration
├── requirements.txt   # List of required dependencies
└── README.md          # Project documentation
```

## Dataset

The dataset is located in `data/oral.csv` and includes various features related to oral cancer risk factors.

## Usage

There are two possible ways of using the project. First, by using separate files to visualize data analysis and second,
by using multiple methods at once with main.py script. Currently, it contains sample visualisations of the most interesting associations between clsses.
It is possible to change parameters of the methods and use them more than once.

## License

This project is for educational purposes and does not have a specific license.




