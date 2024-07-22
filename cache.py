from memory import Memory
from main_memory import MainMemory

class Cache(Memory):
	def __init__(self):
		super().__init__(name="Cache", access_time=0.5)
		self.main_memory = MainMemory()
		self.sets = 2
		self.cache_indices = [0, 2, None, None]
        
		self.data = [
			{"tag": None, "data": ""},
			{"tag": None, "data": ""},
			{"tag": None, "data": ""},
			{"tag": None, "data": ""},
			{"tag": None, "data": ""},
			{"tag": None, "data": ""},
			{"tag": None, "data": ""},
			{"tag": None, "data": ""},
			{"tag": None, "data": ""},
			{"tag": None, "data": ""},
			{"tag": None, "data": ""},
			{"tag": None, "data": ""},
			{"tag": None, "data": ""},
			{"tag": None, "data": ""},
			{"tag": None, "data": ""},
			{"tag": None, "data": ""},
		]

	def write(self, address, data):
		super().write()
		entry = self.get_entry(address)
		if entry is not None:
			entry["data"] = data
		else:
			self.replace_entry(address, data)
    
		self.main_memory.write(address, data)
		print(data)

	def read(self, address):
		super().read()
		data = None
		entry = self.get_entry(address)
		if entry is not None:
			data = entry["data"]
		else:
			data = self.main_memory.read(address)
               
		self.replace_entry(address, data)

		return data

	def replace_entry(self, address, data):
		index = 0
		print(data)
		set_number = address % self.sets
		index = self.cache_policy(set_number)
		self.data[index] = {"tag": address, "data": data}

	def cache_policy(self, set_number):
		self.cache_indices[set_number] += 1
		if self.cache_indices[set_number] == len(self.data)/self.sets+(set_number*int(len(self.data)/self.sets)):
			self.cache_indices[set_number] = set_number*int(len(self.data)/self.sets)

		return self.cache_indices[set_number]

	def get_entry(self, address):
		for entry in self.data:
			if entry["tag"] == address:
				print(f"HIT: ", end="")
				return entry

		print(f"MISS", end="")
		return None