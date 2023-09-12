def knapsack(weight,cost,capacity):
    num=len(weight)
    table=[[0]*(capacity+1)for __ in range(num+1)]
    for i in range(1,num+1):
        for j in range(1,capacity+1):
            if weight[i-1]<=j:
                table[i][j]=max(cost[i-1]+table[i-1][j-weight[i-1]],table[i-1][j])
            else:
                table[i][j]=table[i-1][j]
    selected=[]
    total=capacity
    for i in range(num,0,-1):
        if table[i][total]!=table[i-1][total]:
            selected.append(i-1)
            total-=weight[i-1]
    selected.reverse()
    return table[num][capacity],selected

weight=[int(x) for x in input("Enter the weight:").split()]
cost=[int(x) for x in input("Enter the cost:").split()]
capacity=int(input("Enter capacity:"))
totalcost,selecteditem=knapsack(weight,cost,capacity)
print("Total cost:",totalcost)
print("items indes:",selecteditem)
print("weight",[weight[i] for i in selecteditem])
print("cost",[cost[i] for i in selecteditem])
