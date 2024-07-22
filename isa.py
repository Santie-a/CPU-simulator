from cache import Cache
from register import Register
from alu import ALU

class ISA:
    def __init__(self, cpu):
        self.cpu = cpu
        self.alu = ALU()
        self.memory = Cache()
        self.registers = Register()
        self.instructions = {
            "ADD": self.add,
            "SUB": self.sub,
            "MULT": self.mult,
            "DIV": self.div,
            "MOV": self.mov,
            "LODM": self.load_from_memory,
            "LODR": self.load_to_register,
            "STORE": self.store,
        }

    def execute(self, instruction):
        opcode = instruction[0]
        operands = [int(i) if i.isdigit() else i for i in instruction[1].split(" ")]
        if opcode in self.instructions:
            self.instructions[opcode](operands)
        else:
            raise Exception(f"Unknown instruction: {opcode}")

    def add(self, operands):
        reg_dest, reg_src1, reg_src2 = operands
        self.registers.data[reg_dest] = self.alu.add(
            self.registers.data[reg_src1], self.registers.data[reg_src2]
        )

    def sub(self, operands):
        reg_dest, reg_src1, reg_src2 = operands
        self.registers.data[reg_dest] = self.alu.subtract(
            self.registers.data[reg_src1], self.registers.data[reg_src2]
        )

    def mult(self, operands):
        reg_dest, reg_src1, reg_src2 = operands
        self.registers.data[reg_dest] = self.alu.multiply(
            self.registers.data[reg_src1], self.registers.data[reg_src2]
        )

    def div(self, operands):
        reg_dest, reg_src1, reg_src2 = operands
        self.registers.data[reg_dest] = self.alu.divide(
            self.registers.data[reg_src1], self.registers.data[reg_src2]
        )

    def mov(self, operands):
        reg_dest, reg_src = operands
        self.registers.data[reg_dest] = self.registers.data[reg_src]

    def load_from_memory(self, operands):
        reg_dest, address = operands
        self.registers.data[reg_dest] = self.memory.read(address)
        print(self.registers.data[reg_dest])

    def load_to_register(self, operands):
        reg_dest, data = operands
        self.registers.write(reg_dest, data)
        print(self.registers.data[reg_dest])

    def store(self, operands):
        address, reg_src = operands
        self.memory.write(address, self.registers.data[reg_src])

    def get_exec_time(self):
        exec_time = self.registers.get_exec_time()
        if self.memory is not None:
            exec_time += self.memory.get_exec_time()
    
        return exec_time