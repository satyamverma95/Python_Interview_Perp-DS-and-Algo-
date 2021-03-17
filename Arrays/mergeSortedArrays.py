

#Function to merge two sorted Arrays
def mergeArrays ( array_1, array_2 ):

  mergedArrays = list()
  i=0; j=0  #Setting the pointers to start of the array. 

  #Comparing the two arrays and adding elements based on comparison operator. 
  while ( i < len( array_1) and ( j < len (array_2) ) ):

    if ( array_1[i] < array_2 [j]  ):
      mergedArrays.append( array_1[i] )
      i += 1
    elif ( array_1[i] > array_2 [j] ):
      mergedArrays.append( array_2[j] )
      j +=1
    elif ( array_1[i] == array_2 [j] ):
      mergedArrays.append( array_1[i] )
      mergedArrays.append( array_2[j] )
      i += 1
      j += 1
    
  #When comparison merging is done then we just append the rest of the elements. 

  while ( i < len(array_1) ):
    mergedArrays.append( array_1[i] )
    i += 1

  while ( j < len(array_2) ):
    mergedArrays.append( array_2[j] )
    j += 1

  print ( "Merged Arrays", mergedArrays )


if __name__ == "__main__":

  #HardCoding the two arrays
  array_1 = [ 0, 3, 4, 31, 90 ] 
  array_2 = [ 4, 6, 12, 30,  ]

  mergeArrays( array_1, array_2 )


