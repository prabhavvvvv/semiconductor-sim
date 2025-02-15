class ANDGate:
    def logic(self, input1, input2):
        return input1 & input2

class NOTGate:
    def logic(self, input1):
        return 1 if input1 == 0 else 0

class HalfAdder:
    def __init__(self):
        self.xor_gate = lambda a, b: a ^ b
        self.and_gate = lambda a, b: a & b

    def add(self, a, b):
        sum_bit = self.xor_gate(a, b)
        carry_bit = self.and_gate(a, b)
        return (sum_bit, carry_bit)

# Instantiate
and_gate = ANDGate()
not_gate = NOTGate()
ha = HalfAdder()

# Print outputs line by line
print("AND(1,1) =", and_gate.logic(1,1))  # 1
print("AND(1,0) =", and_gate.logic(1,0))  # 0

print("NOT(1) =", not_gate.logic(1))     # 0
print("NOT(0) =", not_gate.logic(0))     # 1

print("HalfAdder(1,1) =", ha.add(1,1))   # (0, 1)
print("HalfAdder(1,0) =", ha.add(1,0))   # (1, 0)

class NMOS:
    def __init__(self, gate, source, drain):
        self.gate = gate
        self.source = source
        self.drain = drain

    def is_conducting(self):
        return self.gate == 1  # Conducts when gate is HIGH

class PMOS:
    def __init__(self, gate, source, drain):
        self.gate = gate
        self.source = source
        self.drain = drain

    def is_conducting(self):
        return self.gate == 0  # Conducts when gate is LOW

nmos = NMOS(gate=1, source=0, drain=1)
print(nmos.is_conducting())  # True (Conducts)

pmos = PMOS(gate=1, source=1, drain=0)
print(pmos.is_conducting())  # False (Does not conduct)

class NANDGate:
    def logic(self, input1, input2):
        nmos1 = NMOS(input1, 0, input2)
        nmos2 = NMOS(input2, 0, 0)
        pmos1 = PMOS(input1, 1, 1)
        pmos2 = PMOS(input2, 1, 1)

        if nmos1.is_conducting() and nmos2.is_conducting():
            return 0  # NMOS path is ON, output LOW
        else:
            return 1  # PMOS keeps it HIGH

nand_gate = NANDGate()
print(nand_gate.logic(1, 1))  # Output: 0
print(nand_gate.logic(1, 0))  # Output: 1

class HalfAdder:
    def __init__(self):
        self.xor_gate = lambda a, b: a ^ b  # XOR for Sum
        self.and_gate = lambda a, b: a & b  # AND for Carry

    def add(self, a, b):
        sum_bit = self.xor_gate(a, b)
        carry_bit = self.and_gate(a, b)
        return sum_bit, carry_bit

ha = HalfAdder()
print(ha.add(1, 1))  # Output: (0, 1) -> Sum: 0, Carry: 1
