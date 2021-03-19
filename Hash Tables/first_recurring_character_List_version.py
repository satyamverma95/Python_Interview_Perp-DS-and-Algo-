
#Given an array = [2,5,1,2,3,5,1,2,4]:
#It should return 2

#Given an array = [2,1,1,2,3,5,1,2,4]:
#It should return 1

#Given an array = [2,3,4,5]:
#It should return undefined


def getFirstRecurringChar ( arr ):

  char_register = list ()

  for number in arr :
  
    if number in char_register:
      print ( number )
      return
    else:
      char_register.append( number )  

  print ( "All Numbers are distinct" )


if __name__ == "__main__":

  array = [2,5,3,4,5]

  getFirstRecurringChar ( array ) 
