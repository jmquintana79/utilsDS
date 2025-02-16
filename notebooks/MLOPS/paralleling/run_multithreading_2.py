# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2025-02-16 19:36:41
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2025-02-16 19:50:06

import time
import concurrent.futures
import logging
logging.basicConfig(level=logging.INFO)
logging.info("Start ...")

def stop_at_floor(floor):
    logging.info(f"elevator moving to floor {floor}")
    time.sleep(floor)
    logging.info(f"elevator stops on floor {floor}")

def elevator():
    max_workers = 3  # Número máximo de hilos en paralelo
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        executor.map(stop_at_floor, range(10, 0, -1))  # Lanza 10 tareas, pero solo 3 simultáneas

if __name__ == "__main__":
    elevator()
