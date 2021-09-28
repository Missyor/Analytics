
#### Finding Averages

## Mean     

import statistics

myList = [1, 4, 4, 7, 9]
mean = statistics.mean(myList)
print(mean)

##Median
median = statistics.median(myList)
print(median)

##Mode
mode = statistics.mode(myList)
print(mode)

####Plotting Graphs
import matplotlib.pyplot as ply
ply.plot(myList)
#ply.show()

### Adding Labels
ply.title("Numbers")
ply.xlabel("List index")
ply.ylabel("Numbers")
ply.show()

