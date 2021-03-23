
def reverseString ( string ):

  if ( len ( string ) <=1 ):
    return( string )
  
  return ( reverseString(string [1:]) + string [0] )


if __name__ == "__main__":

  string =  "I love programming"

  string = reverseString( string )

  print ( string )
