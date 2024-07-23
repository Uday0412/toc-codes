# DFA implementation in Python to recognize strings ending with '01'

class DFA:
    def __init__(self):
        self.state = 'q0'
    
    def transition(self, char):
        if self.state == 'q0':
            if char == '0':
                self.state = 'q1'
            elif char == '1':
                self.state = 'q0'
        
        elif self.state == 'q1':
            if char == '0':
                self.state = 'q1'
            elif char == '1':
                self.state = 'q2'
        
        elif self.state == 'q2':
            if char == '0':
                self.state = 'q1'
            elif char == '1':
                self.state = 'q3'
        
        elif self.state == 'q3':
            if char == '0':
                self.state = 'q1'
            elif char == '1':
                self.state = 'q0'
    
    def is_accepting(self):
        return self.state == 'q2'

# Function to check if a string is accepted by the DFA
def is_accepted(string):
    dfa = DFA()
    for char in string:
        dfa.transition(char)
    return dfa.is_accepting()

# Example usage
test_strings = ["101", "1101", "1001", "01", "0", "1", "000", "010", "111"]
for s in test_strings:
    print(f"String '{s}' is accepted: {is_accepted(s)}")



'''
      (q0) --0--> (q1) --0--> (q1)
    |            |         |
    1            1         1
    |            |         |
   (q0)        (q2) --1--> (q3)
                 |         |
                 0         0
                 |         |
                (q1)     (q1)

'''