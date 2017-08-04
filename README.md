# 170-Project

Problem:  Had a very difficult knapsack problem in this format and where we have to find the most profit:

Created a python script to solve this problem.

[P pounds] <br>
[M dollars] <br>
[N number of items] <br>
[C number of constraints] <br>
[item_name]; [class]; [weight]; [cost]; [resale value] <br>
[item_name]; [class]; [weight]; [cost]; [resale value]  <br>
... <br>
[incompatible_class1, incompatible_class2, incompatible_class3] <br>
[incompatible_class4, incompatible_class5] <br>
... <br>
[end of file] <br>

Solution:
The basis of our algorithm was a greedy one based on a ratio of each item’s resale_value / (cost * weight) ratio. 
This ratio makes sense because you want the greatest proportion of how much you can sell an item for depending on how much you bought it for, while also wanting it to take up as little space as possible. 
To do this, we first iterate through all the items, and calculate it based on each item’s characteristics.   
From here, we begin our greedy algorithm by looking at the first two items with the highest value/weight ratio, unless there is only one left for consideration. 
Between these two items, we will randomly pick one. 
We introduce randomization here because it is an effective strategy to picking local optimas. 
For each item chosen, we check if its already been constrained by a previously bought item; if not, then we buy it, and adjust our bought classes, weight and money left. 
Repeat until there is no more money, weight, or items left.   
One strategy we tried was using the concept of opportunity cost, or the loss in potential gain from possible alternatives. 
To calculate the opportunity cost for each class, we add the value/weight ratio for each item that belongs to that class. 
Then, we will iterate through each constraint and find all the incompatible classes for each class, and add their respective total ratio costs - this combined value for each class is its opportunity cost. 
Essentially what this value represents is: say you pick item i from class c, then you cannot pick any item that belongs to any incompatible class for class i, and thus are losing on their resale opportunity. 
For two items with similar value/weight ratios, we obviously want to pick the item with the lower opportunity cost. 
During the randomization step, randomly pick one based on a proportion of their opportunity cost, with the one with the lower opportunity cost being more likely to be chosen. 
However, implementation of this strategy resulted in a slightly lower score, but it is definitely something we want to explore in the future.   

Runtime Analysis:   
N - number of items C - number of Constraints L – average length of each constraint  
calculating value/weight ratios - O(N) greedily choosing each item, checking constraints for each one - O(CNL) 

Collaborated with Dennis Yang
