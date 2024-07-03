"""
Sets 2 - Operations on sets
* Discard
* Remove
* Clear
* Add
Date : 5.3.2024
"""
import os

os.system('clear')
set1 = {1,2,3,4,5,6,7,8,9,10}
print(set1)
input()
set1.discard(5)    #Removes the element 5 from the set
print(set1)
input()
set1.remove(6)    #Removes the element 6 from the set
print(set1)
"""
Difference between discard and remove -
discard - If the element is not present in the set, it will not raise an error
remove - If the element is not present in the set, it will raise an error
"""
input()
set1.add(11)    #Adds the element 11 to the set
print(set1)
input()
set1.clear()    #Removes all the elements from the set
print(set1)