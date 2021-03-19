
class HashTable :
  def __init__ ( self, size ):
    self.array  = [ None ] * size
    


  def _hash ( self, key ): #private Property of class
    hash = 0
    for index in range ( len ( key ) ):
      hash = ( hash + ord( key[index] ) * index ) % len( self.array )

    return hash

  def set ( self, key, value ):

    address = self._hash( key )

    if ( not self.array[ address ] ):
      self.array[ address ] = []
  
    self.array[address].append(  [ key, value ] )

  def get ( self, key ):

    address = self._hash( key )
    currentBucket = self.array[ address ]
    if ( currentBucket ):
      for item in (currentBucket ):
        if ( item [ 0 ] == key ):
          print ( item [ -1 ])
          return 

    print ("No such key exists")


  def keys ( self ):

    keyArray  = list()

    for data in self.array:

      if (  data != None ):
  
        for sub_data in data:
          keyArray.append( sub_data[0] )

    print ( keyArray )


  def values ( self ):

    valueArray  = list()

    for data in self.array:

      if (  data != None ):
  
        for sub_data in data:
          valueArray.append( sub_data[-1] )

    print ( valueArray )


  def printMemeory ( self ):

    print ( self.array )

if __name__ == "__main__":
  
  hashObject  = HashTable(2)
  hashObject.set( 'grapes', '23')
  hashObject.set( 'apples', '45')
  hashObject.get( 'apples' )
  hashObject.keys()
  hashObject.values()

  #hashObject.printMemeory()
