class DFA_101:
    def __init__(self):
        # Define DFA states and transitions
        self.states = ['q0', 'q1', 'q2', 'q3']
        self.alphabet = ['0', '1']
        self.transition = {
            'q0': {'0': 'q0', '1': 'q1'},
            'q1': {'0': 'q2', '1': 'q1'},
            'q2': {'0': 'q0', '1': 'q3'},
            'q3': {'0': 'q3', '1': 'q3'}
        }
        self.start_state = 'q0'
        self.accept_states = ['q3']

    def accepts(self, string):
        current_state = self.start_state
        for char in string:
            if char in self.alphabet:
                current_state = self.transition[current_state][char]
            else:
                return False
        return current_state in self.accept_states

# Example usage
dfa_101 = DFA_101()
test_strings = ["", "0", "1", "101", "1001", "1101", "1010", "10101"]

for string in test_strings:
    if dfa_101.accepts(string):
        print(f"The string '{string}' is accepted by the DFA (contains '101').")
    else:
        print(f"The string '{string}' is not accepted by the DFA (does not contain '101').")
