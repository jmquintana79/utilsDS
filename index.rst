.
├── LICENSE
├── README.md
├── TODO.md
├── environment.yml
├── index.rst
├── notebooks
│   ├── analysis
│   │   ├── EDA
│   │   │   ├── notebook-EDA1-whole_data.ipynb
│   │   │   ├── notebook-EDA2-relationships.ipynb
│   │   │   └── notebook-EDA3-splitted_data.ipynb
│   │   ├── errors
│   │   │   └── notebook-error_analysis.ipynb
│   │   └── fourier
│   │       ├── notebook-Fourier_Analysis-Solar_Example.ipynb
│   │       └── notebook-Fourier_transformation.ipynb
│   ├── datasets
│   │   └── notebook-dataset-sklearn2csv.ipynb
│   ├── feature_engineering
│   │   └── selection
│   │       └── notebook-features_selection-sklearn.ipynb
│   ├── pipelines
│   │   └── notebook-dev_pipelines.ipynb
│   ├── preprocessing
│   │   └── anomalies
│   │       ├── notebook-outliers_detection-2D.ipynb
│   │       └── notebook-steps_detection.ipynb
│   └── similarity
│       └── notebook-similarity_distance-Dynamic_Time_Warping-check.ipynb
├── scripts
│   ├── analysis
│   │   └── errors
│   │       ├── __init__.py
│   │       ├── classification.py
│   │       └── regression.py
│   ├── data
│   │   ├── __init__.py
│   │   └── model.py
│   ├── datasets
│   │   ├── README.md
│   │   ├── __init__.py
│   │   ├── boston.py
│   │   ├── data
│   │   │   ├── dataset.prediction.csv.gz
│   │   │   ├── dataset.solar.csv.gz
│   │   │   ├── dataset.weather.csv.gz
│   │   │   └── dataset.wine.csv.gz
│   │   ├── diabetes.py
│   │   ├── iris.py
│   │   ├── kaggle
│   │   │   └── titanic
│   │   │       ├── load.py
│   │   │       ├── summary-test.txt
│   │   │       ├── summary-train.txt
│   │   │       ├── test.csv.gz
│   │   │       └── train.csv.gz
│   │   ├── prediction.py
│   │   ├── solar.py
│   │   ├── summaries
│   │   │   ├── summary-dataset.boston.txt
│   │   │   ├── summary-dataset.diabetes.txt
│   │   │   ├── summary-dataset.iris.txt
│   │   │   ├── summary-dataset.solar.txt
│   │   │   ├── summary-dataset.weather.txt
│   │   │   └── summary-dataset.wine.txt
│   │   ├── tools
│   │   │   ├── notebook-create_dataset.ipynb
│   │   │   └── tool-summary_csv.sh
│   │   ├── weather.py
│   │   └── wine.py
│   ├── models
│   │   ├── CustomDeco.py
│   │   ├── LinearRegressor.py
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── gam
│   │   │   └── notebook-GAM.ipynb
│   │   ├── metrics.py
│   │   ├── templates.py
│   │   ├── tuning.py
│   │   └── xgboost
│   │       ├── notebook-DMatrix-data_structure.ipynb
│   │       ├── test-any_regressor_tuning4.py
│   │       ├── test-xgboost_tuning1.py
│   │       ├── test-xgboost_tuning2.py
│   │       └── test-xgboost_tuning3.py
│   ├── pipelines
│   │   ├── __init__.py
│   │   ├── custom.py
│   │   └── xpipes.py
│   ├── plot
│   │   └── github_activity.py
│   ├── preprocessing
│   │   ├── __init__.py
│   │   ├── outliers
│   │   │   ├── median1D.py
│   │   │   ├── median2D.py
│   │   │   └── multigaussian.py
│   │   ├── preparation.py
│   │   ├── scalers
│   │   │   └── normalization.py
│   │   └── smoothers
│   │       └── lowess.py
│   └── utils
│       ├── __init__.py
│       ├── columns.py
│       ├── datasets.py
│       ├── reader.py
│       ├── saver.py
│       └── timer.py
└── tools
    ├── data_understanding
    │   └── tool-summary_csv.sh
    └── experiments_mlflow
        ├── arguments.py
        ├── load.py
        ├── main.py
        ├── model.py
        └── notebook-experiments_manager.ipynb

35 directories, 84 files
