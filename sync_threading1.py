# Synchronised Threading
import threading
import time

'''cars = 10

lock = threading.Lock()

def double():
    global cars, lock
    lock.acquire()
    while cars < 20:
        cars *= 2
        print(cars)
        time.sleep(2)
    print("Reached The Maximum!")
    lock.release()
    
def halve():
    global cars, lock
    lock.acquire()
    while cars > 1:
        cars /= 2
        print(cars)
        time.sleep(1)
    print("Reached The Minimum!")
    lock.release()
        
t1 = threading.Thread(target=halve)
t2 = threading.Thread(target=double)

t1.start()
t2.start()'''

# Semaphores limit the acces to the resources by placing a number on it.
semaphore = threading.BoundedSemaphore(value=5)

def access(thread_number):
    print("{} is trying to access!".format(thread_number))