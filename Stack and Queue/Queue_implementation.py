class Node:
  def __init__( self, data ):
    self.data = data
    self.next = None

 

class Queue :
  def __init__( self ):
    self.head = None

  def enqueue ( self, data ):

    if ( not self.head ):
      self.head = Node( data ) 
    else:
      
      tempIter  = self.head
      while ( tempIter.next != None ):
        tempIter  = tempIter.next

      tempIter.next = Node( data )
      
  def peek ( self ):

    if ( not self.head ):
      print ( "Empty Queue")
      return   
      
    print ( "First Item :{} \n".format(self.head.data ) )


  def dequeue ( self ):

    if ( not self.head ):
      print( "Queue is empty.")
      return 

    self.head = self.head.next


  def printQueue ( self ):

    tempIter  = self.head

    while ( tempIter != None ):
      print ( "{}".format( tempIter.data ), end=" | " )
      tempIter  = tempIter.next



if __name__ == "__main__":

  q       = Queue ( )

  q.enqueue(60)
  q.enqueue(56)
  q.enqueue(90)
  q.enqueue(23)
  q.enqueue(78)
  q.enqueue(230)
  
  q.peek()

  q.printQueue()

  q.dequeue()

  print ( "\n\nAfter dequeuing.\n\n")
  q.printQueue()
