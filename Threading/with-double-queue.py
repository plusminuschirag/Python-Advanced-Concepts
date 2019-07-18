#Why we need double queue?
#Because operations like print are heavy to do and when they are accessed by seprate threads, it may go downhill
#faster than lance armstrong's foundation. So if you believe in good karma don't use print function in that
#Use a queue and when done print the results


from queue import Queue
from threading import Thread
import time
import requests # Install requests module first.

THREAD_POOL_SIZE = 4
pairs = ["XRPBTC","XRPETH","XRPINR","BTCINR","XRPUSDT","ETHUSDT","BTCUSDT","BTCTUSD","BTCUSDC"]

started = time.time()
    
def fetch_pair(pair):
    url = "https://api.coindcx.com/exchange/v1/trades/" + pair
    response = requests.get(url)
    data = response.json()
    return data['trade_data'][0]

pairQueue = Queue()
for pair in pairs:
    pairQueue.put(pair)
resultQueue = Queue()


def dataFetcher(pairQueue,resultQueue):
    while not pairQueue.empty():
        try:
            pair = pairQueue.get(block=False)
        except Empty:
            break
        else:
            resultQueue.put(fetch_pair(pair))
            pairQueue.task_done()

threads = [Thread(target=dataFetcher,args=(pairQueue,resultQueue)) for _ in range(THREAD_POOL_SIZE)]

for thread in threads:
    thread.start()

pairQueue.join()

while threads:
    threads.pop().join()

while not resultQueue.empty():
    print(resultQueue.get())

elapsed = time.time() - started
print("Time Elapsed: {:.2f}s".format(elapsed))