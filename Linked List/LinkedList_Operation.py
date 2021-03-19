class Node:
  def __init__( self, data ):
    self.data = data
    self.next = None

 

class LinkedList :
  def __init__( self ):
    self.head = None

  def appendToLast ( self, data ):

    if ( not self.head ):
      self.head = Node( data ) 
    else:
      
      tempIter  = self.head
      while ( tempIter.next != None ):
        tempIter  = tempIter.next

      tempIter.next = Node( data )


  def addInTheFront ( self, data ):

    if ( not self.head ):
      self.head = Node ( data )
    else:
      newNode = Node( data )
      newNode.next  = self.head
      self.head = newNode        

  def insertAfter( self, after, data ):
    
    newNode   = Node ( data )
    tempIter  = self.head
    
    while ( tempIter.data != after ):
      tempIter  = tempIter.next

    newNode.next  = tempIter.next
    tempIter.next = newNode


  def deleteNode ( self, data ):

    if ( not self.head ):
      return 

    if ( self.head.data == data):
      self.head = self.head.next
      return

    tempIter  = self.head

    while ( tempIter.next.data != data ):
      tempIter  = tempIter.next
    
    tempIter.next = tempIter.next.next



  def printLinkedList ( self ):

    tempIter  = self.head

    while ( tempIter != None ):
      print ( "{} -->".format( tempIter.data ), end=" " )
      tempIter  = tempIter.next
    print( "None" )



if __name__ == "__main__":

  ll       = LinkedList ( )

  ll.addInTheFront(60)
  ll.appendToLast(56)
  ll.appendToLast(90)
  ll.appendToLast(23)
  ll.insertAfter(56, 78)
  ll.deleteNode(  )

  ll.printLinkedList()
  
