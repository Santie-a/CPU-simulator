from cpu import CPU

cpu = CPU()

#cpu.load_instructions('instructions_numeric.txt') # Numeric Operations
#cpu.run()

cpu.load_instructions('instructions_text.txt') # Text storage
cpu.run()

cpu.show_registers()
cpu.show_memory()