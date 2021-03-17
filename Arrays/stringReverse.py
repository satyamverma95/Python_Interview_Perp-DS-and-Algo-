#Function to Reverse a string using O(n) time complexity
def reverseString( string ):

  end   = len(string) -1 
  str_rev = ''

  while ( end >=0 ):

    str_rev += string [ end ]
    end -= 1

  print (str_rev)  

#Using the extended slice method to reverse the string
def reverseStringExtendedSlice ( string ):

  print ( string[::-1] )


if __name__ == "__main__":

  #HardCoding Strng as of now
  string  = input("Enter String : ")

  
  reverseString( string )
  reverseStringExtendedSlice ( string )


