a=int(input('enter number'))

for i in range(a):
    for j in range(a):
        if j>i:
         print("*",end=" ")
        else:
            print(" ",end="")
    print("")

    '''

  * * * * * *
   * * * * *
    * * * *
     * * *
      * * 
       *
    
    '''