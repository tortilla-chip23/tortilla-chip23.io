import random
import operator
import matplotlib.pyplot
import agentframework

def distance_between(agents_row_a, agents_row_b):
     return (((agents_row_a.x - agents_row_b.x)**2) + 
     ((agents_row_a.y - agents_row_b.y)**2))**0.5

num_of_agents = 100
num_of_iterations = 10
neighbourhood = 20

 # Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment)) 

 # Move the agents, adjust looping
for j in range(num_of_iterations):
     for i in range(num_of_agents):
         agents[i].move()
         agents[i].eat()
         agents[i].share_with_neighbours(neighbourhood) 
  
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
for i in range(num_of_agents):
     matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
matplotlib.pyplot.show()

for agents_row_a in agents:
     for agents_row_b in agents:
         distance = distance_between(agents_row_a, agents_row_b) 

for j in range(num_of_iterations):
     for i in range(num_of_agents):
         agents[i].move()
         agents[i].eat()         
         
#Import in data from csv
import csv 
with open ('D:\in.txt')as file:
    filecontent=csv.reader(file)
    for row in filecontent: 
        print(row)

#show data from csv file
value = row
environment = []
rowlist = [] 
rowlist.append(value)
environment.append(rowlist)

#display with matplotlib
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
     matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()
	
    
    