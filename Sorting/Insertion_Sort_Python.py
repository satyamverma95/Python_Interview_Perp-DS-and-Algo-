def insertionSort ( array ):

  for index_1 in range(1, len(array)):
  
    key = array[index_1]
    tmepIndex = index_1 - 1

    while ( tmepIndex >= 0 and array[tmepIndex] > key ):
      array[tmepIndex+1] = array[tmepIndex]
      tmepIndex -= 1
    
    array[tmepIndex+1] = key
    

  print ( "Sorted Array : ", array )
      

if __name__ == "__main__":

  numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0, -9]

  insertionSort ( numbers )
