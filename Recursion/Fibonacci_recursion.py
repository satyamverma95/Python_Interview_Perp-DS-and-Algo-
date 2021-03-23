
def fibonacci ( number ):

  if ( number <=1 ):
    return( number )
  
  return ( fibonacci ( number - 1 )  + fibonacci ( number -2 ) )


if __name__ == "__main__":

  number = 10

  for num in range ( number):
    print ( fibonacci( num ) )

