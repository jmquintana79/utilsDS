# Summary of 5_Default_NeuralNetwork

[<< Go back](../README.md)


## Neural Network
- **dense_1_size**: 32
- **dense_2_size**: 16
- **learning_rate**: 0.05
- **num_class**: 3
- **explain_level**: 2

## Validation
 - **validation_type**: split
 - **train_ratio**: 0.75
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
logloss

## Training time

1.7 seconds

### Metric details
|           |   setosa |   versicolor |   virginica |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------:|-------------:|------------:|-----------:|------------:|---------------:|----------:|
| precision | 0.9      |     1        |    0.642857 |   0.785714 |    0.847619 |       0.853061 |  0.870568 |
| recall    | 1        |     0.4      |    1        |   0.785714 |    0.8      |       0.785714 |  0.870568 |
| f1-score  | 0.947368 |     0.571429 |    0.782609 |   0.785714 |    0.767135 |       0.760146 |  0.870568 |
| support   | 9        |    10        |    9        |   0.785714 |   28        |      28        |  0.870568 |


## Confusion matrix
|                       |   Predicted as setosa |   Predicted as versicolor |   Predicted as virginica |
|:----------------------|----------------------:|--------------------------:|-------------------------:|
| Labeled as setosa     |                     9 |                         0 |                        0 |
| Labeled as versicolor |                     1 |                         4 |                        5 |
| Labeled as virginica  |                     0 |                         0 |                        9 |

## Learning curves
![Learning curves](learning_curves.png)

## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)

[<< Go back](../README.md)
