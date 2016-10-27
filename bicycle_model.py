import random

class Bicycle(object): 
	"""Models bicycles"""
	def __init__(self, model, weight, cost): 
		self.model=model
		self.weight=weight
		self.cost=cost
	
class BikeShop(object):
    """Models Bike Shops"""
    def __init__(self, name, inventory, markup, bikesSold, profit):
        self.name=name
        self.inventory=inventory
        self.markup=markup
        self.bikesSold=bikesSold
        self.profit=profit
		
    def sellBike(self, model, cost):
        if model in self.inventory: 
            self.bikesSold += 1
            self.profit+=(cost*(self.markup+1) - cost)
            self.inventory[model] -= 1
        else: 
            print("Sorry, we do not have that bike")
			
    def printInventory(self):
        print("Our current inventory is as follows:")	
        for key in self.inventory: 
            print("{} : {} bikes".format(key.model, self.inventory[key]))
			
    def numBikesSold(self):
        print("We have sold {} bikes".format(self.bikesSold))
		
    def profitEarned(self):
        print("We have earned {} in profit.".format(self.profit))
			
class Customer(object):
    """Makes customers"""
    def __init__(self, name, budget): 
        self.name=name
        self.budget=budget
		
    def buyBike(self, model):
        print("I would like to buy a {}".format(model))

		
if __name__ == '__main__':		
    modelA = Bicycle("modelA", "25lbs", 1000)
    modelB = Bicycle("modelB", "35lbs", 450)
    modelC = Bicycle("modelC", "45lbs", 300)
    modelD = Bicycle("modelD", "15lbs", 950)
    modelE = Bicycle("modelE", "55lbs", 200)
    modelF = Bicycle("modelF", "60lbs", 100)
    
    BikesRUs = BikeShop("BikesRUs", {modelA: 5, modelB:10, modelC: 7, modelD:8, modelE: 20, modelF: 25}, .20, 0, 0)
    
    customer1 = Customer('Anne', 200)
    customer2 = Customer('Becky', 500)
    customer3 = Customer('Sarah', 1000)
    customers=[customer1, customer2, customer3]
    
    for customer in customers: 
    	customer.inBudgetBikeModels=[]
    	customer.inBudgetBikes=[]
    	for bike in BikesRUs.inventory: 
    		if (bike.cost*(1+BikesRUs.markup)) <= customer.budget:
    			customer.inBudgetBikeModels.append(bike.model)
    			customer.inBudgetBikes.append(bike)
    	print(customer.name + ", these bikes are in your budget: {}".format(', '.join(customer.inBudgetBikeModels)))
    
    BikesRUs.printInventory()	
    	
    for customer in customers: 
    	requestedBike=random.choice(customer.inBudgetBikes)
    	customer.buyBike(requestedBike.model)
    	BikesRUs.sellBike(requestedBike, requestedBike.cost)
    	print("{} bought a {} for {} and now has {} remaining in his/her bike fund.".format(customer.name, requestedBike.model, (requestedBike.cost*(BikesRUs.markup+1)), (customer.budget - (requestedBike.cost*(BikesRUs.markup+1)))))
    	
    print("{} sold {} bikes for a total profit of {}".format(BikesRUs.name, BikesRUs.bikesSold, BikesRUs.profit))
    
    BikesRUs.printInventory()
    	
    	
    	