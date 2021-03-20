class Node:
  def __init__( self, data ):
    self.data = data
    self.next = None
    self.prev = None

 

class DoublyLinkedList :
  def __init__( self ):
    self.head = None

  def appendToLast ( self, data ):

    newNode = Node ( data )

    if ( not self.head ):
      self.head = newNode 
    else:
      
      tempIter  = self.head
      while ( tempIter.next != None ):
        tempIter  = tempIter.next

      tempIter.next = newNode
      newNode.prev  = tempIter



  def addInTheFront ( self, data ):

    if ( not self.head ):
      self.head = Node ( data )
    else:
      newNode         = Node( data )
      newNode.next    = self.head
      self.head.prev  = newNode
      self.head       = newNode       

  def insertAfter( self, after, data ):
    
    newNode   = Node ( data )
    tempIter  = self.head
    
    while ( tempIter.data != after ):
      tempIter  = tempIter.next

    tempIter.next.prev  = newNode
    newNode.next  = tempIter.next
    newNode.prev  = tempIter
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
    
    tempIter.next             = tempIter.next.next
    tempIter.next.next.prev   = tempIter 


  def printLinkedList ( self, reverse=False):

    tempIter  = self.head

    if (reverse):
      while ( tempIter.next != None ):
        tempIter  = tempIter.next

      print( "None <==>", end = " ")

      while ( tempIter != None ):
        print ( "{} <==>".format( tempIter.data ), end=" " )
        tempIter  = tempIter.prev    
      print ("HEAD", end = " " )

    else  : 
      print ("HEAD <==>", end = " " )
      while ( tempIter != None ):
        print ( "{} <==>".format( tempIter.data ), end=" " )
        tempIter  = tempIter.next
      print( "None" )

    



if __name__ == "__main__":

  dll       = DoublyLinkedList ( )

  dll.addInTheFront(60)
  dll.appendToLast(56)
  dll.appendToLast(90)
  dll.appendToLast(23)
  dll.insertAfter(56, 78)
  #ll.deleteNode(  )

  dll.printLinkedList( reverse=False)
  
