#Name: Jose Melquiades Escobar

#draw patter with nested loops
def main ():
    #call func to display the pattern
    drawPattern()




#define the function to draw the pattern
def drawPattern():
    for outerLoop in range (8, 0, -1):   #total of 7 iteration 
        for innerLoop in range(outerLoop - 1): #start at 8, subtract 1 for every iteration
            print ('@', end = '')     #display each @ symbol with nothing between this loop's iterations
        print ()                      #seperate each outer look, starting a new line 

      
main()
