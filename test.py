import sys  
import _thread
import time

def test(val):
    while 1:
        print(val)
        time.sleep(5)

threads = []


try:
  thread1 = _thread.start_new_thread( test, ("Thread-1",) )
  thread2 = _thread.start_new_thread( test, ("Thread-2",) )
  
  threads.append(thread1)
  threads.append(thread2)
except:
   print ("Error: unable to start thread")



while 1 : 
    pass

