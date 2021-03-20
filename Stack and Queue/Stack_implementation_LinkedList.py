class Node:
  def __init__( self, data ):
    self.data = data
    self.next = None

 

class Stack :
  def __init__( self ):
    self.head = None

  def append ( self, data ):

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
      
    tempIter  = self.head
    while ( tempIter.next != None ):
      tempIter  = tempIter.next
 
    print ( "Top Item :{} \n".format( tempIter.data ) )


  def pop ( self ):

    if ( not self.head ):
      print( "Queue is empty.")
      return 

    tempIter  = self.head
    
    while ( tempIter.next != None ):
      prevNode  = tempIter
      tempIter  = tempIter.next
    
    prevNode.next = None 


  def printStack ( self ):

    tempIter  = self.head

    while ( tempIter != None ):
      print ( " {} ".format( tempIter.data ), end = "||" )
      tempIter  = tempIter.next



if __name__ == "__main__":

  s       = Stack ( )

  s.append(60)
  s.append(56)
  s.append(90)
  s.append(23)
  s.append(78)
  s.append(230)
  
  s.peek()

  s.printStack()

  s.pop()

  print ( "\n\nAfter dequeuing.\n\n")
  s.printStack()
