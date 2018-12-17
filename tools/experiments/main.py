# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2018-09-03 15:40:43
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2018-09-04 10:56:17

"""
RUN EXPERIMENTS using MLFLOW:

# create experiment
$ mlflow experiments create <<experiment_name>>
# check necesary arguments
$ python3.6 main.py --help
# launch experiment
$ python3.6 main.py <<experiment_id>> [OPTIONS]
# check result with the graphical tracker
$ mlflow ui
"""

import sys
sys.path.append('../')
from models.metrics import metrics_regression

import click
import warnings
import mlflow
import mlflow.sklearn


# # available experiments
from mlflow.tracking import get_service
# get service
service = get_service()
# returns a list of mlflow.entities.Experiment
experiments = service.list_experiments()
# collect experiments information
lidexp = list()
didexp = dict()
for ii, iexp in enumerate(experiments):
    lidexp.append(iexp.experiment_id)
    didexp[iexp.experiment_id] = {'name': iexp.name, 'location': iexp.artifact_location}


# # ARGUMENTS: GENERAL
from experiments.arguments import *


# # LOAD DATA
from experiments.load import data
dfdata = data()


@click.command()
@click.argument('exp_id', type=click.INT)
@click.option('--alpha', default=0.5, help='alpha regularization term.', type=click.FLOAT)
@click.option('--l1_ratio', default=0.5, help='l1 regularization term.', type=click.FLOAT)
def main(exp_id, alpha, l1_ratio):
    """
    Launch an experiment.
    """
    warnings.filterwarnings("ignore")

    # # validate experiment availability
    if not exp_id in lidexp:
        click.secho('[error] an experiment with id "%s" is not available.' % exp_id, bold=True, fg='red')
        quit('Aborted!')
    else:
        # header
        click.secho('Experiment: id=%s  name=%s' % (exp_id, didexp[exp_id]['name']), bold=True, underline=True, bg='blue')
    # confirmation
    click.confirm('Do you want to continue?', default=False, abort=True, prompt_suffix=': ', show_default=True, err=False)

    # # ARGUMENTS: EXPERIMENT
    click.secho('[arg] alpha = %s' % alpha, fg='green')
    click.secho('[arg] l1_ratio = %s' % l1_ratio, fg='green')

    # runner
    with mlflow.start_run(experiment_id=exp_id):

        # # MODEL
        from experiments import model
        test_y, test_yhat, k = model.launcher(dfdata, alpha, l1_ratio)

        # # SCORES
        dmetrics = metrics_regression(test_y, test_yhat, k)
        # print metrics
        click.echo("[info] Metrics: ")
        click.secho("  BIAS: %s" % dmetrics['bias'], fg='blue')
        click.secho("  MAE: %s" % dmetrics['mae'], fg='blue')
        click.secho("  R2: %s" % dmetrics['r2'], fg='blue')

        # tracking
        mlflow.log_param("alpha", alpha)
        mlflow.log_param("l1_ratio", l1_ratio)
        mlflow.log_metric("bias", dmetrics['bias'])
        mlflow.log_metric("mae", dmetrics['mae'])
        mlflow.log_metric("r2", dmetrics['r2'])


if __name__ == '__main__':
    main()
