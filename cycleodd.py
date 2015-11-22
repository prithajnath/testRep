#Prithaj Nath
#CSC321A Project #1 Odd Cycle Detector 
#Fall 2016


import copy
import sys


#QUEUE keeps track of which vertex to visit next (for BFS)

class Queue:

     def __init__(self):

          self.items = []

     def is_empty(self):

          return self.items == []

     def enqueue(self,item):

          self.items.insert(0,item)

     def dequeue(self):

          return self.items.pop()

     def size(self):

          return len(self.items)


#GRAPH (adjacency list)

class Vertex:

     def __init__(self,key):

          self.id = key
          self.connectedTo={} #dictionary which contains all the other vertices it is connected to
          self.pred = [] #for BFS tree / a list because we are dealing with cycles
          self.color = "white" #for BFS tree
          self.bp_color = "null"


     def addNeighbor(self,nbr,weight=0):

          self.connectedTo[nbr] = weight #nbr is another Vertex object 

     def __str__(self):

          
          return str(self.id) 

     def getConnections(self):

          return self.connectedTo.keys()

     def getId(self):

          return self.id

     def getWeight(self,nbr):

          return self.connectedTo[nbr]

     def getColor(self):

          return self.color
     
     def setColor(self,color):

          self.color = color

     def setPred(self,node):

          self.pred.append(node)

     def getPred(self):

          return self.pred

     def change_color(self,a):

          self.bp_color = a


     def get_bp_color(self):

          return self.bp_color


class Graph:

     def __init__(self):

          self.vertList = {}  #this is the masterlist
          self.numVertices = 0
          self.bipartite = True

     def addVertex(self,key): #turn something into a Vertex object

          self.numVertices = self.numVertices + 1

          newVertex = Vertex(key)

          self.vertList[key] = newVertex #maps vertex names to vertex objects

          return newVertex

     def getVertex(self,n):

          if n in self.vertList:

               return self.vertList[n] #returns the Vertex object
          else:

               return None

     def __contains__(self,n):#tweak the built-in operator 'in'(containment check)

          return n in self.vertList #lets you iterate through the Vertex objects in Graph

     def addEdge(self,f,t,cost = 0):

          if f not in self.vertList: #if f is not a node in the graph

               nv = self.addVertex(f)

          if t not in self.vertList:     #if t is not a node in the graph

               nv = self.addVertex(t)

          self.vertList[f].addNeighbor(self.vertList[t], cost)

     def getVertices(self):

          return self.vertList.keys()

     def __iter__(self): # iterate over Vertex objects over the Graph

          return iter(self.vertList.values())

     def change_bp_ness(self,val):

          self.bipartite = val

     def is_bipartite(self):

          return self.bipartite


#to color nodes
def bp_color(node):

     if node.get_bp_color() == "null" and node.getPred() == []: #root node

          node.change_color("blue")
          
     elif node.get_bp_color() == "null":

          for i in node.getPred():

               if i.get_bp_color() == "blue":

                    node.change_color("red")
                    
               elif i.get_bp_color() == "red":

                    node.change_color("blue")
               break
          

def bfs_tree(graph,s_node): #BFS tree builder

 
     q = Queue()
     q.enqueue(s_node)
     tree = []
     tree.append(str(s_node))

 

     while(q.size() > 0):

          current_vertex = q.dequeue()

          
          for nbr in current_vertex.getConnections(): #loop through the neighbors(Vertex objects) of current_vertex
               

               
               if (nbr.getColor() == "white"):
                    
                    nbr.setColor("gray")
                    nbr.setPred(current_vertex)
                    q.enqueue(nbr)
                    tree.append(str(nbr))
                  
               elif (nbr.getColor() == "gray"): #if there is a half-explored node
                    
                    
                     nbr.setPred(current_vertex)
                                 
          current_vertex.setColor("black")
          
     return tree


def is_tree(graph):

     tree = True

     for g in graph:

          if len(g.getPred()) > 1:

               tree = False

               break
     return tree
          

             
def traverse_color(graph,tree):

     for i in tree:

          bp_color(graph.getVertex(int(i)))

                   

def main():

     
     g = Graph()

     afile = open('filename','r')

     len_file = 0

     num_nodes = 0

     node_list = []

     for i in afile:


          if len_file == 0:

               num_nodes = int(i)
               
          elif len_file > 1:
               

               mystring = i.split(" ")
               node_list.append(mystring)
               


          len_file = len_file + 1

     

     for k in range(len_file - 2):

          node_list[k][2] = node_list[k][2].rstrip("\n")
          

     for i in range(1,num_nodes+1):

          g.addVertex(i)
       
     
     for j in range(len(node_list)):

          #edges had to be added both ways so each node is listed in the adjacency list of the other
          g.addEdge(int(node_list[j][1]),int(node_list[j][2]))
          g.addEdge(int(node_list[j][2]),int(node_list[j][1]))



     tree = bfs_tree(g,g.getVertex(1))

     if is_tree(g): #checking if the graph is a tree

          print("TREE")
          sys.exit()

     #two coloring the graph
     traverse_color(g,tree)


     #putting red and blue edges in separate lists so that we can check if there are any edges between them
     
     R = []

     B = []

     for l in g:

          if l.get_bp_color() == "blue":

               B.append(l)
          else:
               R.append(l)

     
     odd_cycle_tree = []
     
     for n in B:

          for p in n.getConnections():

               if p in B:

                    g.change_bp_ness(False)
                    odd_cycle_tree.append(p)
                    odd_cycle_tree.append(n)
                    
     

     for r in R:

          for q in r.getConnections():

               if q in R:
                    g.change_bp_ness(False)
                    odd_cycle_tree.append(q)
                    odd_cycle_tree.append(r)

     a_list = copy.copy(odd_cycle_tree)
     

     #adding edges in the same level of the BFS tree to a list 
     if len(a_list) > 2:

          b_list = []

          k = 0

          j = len(a_list) - 2

          for l in range(len(a_list)//2):
               

               b_list.append(a_list[k:-j])

               if j!= 2:

                    j = j - 2
               else:
                    k = k + 2
                    b_list.append(a_list[k:])
                    break
          k = k + 2

     else:
 
          b_list = [a_list]




     #printing odd cycles

     while len(b_list) > 0:
          

          mystring = ""

          temp_edge = b_list.pop()

          x = temp_edge[0]

          y = temp_edge[1]


          while True:
               

               mystring = mystring + str(x) + str(y)

               if [val for val in x.getPred() if val in y.getPred()] != []: #if they have a common predecessor  

                    if [val for val in x.getPred() if val in y.getPred()][0].getPred() == []: # it's the root node

                         print(mystring + str([val for val in x.getPred() if val in y.getPred()][0]))
                    
                         break
                    else:

                         print(mystring + str([val for val in x.getPred() if val in y.getPred()][0]))

               x = x.getPred()[0]

               y = y.getPred()[0]

     

main()

               

               

     
          

     

     
          
          

