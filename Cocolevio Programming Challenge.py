#Daniel Tian
#Cocolevio Programming Challenge
x = 25 #total material given for supply
amount = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #corresponding quantity of the material that companies request
price = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30] #corresponding price that company is willing to pay

index = range(0,len(amount)) #Creates list of indexes
company_sold_to = [] #declare and initialize empty list to list out what companies should the material to be sold to
profit = 0 #how much profit made

#Creates a list of rate of pay (price per quantity)for each company
parent_rate = []
for i in index:
    n1 = float(price[i])
    n2 = float(amount[i])
    parent_rate.append(round(n1/n2,2))
