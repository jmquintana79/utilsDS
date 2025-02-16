# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2025-02-16 19:36:41
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2025-02-16 21:40:29


import multiprocessing
import time
import logging
logging.basicConfig(level=logging.INFO)
logging.info("Start ...")

def stop_at_floor(floor, sem):
    with sem: 
        logging.info(f"elevator moving to floor {floor}")
        time.sleep(floor)
        logging.info(f"elevator stops on floor {floor}")

def elevator():
    max_procesos = 3  # Número máximo de hilos concurrentes
    sem = multiprocessing.BoundedSemaphore(max_procesos)
    floors = []
    for floor in range(10, 0, -1):
        logging.info(f"Launching floor {floor}")
        p = multiprocessing.Process(target=stop_at_floor, args=(floor, sem))
        p.start()
        floors.append(p)

    for p in floors:
        p.join()  # Espera a que todos los hilos terminen

if __name__ == "__main__":
    elevator()

