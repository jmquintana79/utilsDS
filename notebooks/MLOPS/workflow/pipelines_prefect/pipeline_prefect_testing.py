# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2025-02-16 15:31:49
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2025-02-16 19:34:08

from prefect import task, flow, get_run_logger
from prefect.exceptions import Abort
from prefect.states import Completed, Failed
import pandas as pd
from datetime import datetime, timezone
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

@task
def tarea_que_puede_saltar(valor):
    if valor < 0:
        raise Abort("Valor negativo, terminando tarea.")
    elif valor == 0:
        return Failed(message="How did this happen!?")
    else:
        return Completed(message="I am happy with this result", name="Skipped")
    
# 1. Lectura de datos
@task(name="Reading Data Task", retries=3, retry_delay_seconds=5, timeout_seconds=60)
def read_data():
    logger = get_run_logger()
    # Para el ejemplo, usaremos un dataset público de Scikit-learn como si fuera un archivo CSV
    from sklearn.datasets import load_iris
    data = load_iris()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['target'] = data.target
    logger.info(f"Loaded data: {df.shape}")
    return df

# 2. Preparación de datos
@task(name="Data Preparation Task")
def prepare_data(df: pd.DataFrame):
    # Dividimos los datos en características (X) y etiquetas (y)
    X = df.drop(columns=["target"])
    y = df["target"]
    
    # Dividimos en conjunto de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

# 3. Entrenamiento del modelo
@task(name = "Model Training Task")
def train_model(X_train, y_train):
    # Creamos un modelo de Random Forest y lo entrenamos
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

# 4. Evaluación del modelo
@task(name = "Evaluate Model Task")
def evaluate_model(model, X_test, y_test):
    logger = get_run_logger()
    # Realizamos predicciones
    y_pred = model.predict(X_test)
    
    # Calculamos la precisión del modelo
    accuracy = accuracy_score(y_test, y_pred)
    logger.info(f"Accuracy: {accuracy}")
    return accuracy

@flow(name="My first flow", version="0.1.0", flow_run_name="{name}-on-{date:%A}")
def mi_flujo(name:str = "Juan", date:datetime=datetime.now(timezone.utc)):
    tarea_que_puede_saltar(4)
    # Paso 1: Leer los datos
    df = read_data()
    # Paso 2: Preparar los datos
    X_train, X_test, y_train, y_test = prepare_data(df)
    # Paso 3: Entrenar el modelo
    model = train_model(X_train, y_train)
    # Paso 4: Evaluar el modelo
    accuracy = evaluate_model(model, X_test, y_test)


if __name__ == "__main__":
    mi_flujo(name="marvin", date=datetime.now(timezone.utc))


