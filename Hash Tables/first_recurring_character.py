
#Given an array = [2,5,1,2,3,5,1,2,4]:
#It should return 2

#Given an array = [2,1,1,2,3,5,1,2,4]:
#It should return 1

#Given an array = [2,3,4,5]:
#It should return undefined


def getFirstRecurringChar ( arr ):

  char_register = dict()

  for number in arr :
  
    if number not in char_register :
      char_register [ number ]  = 1
    else:
      char_register [ number ]  +=  1 

    if ( char_register [ number ] > 1 ):
      print ( number )
      return 

  print ( "All Numbers are distinct" )


if __name__ == "__main__":

  array = [2,3,4,5]

  getFirstRecurringChar ( array ) 
