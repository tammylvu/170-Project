"""
===============================================================================
  Please complete the following function.
===============================================================================
"""

def solve(P, M, N, C, items, constraints):
    """
    Write your amazing algorithm here.

    Return: a list of strings, corresponding to item names.
    """
    output = []
    weightLeft = P
    moneyLeft = M
    currClasses = set()
    value = 0

    class_cost = [] 
    for i in range(N):
        class_cost.append(0)
    
    # add value/(cost*weight) ratio to each item array if it can be placed into knapsack
    # [item_name]; [class]; [weight]; [cost]; [resale value]
    for i in items:
        if i[2] < weightLeft and i[3] < moneyLeft:
            if i[2] == 0:
                i.append(float('inf'))
            elif i[3] == 0:
                i.append(i[4] / i[2])
            else:
                i.append(i[4] / (i[3] * i[2]))
        else:
            i.append(0)

        class_cost[i[1]] = class_cost[i[1]] + i[5]

    # all classes incompatible with each class
    # tot_incompatible = list of sets, indexed by class
    tot_incompatible = []
    for i in range(N):
        tot_incompatible.append(set())
    # print("length of tot_incompatible: " + str(len(tot_incompatible)))
    # print("N: " + str(N))
    # print("Should be 0: " + str(len(tot_incompatible[0])))

    # iterate through all constraints
    for c in constraints:
        for i in range(N):
            if c.issuperset(set([i])):
                tot_incompatible[i] = tot_incompatible[i].union(c)
    
    # print(len(tot_incompatible[0]))
    # print(tot_incompatible[0])
    # print(tot_incompatible[0].pop())
    # print(len(tot_incompatible[0]))

    for i in range(N):
        tot_incompatible[i].discard(i)
    
    # op_costs = opportunity cost for each class, indexed by class
    op_costs = []
    for i in range(N):
        op_cost = 0
        # print(len(tot_incompatible[i]))
        for j in tot_incompatible[i]:
            op_cost = op_cost + class_cost[j]
        op_costs.append(op_cost)

    sortedList = sorted(items, key = lambda x: x[5], reverse = True)
    print(sortedList[0])

    while (moneyLeft > 0) and (weightLeft > 0) and (len(sortedList) != 0):

        # choose between first 2 largest ratios based on opportunity cost
        if len(sortedList) > 2:
            if (op_costs[sortedList[0][1]] != 0) or (op_costs[sortedList[1][1]] != 0):
                randFloat = np.random.random_sample()
                cutoff = 1 - (op_costs[sortedList[0][1]] / (op_costs[sortedList[0][1]] + op_costs[sortedList[1][1]]))
                if (randFloat <= cutoff):
                    randInd = 0
                else:
                    randInd = 1
            else:
                randInd = np.random.choice([0,1])
            randChoice = sortedList[randInd]
            
        # if only length 1, choose that item
        elif len(sortedList) == 1:
            randInd = 0
            randChoice = sortedList[randInd]
            
        # just in case
        else:
            break

        # insert only if enough weight, money, and not in any constraints
        if (randChoice[2] < weightLeft) and (randChoice[3] < moneyLeft):
            tempClasses = currClasses.union(set([randChoice[1]]))
            isConstrained = False
            if len(tempClasses) > 1:    
                for c in constraints:
                    if len(tempClasses.intersection(c)) > 1:
                        isConstrained = True
                        break
                    
            # if not constrained, add to output
            if not isConstrained:
                output.append(randChoice[0])
                weightLeft -= randChoice[2]
                moneyLeft -= randChoice[3]
                currClasses = tempClasses
                value += randChoice[4]
                
        # delete from list no matter what so that don't repeat calculations on it
        del sortedList[randInd]
    
    return output