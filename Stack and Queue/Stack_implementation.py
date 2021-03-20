class Stack:
  def __init__ ( self ):
    self.top    = None
    self.bottom = None
    self.array  = list()

  def append ( self, data ):

    if ( len( self.array ) == 0 ):
      self.bottom = data

    self.array.append( data )
    self.top    = data

  def pop ( self ):

    if ( len ( self.array ) == 0 ):
      self.bottom = None
      print ( "Stack Empty" )
      return 

    print ( "Element Popped : {}".format( self.array.pop()) )
    self.top    = self.array [-1]

  def peep ( self ):

    if ( len ( self.array ) == 0 ):
      print ( "Stack Empty" )
      return 

    print ( "Top Element : {}".format(self.array [-1] ) )

  def printStack ( self ):
    
    index = len ( self.array ) - 1

    while ( index >= 0 ):
      print ( "| {} |".format(self.array [ index ]) )
      print ( "-------" )
      index -= 1

  def stackSize ( self ):

    print ( "Stack Size : ", len( self.array ) )


if __name__ == "__main__":

  stack = Stack()

  stack.append(1)
  stack.append(2)
  stack.append(3)
  stack.append(4)
  stack.append(5)
  stack.append(6)
  stack.append(7)
  stack.append(8)
  stack.append(9)
  stack.append(10)

  
  stack.peep()
  stack.pop()
  stack.stackSize()
  #stack.printStack()
