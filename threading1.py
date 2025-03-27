# Threading helps you run multiple functions simultaneously.
import threading

'''def function1():
    for x in range(5):
        print("God is Good!")
        
def function2():
    for x in range(5):
        print("All The Time, God is Good!")


t1 = threading.Thread(target=function1)
t2 = threading.Thread(target=function2)

t1.start()
t2.start()'''
# The above lets you run the functions in sequence.

'''def asda():
    for x in range(5):
        print("ASDA is hiring!")

t1 = threading.Thread(target=asda)
t1.start()

t1.join()

print("End of Layoffs") '''
# The above  runs the main function and prints "End of Layoffs" after the thread is done.