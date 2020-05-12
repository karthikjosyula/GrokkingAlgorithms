#Hash table to store the friends of 1st connection friends and friends of second connection friends and so on...
friendshash = {}
friendshash['karthik'] = ['nani','shravan','rafi','phani']
friendshash['nani'] = ['kishore','kranthi','jaideep','joe','videesh']
friendshash['shravan'] = []
friendshash['rafi'] = ['kishore','ravi']
friendshash['phani'] = ['hari']
friendshash['kishore'] = ['tittu']
friendshash['kranthi'] = []
friendshash['jaideep'] = []
friendshash['joe'] = []
friendshash['videesh'] = []
friendshash['tittu'] = []
friendshash['ravi'] = []
friendshash['hari'] = []

#load the names of frinends into a queue. import deque, append the hashtable keys of a given value to queue
from collections import deque
search_queue = deque()
search_queue += friendshash['karthik']

#creating an array with names who own a bike
bikeowners = ['tittu','hari']
searched = []
#breadth first search
while search_queue:
    friend = search_queue.popleft()
    if friend in bikeowners and not friend in searched:
        print(friend + " is the closest bike owner")
        break
    else:
        search_queue += friendshash[friend]
        searched.append(friend)
