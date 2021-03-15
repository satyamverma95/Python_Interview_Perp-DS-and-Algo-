import timeit


def findNemo2 ( array ):
  for elem in array:
    if elem == "Nemo":
      print ( "Found Nemo!")


def findNBoxes ( array ):
  elem_1  = array [0]
  elem_2  = array [1]

  print ( "Found Elem 1 : {}, Elem 2 : {}".format(elem_1, elem_2))


#This signifies the start of the program
if __name__ == "__main__":

  array_small   = ['Nemo']
  array_medium  = ['Nemo'] * 20
  array_large   = ['Nemo']* 10000
  
  start =  timeit.default_timer()
  
  findNemo2( array_medium ) #O(n)--> Linear Time. Based on length of array. 

  end   = timeit.default_timer()

  print ( "Run Time : (ms)  ", (end - start) ) 


  #Checking time for O(1) operations

  start =  timeit.default_timer()
  
  findNBoxes( array_large ) #O(n)--> Linear Time. Based on length of array. 

  end   = timeit.default_timer()

  print ( "Run Time : (ms)  ", (end - start) ) 
