import time
import sys

def main(plant:str):
    print(plant)
    time.sleep(3)
    return None

if __name__ == "__main__":
    plant = sys.argv[1]
    main(plant)