def selectionSort ( array ):

  for index_1 in range(len(array)):
    for index_2 in range(index_1, len(array)):
      smallest_index = index_1
      if ( array [index_2] < array[smallest_index] ): 
        smallest_index = index_2
      
      (array[index_1], array[smallest_index] )  =  ( array[smallest_index], array[index_1])

  print ( "Sorted Array : ", array )
      

if __name__ == "__main__":

  numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0, -9]

  selectionSort ( numbers )
