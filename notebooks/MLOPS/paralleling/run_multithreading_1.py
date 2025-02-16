# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2025-02-16 19:36:41
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2025-02-16 19:49:30


import threading
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
    max_hilos = 3  # Número máximo de hilos concurrentes
    sem = threading.Semaphore(max_hilos)
    floors = []
    for floor in range(10, 0, -1):
        logging.info(f"Launching floor {floor}")
        t = threading.Thread(target=stop_at_floor, args=(floor, sem))
        t.start()
        floors.append(t)

    for t in floors:
        t.join()  # Espera a que todos los hilos terminen

if __name__ == "__main__":
    elevator()
