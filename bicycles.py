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