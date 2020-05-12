'''
Like Breadth-First search, Dijkstra's algorithm works on graphs.
But the difference is BFS algorithm works on unweighted graphs and Dijkstra's algorithm works on non-negative weighted graphs.
Dijkstra's algorithm only works with Directed Acyclic Graphs - DAGs
DAG : a graph which has one direction and is not cyclic - 2 nodes parent to each other or a node parent to itself
The 4 steps of Dijkstra's algorithm :
1. Find the cheapest node. This node is the node with least weight.
2. check whether there's cheapest path to the neighbors of that node.
3. Repeat untill we have done this for every node.
4. Calculate the final path.

Requirements to implement Dijkstra's algorithm:
1. Hash table to store the nodes and the immediate neighbors and costs, to begin with.
2. 2nd hash table to store the nodes and costs. Future nodes will have costs = infinity : batman = float("inf")
3. 3rd hash table to store the parents. Donot update the unseen nodes with parents. Leave them blank

Lets work on an example:
My starting point is NY and destination is Chicago
NY to Buffalo in 4 hours
NY to Pittsburgh in 9 hours
Buffalo to Detroit in 5 hours
Buffalo to Pittsburgh in 3 hours
Buffalo to Cleveland in 3 hours
Pittsburgh to Cleveland in 2 hours
Pittsburgh to Indianapolis in 6 hours
Indianapolis to Chicago in 3 hours
Cleveland to Toledo in 2 hours
Toledo to Chicago in 4 hours
Detroit to Chicago in 5 hours

If BFS is implemented it would have looked for least nodes to traverse and would have picked
NY - Pittsburgh - Indianapolis - Chicago
9 + 6 + 3  = 18 hours
OR
NY - Buffalo - Detroit - Chicago
4 + 5 + 5 = 14 hours
Totally ignoring the time required to travel as BFS is unweighted algorithm

What does Dijkstra's algorithm does?
This looks at all the possible edges to immediate nodes and picks the least weighted edge or edges to reach that node.
'''
#First hash table to store immediate nodes and weights
tripmap = {}
tripmap["NY"] = {}
tripmap["NY"]["Buffalo"] = 4
tripmap["NY"]["Pittsburgh"] = 9
tripmap["Buffalo"] = {}
tripmap["Buffalo"]["Pittsburgh"] = 3
tripmap["Buffalo"]["Detroit"] = 5
tripmap["Buffalo"]["Cleveland"] = 2
tripmap["Pittsburgh"] = {}
tripmap["Pittsburgh"]["Cleveland"] = 2
tripmap["Pittsburgh"]["Indianapolis"] = 6
tripmap["Indianapolis"] = {}
tripmap["Indianapolis"]["Chicago"] = 3
tripmap["Cleveland"] = {}
tripmap["Cleveland"]["Toledo"] = 2
tripmap["Toledo"]={}
tripmap["Toledo"]["Chicago"] = 4
tripmap["Detroit"]={}
tripmap["Detroit"]["Chicago"] = 5
tripmap["Chicago"] = {} #The final node doesnot have any neighbors

# second hash table for hours. All future hours will be infinity
batman = float("inf")
hours = {}
hours["Buffalo"] = 4
hours["Pittsburgh"] = 9
hours["Detroit"] = batman
hours["Cleveland"] = batman
hours["Indianapolis"] = batman
hours["Toledo"] = batman
hours["Chicago"] = batman

# third hashtable for parents ; i name this as prevstop
prevstop = {}
prevstop["Buffalo"] = "NY"
prevstop["Pittsburgh"] = "NY"
prevstop["Detroit"] = None
prevstop["Cleveland"] = None
prevstop["Indianapolis"] = None
prevstop["Toledo"] = None
prevstop["Chicago"] = None

#Processed node should not be visited again
pitstop = []
#Implementing Dijkstra's algo

def find_least_hours_to_city(hours):
    least_hour = float("inf")
    least_hour_to_city = None
    for city in hours:
        hours_num = hours[city]
        if hours_num < least_hour and city not in pitstop:
            least_hour = hours_num
            least_hour_to_city = city
    return least_hour_to_city

city = find_least_hours_to_city(hours)
while city is not None:
    hours_num = hours[city]
    nextstops = tripmap[city]
    for i in nextstops.keys():
        new_hours = hours_num + nextstops[i]
        if hours[i] > new_hours:
            hours[i] = new_hours
            prevstop[i] = city
    pitstop.append(city)
    city = find_least_hours_to_city(hours)
print(hours)
