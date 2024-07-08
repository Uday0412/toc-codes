class DFA_Odd0sOdd1s:
    def __init__(self):
        # Define DFA states and transitions
        self.states = ['q00', 'q01', 'q10', 'q11']
        self.alphabet = ['0', '1']
        self.transition = {
            'q00': {'0': 'q10', '1': 'q01'},
            'q01': {'0': 'q11', '1': 'q00'},
            'q10': {'0': 'q00', '1': 'q11'},
            'q11': {'0': 'q01', '1': 'q10'}
        }
        self.start_state = 'q00'
        self.accept_states = ['q11']

    def accepts(self, string):
        current_state = self.start_state
        for char in string:
            if char in self.alphabet:
                current_state = self.transition[current_state][char]
            else:
                return False
        return current_state in self.accept_states

# Example usage
dfa_odd0sOdd1s = DFA_Odd0sOdd1s()
test_strings = ["", "0", "1", "01", "10", "111", "1100", "10101"]

for string in test_strings:
    if dfa_odd0sOdd1s.accepts(string):
        print(f"The string '{string}' is accepted by the DFA (odd number of '0's and '1's).")
    else:
        print(f"The string '{string}' is not accepted by the DFA (not odd number of '0's and '1's).")
