class Graph:
    def __init__( self, size ):

        self.adjMatrix  =   []
        #Initializing the adjacency matrix in Python
        for i in  range (  1, size  + 1 ):
                self.adjMatrix.append( [0] * size )

        #Stroing the size for futhter reference
        self.size       =   size

    def addEdges ( self , v1, v2 ):
        if ( v1 == v2 ):
            print ( "Vertex is same", v1, v2 )
            return
        self.adjMatrix[v1][v2]  =   1
        self.adjMatrix[v2][v1]  =   1


    def removeEdges ( self, v1, v2):
        if ( v1==v2 ):
            print ("Vertex is same, edges can't be removed")
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def printMatrix ( self) :

        for row in self.adjMatrix:
            for val in row:
                print (val, end=' ')
            print ('\n')


def main ():

    g = Graph(4)
    g.addEdges(0,1)
    g.addEdges(0,2)
    g.addEdges(1,2)
    g.addEdges(2,0)
    g.addEdges(2,3)

    g.printMatrix()

if __name__ == "__main__":

    main()
