import timeit


def findNemo2 ( array ):
  for elem in array:
    if elem == "Nemo":
      print ( "Found Nemo!")



#This signifies the start of the program
if __name__ == "__main__":

  array_small   = ['Nemo']
  array_medium  = ['Nemo'] * 20
  array_large   = ['Nemo']* 10000
  
  start =  timeit.default_timer()
  
  findNemo2( array_large ) #O(n)--> Linear Time. Based on length of array. 

  end   = timeit.default_timer()

  print ( "Run Time : (ms)  ", (end - start) ) 
