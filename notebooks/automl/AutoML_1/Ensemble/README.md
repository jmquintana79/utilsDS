# Summary of Ensemble

[<< Go back](../README.md)


## Ensemble structure
| Model             |   Weight |
|:------------------|---------:|
| 2_DecisionTree    |        2 |
| 4_Default_Xgboost |        3 |

### Metric details
|           |   0 |         1 |         2 |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|----:|----------:|----------:|-----------:|------------:|---------------:|----------:|
| precision |   1 |  1        |  0.866667 |   0.947368 |    0.955556 |       0.954386 |  0.127714 |
| recall    |   1 |  0.846154 |  1        |   0.947368 |    0.948718 |       0.947368 |  0.127714 |
| f1-score  |   1 |  0.916667 |  0.928571 |   0.947368 |    0.948413 |       0.947055 |  0.127714 |
| support   |  12 | 13        | 13        |   0.947368 |   38        |      38        |  0.127714 |


## Confusion matrix
|              |   Predicted as 0 |   Predicted as 1 |   Predicted as 2 |
|:-------------|-----------------:|-----------------:|-----------------:|
| Labeled as 0 |               12 |                0 |                0 |
| Labeled as 1 |                0 |               11 |                2 |
| Labeled as 2 |                0 |                0 |               13 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
