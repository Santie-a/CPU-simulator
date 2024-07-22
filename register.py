from memory import Memory

class Register(Memory):
    def __init__(self):
        super().__init__(name="Register", access_time=0.1)
        self.data = {
            0: None, 1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None
        }
        
    def read(self, address):
        super().read()
        return self.data[address]
    
    def write(self, address, data):
        super().write()
        self.data[address] = data 

    def get_execution_time(self):
        return self.execution_time