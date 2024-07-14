class DFA:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2'}
        self.alphabet = {'0', '1'}
        self.initial_state = 'q0'
        self.accepting_state = 'q0'
        self.transitions = {
            ('q0', '0'): 'q1',
            ('q0', '1'): 'q0',
            ('q1', '0'): 'q2',
            ('q1', '1'): 'q1',
            ('q2', '0'): 'q0',
            ('q2', '1'): 'q2',
        }
    
    def accepts(self, input_string):
        current_state = self.initial_state
        count_zeros = 0
        
        for symbol in input_string:
            if symbol not in self.alphabet:
                return False
            if symbol == '0':
                count_zeros += 1
            current_state = self.transitions.get((current_state, symbol))
            if current_state is None:
                return False
        
        # Check if the final state is an accepting state and the count of '0's is divisible by 3
        return current_state == self.accepting_state and count_zeros % 3 == 0

# Example usage:
dfa = DFA()
test_strings = ["101010", "000", "111000", "1100", "1001"]

for test_string in test_strings:
    if dfa.accepts(test_string):
        print(f"Accepted: {test_string}")
    else:
        print(f"Rejected: {test_string}")
