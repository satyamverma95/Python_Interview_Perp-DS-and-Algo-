
class Node:
  def __init__( self, data ):
    self.data = data
    self.left = None
    self.right= None


  def insert ( self, data ):

    if ( self.data ):
        if ( self.data > data):
          if ( self.left == None ):
            self.left  = Node ( data )
          else:
            self.left.insert ( data )
        elif ( self.data < data ):
          if ( self.right == None):
            self.right = Node( data )
          else:
            self.right.insert( data )
    else:
      self.data = data

  def lookup ( self, data) :

    if ( self.data == data ):
      print ( "Node Found")
  
    elif ( self.data > data ):
  
      if( self.left ):
        self.left.lookup ( data )
      else:
        print( "Node does not exists." )
  
    else:
  
      if ( self.right ):
        self.right.lookup ( data )
      else:
        print( "Node does not exists." )


  def printTree ( self ):

    if ( self.left ):
      self.left.printTree()
    print( self.data )
    if( self.right ):
      self.right.printTree()



if __name__ == "__main__":

  b       = Node ( 70 )

  b.insert(50)
  b.insert(30)  
  b.insert(10)
  b.insert(60)
  b.insert(20)

  b.printTree()

  b.lookup( 20 )

