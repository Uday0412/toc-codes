class DFA:
    def __init__(self):
        # Define DFA states and transitions
        self.states = ['q0', 'q1']
        self.alphabet = ['0', '1']
        self.transition = {
            'q0': {'0': 'q1', '1': 'q0'},
            'q1': {'0': 'q0', '1': 'q1'}
        }
        self.start_state = 'q0'
        self.accept_states = ['q0']

    def accepts(self, string):
        current_state = self.start_state
        for char in string:
            if char in self.alphabet:
                current_state = self.transition[current_state][char]
            else:
                return False
        return current_state in self.accept_states

# Example usage
dfa = DFA()
test_strings = ["", "0", "1", "00", "01", "10", "11", "000", "001", "010", "100", "101"]

for string in test_strings:
    if dfa.accepts(string):
        print(f"The string '{string}' is accepted by the DFA.")
    else:
        print(f"The string '{string}' is not accepted by the DFA.")
