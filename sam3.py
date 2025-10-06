from datetime import datetime
import time

def show_time():
    for i in range(5):  
        print(datetime.now().strftime("%H:%M:%S"))
        time.sleep(1)

if __name__ == "__main__":
    show_time()
