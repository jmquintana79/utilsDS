# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2018-09-03 15:40:43
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2018-09-03 17:21:15

"""
RUN EXPERIMENTS using MLFLOW.
"""

import sys
sys.path.append('../')
from models.metrics import metrics_regression

import click
import warnings
import mlflow
import mlflow.sklearn


# # arguments: general
from experiments.arguments import *

# # load data
from experiments.load import data
dfdata = data()


@click.command()
@click.argument('exp_num', type=click.INT)
@click.option('--alpha', default=0.5, help='alpha regularization term.', type=click.FLOAT)
@click.option('--l1_ratio', default=0.5, help='l1 regularization term.', type=click.FLOAT)
def main(exp_num, alpha, l1_ratio):
    """
    Launch an experiment.
    """
    warnings.filterwarnings("ignore")

    # header
    click.secho('Experiment: %s' % exp_num, bold=True, underline=True, bg='blue')

    # # arguments: experiment
    click.secho('[arg] alpha = %s' % alpha, fg='green')
    click.secho('[arg] l1_ratio = %s' % l1_ratio, fg='green')

    # with mlflow.start_run():
    # # model
    from experiments import model
    test_y, test_yhat, k = model.launcher(dfdata, alpha, l1_ratio)

    # # scoring
    dmetrics = metrics_regression(test_y, test_yhat, k)
    # print metrics
    click.echo("[info] Metrics: ")
    click.secho("  BIAS: %s" % dmetrics['bias'], fg='red')
    click.secho("  MAE: %s" % dmetrics['mae'], fg='red')
    click.secho("  R2: %s" % dmetrics['r2'], fg='red')

    # tracking
    mlflow.log_param("alpha", alpha)
    mlflow.log_param("l1_ratio", l1_ratio)
    mlflow.log_metric("bias", dmetrics['bias'])
    mlflow.log_metric("mae", dmetrics['mae'])
    mlflow.log_metric("r2", dmetrics['r2'])


if __name__ == '__main__':
    main()
