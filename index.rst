.
├── environment.yml
├── index.rst
├── libraries
│   ├── data
│   │   ├── cArray.py
│   │   └── __init__.py
│   ├── datasets
│   │   ├── boston.py
│   │   ├── data
│   │   │   ├── dataset.prediction.csv.gz
│   │   │   ├── dataset.solar.csv.gz
│   │   │   ├── dataset.weather.csv.gz
│   │   │   └── dataset.wine.csv.gz
│   │   ├── diabetes.py
│   │   ├── __init__.py
│   │   ├── iris.py
│   │   ├── kaggle
│   │   │   └── titanic
│   │   │       ├── load.py
│   │   │       ├── summary-test.txt
│   │   │       ├── summary-train.txt
│   │   │       ├── test.csv.gz
│   │   │       └── train.csv.gz
│   │   ├── prediction.py
│   │   ├── __pycache__
│   │   │   ├── boston.cpython-36.pyc
│   │   │   ├── __init__.cpython-36.pyc
│   │   │   ├── prediction.cpython-36.pyc
│   │   │   ├── solar.cpython-36.pyc
│   │   │   └── weather.cpython-36.pyc
│   │   ├── README.md
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
│   │   ├── base.py
│   │   ├── CustomDeco.py
│   │   ├── gam
│   │   │   └── notebook-GAM.ipynb
│   │   ├── __init__.py
│   │   ├── LinearRegressor.py
│   │   ├── metrics.py
│   │   ├── __pycache__
│   │   │   ├── base.cpython-36.pyc
│   │   │   ├── __init__.cpython-36.pyc
│   │   │   └── metrics.cpython-36.pyc
│   │   ├── templates.py
│   │   ├── tuning.py
│   │   └── xgboost
│   │       ├── notebook-DMatrix-data_structure.ipynb
│   │       ├── test-any_regressor_tuning4.py
│   │       ├── test-xgboost_tuning1.py
│   │       ├── test-xgboost_tuning2.py
│   │       └── test-xgboost_tuning3.py
│   ├── pipelines
│   │   ├── custom.py
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── custom.cpython-36.pyc
│   │   │   ├── __init__.cpython-36.pyc
│   │   │   ├── transformer.cpython-36.pyc
│   │   │   └── xpipes.cpython-36.pyc
│   │   └── xpipes.py
│   ├── plot
│   │   └── github_activity.py
│   ├── preprocessing
│   │   ├── __init__.py
│   │   ├── outliers
│   │   │   ├── median1D.py
│   │   │   ├── median2D.py
│   │   │   ├── multigaussian.py
│   │   │   └── __pycache__
│   │   │       └── median2D.cpython-36.pyc
│   │   ├── preparation.py
│   │   ├── __pycache__
│   │   │   └── __init__.cpython-36.pyc
│   │   ├── scalers
│   │   │   ├── normalization.py
│   │   │   └── __pycache__
│   │   │       └── normalization.cpython-36.pyc
│   │   └── smoothers
│   │       └── lowess.py
│   ├── tools
│   │   ├── columns.py
│   │   ├── datasets.py
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── columns.cpython-35.pyc
│   │   │   ├── columns.cpython-36.pyc
│   │   │   ├── datasets.cpython-35.pyc
│   │   │   ├── datasets.cpython-36.pyc
│   │   │   ├── datasets.cpython-37.pyc
│   │   │   ├── __init__.cpython-35.pyc
│   │   │   ├── __init__.cpython-36.pyc
│   │   │   ├── __init__.cpython-37.pyc
│   │   │   ├── reader.cpython-35.pyc
│   │   │   ├── reader.cpython-36.pyc
│   │   │   └── timer.cpython-36.pyc
│   │   ├── reader.py
│   │   ├── saver.py
│   │   └── timer.py
│   └── validation
│       ├── classification.py
│       ├── __init__.py
│       └── regression.py
├── LICENSE
├── notebooks
│   ├── data_analysis
│   │   ├── EDA
│   │   │   ├── notebook-EDA1-whole_data.ipynb
│   │   │   ├── notebook-EDA2-relationships.ipynb
│   │   │   └── notebook-EDA3-splitted_data.ipynb
│   │   ├── fourier_analysis
│   │   │   ├── notebook-Fourier_Analysis-Solar_Example.ipynb
│   │   │   └── notebook-Fourier_transformation.ipynb
│   │   └── validation
│   │       └── notebook-error_analysis.ipynb
│   ├── datasets
│   │   └── notebook-dataset-sklearn2csv.ipynb
│   ├── feature_engineering
│   │   └── selection
│   │       └── notebook-features_selection-sklearn.ipynb
│   ├── pipelines
│   │   └── notebook-dev_pipelines.ipynb
│   ├── preprocessing
│   │   └── outliers
│   │       └── notebook-outliers_detection-2D.ipynb
│   └── similarity
│       └── notebook-similarity_distance-Dynamic_Time_Warping-check.ipynb
├── README.md
├── TODO.md
└── tools
    ├── data_understanding
    │   └── tool-summary_csv.sh
    └── experiments
        ├── arguments.py
        ├── load.py
        ├── main.py
        ├── mlruns
        │   ├── 0
        │   │   └── meta.yaml
        │   └── 1
        │       ├── 0f6fe20f93614e678fc3241dc8d3be73
        │       │   ├── artifacts
        │       │   ├── meta.yaml
        │       │   ├── metrics
        │       │   │   ├── bias
        │       │   │   ├── mae
        │       │   │   └── r2
        │       │   └── params
        │       │       ├── alpha
        │       │       └── l1_ratio
        │       ├── 2fd40b6510ed4fcd9c20340ad4861dd5
        │       │   ├── artifacts
        │       │   ├── meta.yaml
        │       │   ├── metrics
        │       │   │   ├── bias
        │       │   │   ├── mae
        │       │   │   └── r2
        │       │   └── params
        │       │       ├── alpha
        │       │       └── l1_ratio
        │       ├── 468e577d5bb240e8a4e9f6e88ccdbd55
        │       │   ├── artifacts
        │       │   ├── meta.yaml
        │       │   ├── metrics
        │       │   └── params
        │       ├── 4892a411107648999c7532b39ecb8d12
        │       │   ├── artifacts
        │       │   ├── meta.yaml
        │       │   ├── metrics
        │       │   └── params
        │       ├── 5fb3e4454f224a3ca859f3ab43473210
        │       │   ├── artifacts
        │       │   ├── meta.yaml
        │       │   ├── metrics
        │       │   └── params
        │       ├── 960b1f175777490f99a00111236b37a0
        │       │   ├── artifacts
        │       │   ├── meta.yaml
        │       │   ├── metrics
        │       │   └── params
        │       ├── 9bf94e8820244537967da588d5cc2170
        │       │   ├── artifacts
        │       │   ├── meta.yaml
        │       │   ├── metrics
        │       │   └── params
        │       ├── a7e313b0b7a74a1f9be14592c98a5317
        │       │   ├── artifacts
        │       │   ├── meta.yaml
        │       │   ├── metrics
        │       │   │   ├── bias
        │       │   │   ├── mae
        │       │   │   └── r2
        │       │   └── params
        │       │       ├── alpha
        │       │       └── l1_ratio
        │       ├── afcdb67ab52c40c8b977ddd13b57684c
        │       │   ├── artifacts
        │       │   ├── meta.yaml
        │       │   ├── metrics
        │       │   └── params
        │       ├── c2181c8caeb44f6b95c6814c980c1822
        │       │   ├── artifacts
        │       │   ├── meta.yaml
        │       │   ├── metrics
        │       │   │   ├── bias
        │       │   │   ├── mae
        │       │   │   └── r2
        │       │   └── params
        │       │       ├── alpha
        │       │       └── l1_ratio
        │       └── meta.yaml
        ├── model.py
        ├── notebook-experiments_manager.ipynb
        └── __pycache__
            ├── arguments.cpython-36.pyc
            ├── load.cpython-36.pyc
            └── model.cpython-36.pyc

85 directories, 144 files
