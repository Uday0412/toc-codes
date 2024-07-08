class DFA_End00:
    def __init__(self):
        # Define DFA states and transitions
        self.states = ['q0', 'q1', 'q2']
        self.alphabet = ['0', '1']
        self.transition = {
            'q0': {'0': 'q1', '1': 'q0'},
            'q1': {'0': 'q2', '1': 'q0'},
            'q2': {'0': 'q2', '1': 'q0'}
        }
        self.start_state = 'q0'
        self.accept_states = ['q2']

    def accepts(self, string):
        current_state = self.start_state
        for char in string:
            if char in self.alphabet:
                current_state = self.transition[current_state][char]
            else:
                return False
        return current_state in self.accept_states

# Example usage
dfa_end00 = DFA_End00()
test_strings = ["", "0", "00", "10", "1100", "10100", "11100"]

for string in test_strings:
    if dfa_end00.accepts(string):
        print(f"The string '{string}' is accepted by the DFA (ends with '00').")
    else:
        print(f"The string '{string}' is not accepted by the DFA (does not end with '00').")
