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

while x > 0 and len(amount)!=0 and x > min(amount):
    amount_used = []
    soldcompany = []

    index = []
    max_rate = max(parent_rate)
    ind_max_rate = [i for i, j in enumerate(parent_rate) if j == max_rate] #Retrieves corresponding index of the maximum price

    for i in ind_max_rate:
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
