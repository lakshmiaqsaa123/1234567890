#shared memory variables
CAPACITY = 10
buffer = [-1 for 1 in range(CAPACITY)]
in_index = 0
out_index= 0
#Declaring Semaphores
mutex = threading.Semaphore()
empty = threading.Semaphore(CAPACITY)
full = threading.Semaphore(0)
#Producer Thread Class
class Producer (threading.Thread) :
    def run(se1f) :
        global CAPACITY, buffer, in_index, out_index
        global mutex, empty, full

        items_produced = 0
        counter = 0

        while items_produced < 3:
            empty.acquire()
            mutex.acquire()

            counter += 1
            buffer[in_index] = counter
            in_index = (in_index + 1)%CAPACITY
            print("Producer produced :", counter)

            mutex.release()
            full.release()

            time.sleep(1)

            items_produced += 1

# Consumer Thread Class
class Consumer(threading.Thread):
    def run(self):

        global CAPACITY, buffer, in_index, out_index, counter
        global mutex, empty, full

        items_consumed < 3:
            full.acquire()
            mutex.acquire()

            item= buffer[out_index]
            out_index = (out_index + i)%CAPACITY
            print("Consumer consumed item 1", item)

            mutex.release()
            empty.release()

            time.sleep(2.5)

            items_consumed += 1
#creating Threads
producer = Producer()
consumer = Consumer()

#Starting Threads
consumer.start()
producer.start()

#Waiting for threads to complete
producer.join()
consumer.join()

    
        
