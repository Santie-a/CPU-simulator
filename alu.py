class ALU:
	def __init__(self):
		pass

	def add(self, n1, n2):
		return n1 + n2

	def subtract(self, n1, n2):
		return n1 - n2
	
	def multiply(self, n1, n2):
		return n1 * n2

	def divide(self, n1, n2):
		calculated_value = 0
		if n2 != 0:
			calculated_value = int(n1 / n2)
		else:
			print(f"Division by 0 error: {n1}/{n2}")
		return calculated_value