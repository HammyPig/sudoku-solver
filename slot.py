class Slot:
    def __init__(self, value=0):
        self.value = value
        
        if self.value == 0:
            self.possible_values = list(range(1, 10))
        else:
            self.possible_values = []
    

    def __str__(self):
        if self.value == 0:
            return " "
        else:
            return str(self.value)
    
    
    def set_value(self, value):
        self.value = value
    

    def remove_possible_value(self, value):
        self.possible_values.remove(value)
