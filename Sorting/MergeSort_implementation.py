import math

def mergeSort ( array ):

  if ( len ( array) == 1):
    return ( array )

  lenght  = len(array)
  middle  = math.floor ( lenght / 2) 
  leftArray   = array [:middle]
  rightArray  = array [middle:]

  #print ( "Left Array", leftArray )
  #print ( "Right Array", rightArray ) 

  return ( megre( mergeSort(leftArray), mergeSort(rightArray) ) )


def megre ( leftArray, rightArray ):

  sortedArray = []
  leftIndex   = 0
  rightIndex  = 0

  #print ( "Sorting Array", leftArray, rightArray )

  while ( leftIndex < len(leftArray) and rightIndex < len(rightArray) ):
    if ( leftArray[leftIndex] < rightArray[rightIndex]):
      sortedArray.append(leftArray[leftIndex])
      leftIndex +=1
    else:
      sortedArray.append(rightArray[rightIndex])
      rightIndex +=1

  #print ( "Returning Sorted Array: {}, L:{}, R:{}".format( sortedArray,  leftArray[leftIndex:], rightArray[rightIndex:] ) )
  
  
  return ( sortedArray + leftArray[leftIndex:] + rightArray[rightIndex:])


if __name__ == "__main__":

  numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

  n = len ( numbers )

  sortedArray = mergeSort ( numbers )

  print( "Sorted Array : ", sortedArray )
