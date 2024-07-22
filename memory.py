class Memory():
	def __init__(self, name="", access_time=0):
		self.name = name
		self.access_time = access_time
		self.execution_time = 0
          
	def read(self, output=True):
		if output:
			print(f" - {self.name} read: ", end="")
		self.execution_time += self.access_time

	def write(self, output=True):
		if output:
			print(f" - {self.name} write: ", end="") 
		self.execution_time += self.access_time

	def get_exec_time(self):
		return 0