from memory import Memory

class MainMemory(Memory):
	def __init__(self):
		Memory.__init__(self, name="Main Memory", access_time=30)
		self.data = [""] * 16
            
	def read(self, address):
		data = self.data[address]
		super().read()
		return data
	
	def write(self, address, data):
		self.data[address] = data
		super().write()

	def get_exec_time(self):
		return self.exec_time