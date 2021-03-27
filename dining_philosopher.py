import threading
import time
import sys
philosophers_num = sys.argv [1]
go = True


class Philosopher(threading.Thread): #this thing is a thread
    def __init__(self, threadID, left_fork, right_fork):
        threading.Thread.__init__(self)
        self.id = threadID
        self.left_fork = left_fork
        self.right_fork = right_fork

    def run(self): 
        global go

        while go:
            print(f"philosopher {self.id} is thinking...")
            self.left_fork.acquire()
            print(f"philosopher {self.id} picks up left fork.")
            acquired = self.right_fork.acquire(False)
            if acquired:
                print(f"philosopher {self.id} picks up right fork")
                print(f"philosopher {self.id} is eating...")            #
                self.left_fork.release()                                #This block doesn't seem to
                print(f"philosopher {self.id} puts down left fork.")    #be running
                self.right_fork.release()                               #
                print(f"philosopher {self.id} puts down right fork.")   #
                break                                                   #
            else:
                self.left_fork.release()
                print(f"philosopher {self.id} puts down left fork.")
            time.sleep(.1)
       


def main():
    global philosophers_num
    global go

    philosophers_num = int(sys.argv [1])
    threads = []
    locks = []
    #locks.append(lock)
    for i in range(philosophers_num):
        lock = threading.Lock()
        locks.append(lock)
    for i in range(philosophers_num):
        thread = Philosopher(i, locks[i], locks[(i+1)%philosophers_num]) #shows out of range
        threads.append(thread)

    for i in range(philosophers_num):
        threads[i].start()

    time.sleep(.2)
    go = False

main()

#, locks[i], locks[i+1%philosophers_num]
#^^goes in thread after Philosopher i