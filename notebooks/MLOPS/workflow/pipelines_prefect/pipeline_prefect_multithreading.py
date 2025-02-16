# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2025-02-16 18:09:05
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2025-02-16 18:34:29


from prefect import flow, task, get_run_logger
from prefect.futures import wait
from prefect.task_runners import ThreadPoolTaskRunner
import time
import logging
# Configurar el logger para escribir en un archivo
log_file = "log_prefect_multithreading.log"  # Archivo donde se guardarán los logs
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.INFO)  # Nivel de logs
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
file_handler.setFormatter(formatter)

# Agregar el manejador de archivo al logger raíz de Prefect
logging.getLogger("prefect").addHandler(file_handler)

@task
def stop_at_floor(floor):
    logger = get_run_logger()
    logger.info(f"elevator moving to floor {floor}")
    time.sleep(floor)
    logger.info(f"elevator stops on floor {floor}")


@flow(task_runner=ThreadPoolTaskRunner(max_workers=4), flow_run_name='Juan-Today' )
def elevator():
    logger = get_run_logger()
    logger.info("Iniciando flujo") 
    floors = []

    for floor in range(10, 0, -1):
        logger.info(f"Launching floor {floor}")
        floors.append(stop_at_floor.submit(floor))

    wait(floors)
    logger.info("Finalizando flujo") 

if __name__ == "__main__":
    elevator() 