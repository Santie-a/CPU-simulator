from isa import ISA

class CPU:
	def __init__(self):
		self.isa = ISA(self)
		self.counter = 0
		self.instructions = []

	def show_registers(self):
		for reg in self.isa.registers.data:
			print(f"{reg}: {self.isa.registers.data[reg]}")

	def show_memory(self):
		print("Cache data:")

		for reg in self.isa.memory.data:
			print(reg)

		print("\nMain memory: ")

		for i, reg in enumerate(self.isa.memory.main_memory.data):
			print(f"{i}: {reg}")

	def load_instructions(self, file):
		with open(file, 'r') as instructions_file:
			for line in instructions_file.readlines():
				self.instructions.append(line.removesuffix("\n").split(" ",maxsplit=1))

	def run(self):
		while self.counter < len(self.instructions):
			print(f"Executing instruction {self.instructions[self.counter]}...")
			self.isa.execute(self.instructions[self.counter])
			self.counter += 1
		
		self.counter = 0