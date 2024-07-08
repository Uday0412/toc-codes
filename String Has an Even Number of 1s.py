class DFA_Even1s:
    def __init__(self):
        # Define DFA states and transitions
        self.states = ['q0', 'q1']
        self.alphabet = ['0', '1']
        self.transition = {
            'q0': {'0': 'q0', '1': 'q1'},
            'q1': {'0': 'q1', '1': 'q0'}
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
dfa_even1s = DFA_Even1s()
test_strings = ["", "0", "1", "11", "101", "1001", "1111", "1100"]

for string in test_strings:
    if dfa_even1s.accepts(string):
        print(f"The string '{string}' is accepted by the DFA (even number of '1's).")
    else:
        print(f"The string '{string}' is not accepted by the DFA (odd number of '1's).")
