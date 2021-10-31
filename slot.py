class Slot:
    def __init__(self, value=0):
        self.value = value
        
        if self.value == 0:
            self.possible_values = list(range(1, 10))
        else:
            self.possible_values = [self.value]
    

    def __repr__(self):
        if self.value == 0:
            return " "
        else:
            return str(self.value)
    
    
    def set_value(self, value):
        self.value = value
    

    def remove_possible_value(self, value):
        try:
            self.possible_values.remove(value.value)
        except ValueError:
            pass
    

    def print_possible_values(self):
        print("".join(str(n) for n in self.possible_values), end="")
        print((10 - len(self.possible_values)) * " ", end="")
