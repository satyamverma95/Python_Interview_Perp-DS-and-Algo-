
class Graph:
  def __init__( self ):
    self.adjacentList   = {}
    self.numberOfNodes  = 0


  def addVertex ( self, vertex ):
    if vertex not in self.adjacentList:
      self.adjacentList[ vertex ] = []

    self.numberOfNodes += 1
    

  def addEdge ( self, node1, node2 ) :
    
    self.adjacentList[ node1 ].append( node2 )
    self.adjacentList[ node2 ].append( node1 )
    

  def showConnections ( self ):
    
    for vertex in self.adjacentList :
      print ( "{} ---> [ {} ]".format( vertex, self.adjacentList[ vertex ] ) )



if __name__ == "__main__":

  g       = Graph ( )

  g.addVertex(0)
  g.addVertex(1)  
  g.addVertex(2)
  g.addVertex(3)
  g.addVertex(4)
  g.addVertex(5)
  g.addVertex(6)
  g.addEdge(3,1)
  g.addEdge(3,4)
  g.addEdge(4,2)
  g.addEdge(4,5)
  g.addEdge(1,2)
  g.addEdge(1,0)
  g.addEdge(0,2)
  g.addEdge(6,5)

  g.showConnections()

