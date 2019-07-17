#Why we need double queue?
#Because operations like print are heavy to do and when they are accessed by seprate threads, it may go downhill
#faster than lance armstrong's foundation. So if you believe in good karma don't use print function in that
#Use a queue and when done print the results

# pip3 install gmaps - This package is needed for this what I am going to do next.

from queue import Queue
from threading import Thread

from gmaps import Geocoding

api = Geocoding()

locs = {'Delhi','Kolkata','Gujrat','New York','Dubai','Seoul',''}

THREAD_