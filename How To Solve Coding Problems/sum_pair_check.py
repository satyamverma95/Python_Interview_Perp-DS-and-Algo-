#We have two list and we have to find if there exists a pair whose sum equals the desired sum. 


def checkSumPairNaive( arr_1, arr_2, desired_sum ):
#This is the basic brute force approach. 

  for index, item1 in enumerate( arr_1 ):
    for item2 in  arr_1 [ index + 1 : ] :
      if ( item1 + item2 == desired_sum ):
        print ( "Found" )
        return 

  print ("Not Found")


def checkSumPairOptimised ( arr_1, arr_2, desired_sum ):
  
  num_set = set()

  for index, item in enumerate( arr_1 ):

    if item in num_set:
      print( "Found" )
      return 

    num_set.add( desired_sum - item )
  
  print ("Not Found")





if __name__ == "__main__":

  arr_1 = [ 1, 2, 4, 9 ]
  arr_2 = [ 1, 2, 4, 4 ]

  desired_sum = 8

  checkSumPairNaive( arr_1, arr_2, desired_sum )
  checkSumPairOptimised( arr_1, arr_2, desired_sum )
