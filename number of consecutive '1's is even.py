class DFA:
    def __init__(self):
        self.states = {'q0', 'q1'}
        self.alphabet = {'0', '1'}
        self.initial_state = 'q0'
        self.accepting_state = 'q0'
        self.transitions = {
            ('q0', '0'): 'q0',
            ('q0', '1'): 'q1',
            ('q1', '0'): 'q0',
            ('q1', '1'): 'q0',
        }
    
    def accepts(self, input_string):
        current_state = self.initial_state
        consecutive_ones = 0
        
        for symbol in input_string:
            if symbol not in self.alphabet:
                return False
            if symbol == '1':
                consecutive_ones += 1
            else:
                consecutive_ones = 0
            current_state = self.transitions.get((current_state, symbol))
            if current_state is None:
                return False
        
        # Check if the final state is an accepting state and the number of consecutive '1's is even
        return current_state == self.accepting_state and consecutive_ones % 2 == 0

# Example usage:
dfa = DFA()
test_strings = ["101010", "111", "1001", "110011", "101"]

for test_string in test_strings:
    if dfa.accepts(test_string):
        print(f"Accepted: {test_string}")
    else:
        print(f"Rejected: {test_string}")
