**Unique way of adding a member variable in a class**
class BaseClass: 
	def __init__(self, id): 
		self.id = id

base_var = BaseClass(100) 

base_var.__dict__['life'] = 49

print(base_var.life + len(base_var.__dict__)) 
