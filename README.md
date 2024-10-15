
# 📈 forecast-exercise

## Objective
The objective of this exercise is to evaluate the candidate's skills in time series analysis and forecasting using Machine Learning techniques. The candidate is expected to demonstrate proficiency in data handling, predictive modeling, model validation, and interpretation of results.

## Exercise Description
The candidate will be required to develop a predictive model to forecast the daily sales of a retail store chain from a provided time series. The task includes the following steps:
1. **🔍 Data Exploration:** Understand the dataset, identify trends, seasonality, and any anomalies.
2. **🧹 Data Cleaning:** Handle missing values, outliers, and perform any necessary data preprocessing.
3. **🎯 Feature Selection:** Select relevant features that could improve the predictive power of the model.
4. **🤖 Modeling:** Develop a predictive model using appropriate Machine Learning techniques.
5. **✅ Validation:** Validate the model using appropriate metrics and validation techniques.
6. **📊 Presentation of Results:** Interpret the results and present the findings in a clear and concise manner.

## Requirements
Use the dependency manager (and/or virtual environment) of your choice for this exercise. The following requirements are an example of proposal. Use any other relevant libraries for time series analysis and machine learning you need.

- python 3.10+
- pandas
- scikit-learn
- plotly

## Installation
Clone the repository and install the required packages using pip:

```bash
git clone https://github.com/yourusername/forecast-exercise.git
cd forecast-exercise
```

## Usage
1. Navigate to the project directory:

    ```bash
    cd forecast-exercise
    ```

2. Start Jupyter Notebook:

    ```bash
    jupyter notebook
    ```

3. Open the provided notebook `notebooks/1-data-preparation.ipynb` and follow the instructions to complete the exercise.

4. Once you have completed the first notebook continue with the second one `notebooks/2-model-training.ipynb`.

5. If you have arrived to a point where you have a working model, please continue by developing an API you will use to make the model available through an endpoint using the `app/main.py` file.

## Directory Structure
```
forecast-exercise/
├── README.md
├── app
│   └── main.py
├── data
│   ├── calendar.csv
│   ├── ipc_history.csv
│   ├── sales_test_submission.csv
│   └── sales_train_dataset.csv
└── notebooks
    ├── 1-data-preparation.ipynb
    └── 2-model-training.ipynb
```

## Submission
📂 Please complete the exercises in the provided Jupyter Notebooks and submit this repository zipped along with any additional scripts or documentation you used to complete the exercise.

## Evaluation Criteria
- **🧼 Data Handling:** Proficiency in data cleaning and preprocessing.
- **🤖 Predictive Modeling:** Ability to build and tune machine learning models.
- **✅ Model Validation:** Appropriate validation techniques and metrics used.
- **📊 Interpretation of Results:** Clear and insightful interpretation of the model's results.
- **📝 Presentation:** Clarity and organization of the notebook and code.

Good luck, and happy forecasting!
