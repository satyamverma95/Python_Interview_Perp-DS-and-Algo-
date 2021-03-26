def bubbleSort ( array ):

  for index_1 in range(len(array)):
    for index_2 in range(0, len(array)-index_1-1):
      if ( array [index_2] > array[index_2 + 1 ]): 
        
        (array[index_2], array[index_2+1] )  =  ( array[index_2+1], array[index_2])

  print ( "Sorted Array : ", array )
      

if __name__ == "__main__":

  numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

  bubbleSort ( numbers )
