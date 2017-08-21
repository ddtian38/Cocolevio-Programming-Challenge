#Daniel Tian
#Cocolevio Programming Challenge

#Assumptions: No negative values. Each company reqeusts a unique amount of the material.

x = 55 #total material given for supply
company = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'] #companies
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
#Algorithm finds the highest rate from the list of companies and calculates the profit after selling material to the company with the highest rate. 
while x > 0 and len(amount)!=0 and x >= min(amount):
    amount_used = []
    soldcompany = []

    #Retrieves corresponding index of the maximum price
    index = []
    max_rate = max(parent_rate)
    ind_max_rate = [i for i, j in enumerate(parent_rate) if j == max_rate]
    
    for i in ind_max_rate:
        if x-amount[i] >= 0:
            a = amount[i]
            p = price[i]
            profit = profit + max_rate*a
            #Subtracts amount sold from supply
            x = x-a
 
            soldcompany.append(company[i])
            amount_used.append(amount[i])
            company_sold_to.append(company[i])
        
    #Removes used highest rate 
    for r in parent_rate:
        if r == max_rate:
            parent_rate.remove(r)


    #Updating lists for next round of finding the next highest rate
    for n in amount_used:
        for m in amount:
            if n==m:
                amount.remove(m)

    for a in soldcompany:
        for b in company:
            if a == b:
                company.remove(b)
#Prints how much profit is made
print('Profit made: $' + str(round(profit,2)))

#Prints how much material is left
print('Remaining: ' + str(x))

#Prints to which company has the material been given to
print('Companies that the material should be sold to: ' + str(company_sold_to))

