# Search Algorithms Menu
import random

# Adjacency List for graph
graph = {
    "(0,0)" : ["(0,1)","(1,0)"],
    "(0,1)" : ["(0,0)","(0,2)"],
    "(0,2)" : ["(0,1)","(1,2)"],
    "(1,0)" : ["(0,0)","(1,1)","(2,0)"],
    "(1,1)" : ["(1,0)","(1,2)","(2,1)"],
    "(1,2)" : ["(0,2)","(1,1)"],
    "(2,0)" : ["(1,0)"],
    "(2,1)" : ["(1,1)","(2,2)"],
    "(2,2)" : ["(2,1)"]
}

# Random Search
def randomSearch(initialNode,targetNode): 
    x=initialNode
    while True :
        if(x==targetNode):
            print("Success")
            break
        S = graph[x] # expand x and get its neighbours
        x1 = random.choice(S) #  randomly select a child node from S
        x=x1   # move to the randomly selected child node

# Closed List
def closedListSearch(initialNode,targetNode):
    x=initialNode
    closedList=[]
    while True:
        if(x==targetNode):
            print("Success")
            break
        S=graph[x]  # expand x and get its neighbours
        if(S == []): # if S is empty 
            print("Failure!!")
            break # stop search because there are no neighbours
        closedList.append(x) # Append x in closed list
        x1= None  # initially no child node is selected
        for node in S: # for all neighbours
            if node not in closedList: # if node is not in the closed list
                x1 = node  # select this node as the next node
                break # stop checking other neighbours
        if x1 == None:  # if all neighbours are already in closed list
            print("Failure!!")
            break     
        x=x1 # move to the selected child node

# Open List
def openListSearch(initialNode,targetNode):
    openList=[]
    closedList=[]
    openList.append(initialNode) # append initial in open list
    while True:
        if(openList == []): # if open list is empty
            print("Failure")
            break
        x= openList.pop() # take last node from open list

        if(x == targetNode):
            print("Success")
            break
        S=graph[x] # expand x
        closedList.append(x) # append x in closed list
        for x1 in S: # for all neighbours
            if(x1 not in closedList): # if child is not in the closed list 
                openList.append(x1) # add it in the open list

# Uniform Cost
def uniformCostSearch(initialNode, targetNode):

    # adjacency list of graph with cost
    graph = {
        "(0,0)": [("(0,1)", 2), ("(1,0)", 4)],
        "(0,1)": [("(0,0)", 2), ("(1,1)", 3)],
        "(1,0)": [("(0,0)", 4), ("(1,1)", 4), ("(2,0)", 2)],
        "(1,1)": [("(0,1)", 3), ("(1,0)", 4), ("(2,1)", 1)],
        "(2,0)": [("(1,0)", 2), ("(2,1)", 2)],
        "(2,1)": [("(1,1)", 1), ("(2,0)", 2), ("(2,2)", 3)],
        "(2,2)": [("(2,1)", 3)]
    }
    
    openList = []
    closedList = []

    # add initial node with cost 0 and parent none in open list
    openList.append((initialNode, 0, None)) # node,cost,parent

    while True:

        if openList == []:
            print("Failure")
            break

        openList.sort(key=lambda item: item[1]) # sort costs 

        x, cost, parent = openList.pop(0) # pop the lowest cost 

        if x == targetNode:
            print("Success")
            print("Cost:", cost)
            break

        S = graph[x] # expand x 

        closedList.append(x) # append x in closed list

        for node, edgeCost in S: # check all neighbours and get their edgw cost

            if node not in closedList: # if node not in closed list

                newCost = cost + edgeCost # add new cost with previous cost

                found = False

                for i in range(len(openList)): # for evey node in open list

                    if openList[i][0] == node: # check if current node is already in open list

                        found = True

                        if newCost < openList[i][1]: # if new cost is less than the previous cost
                            openList[i] = (node, newCost, x) # update node with lower cost and new parent

                        break

                if found == False: # if node was not found in open list
                    openList.append((node, newCost, x)) # add node with cost and parent
    
print("Search Algorithms Menu")
print("1.Random Search")
print("2.Closed Search")
print("3.Open Search")
print("4.Uniform Cost Search")
choice = int(input("Enter your choice: "))
if(choice==1):
    randomSearch("(0,0)","(2,2)")
elif(choice==2):
    closedListSearch("(0,0)","(2,2)")
elif(choice==3):
    openListSearch("(0,0)","(2,2)")
elif(choice==4):
    uniformCostSearch("(0,0)","(2,0)")
else:
    print("Invalid choice!!")

    
