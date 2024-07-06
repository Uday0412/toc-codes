class DFA:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2'}
        self.alphabet = {'0', '1'}
        self.start_state = 'q0'
        self.accept_states = {'q1'}
        self.transitions = {
            ('q0', '1'): 'q1',
            ('q0', '0'): 'q2',
            ('q1', '1'): 'q1',
            ('q1', '0'): 'q1',
            ('q2', '1'): 'q2',
            ('q2', '0'): 'q2',
        }

    def accepts(self, string):
        current_state = self.start_state
        for char in string:
            current_state = self.transitions.get((current_state, char), 'q2')
        return current_state in self.accept_states

# Example usage
dfa = DFA()

test_strings = ["1", "10", "110", "001", "101", "0", "111"]
for string in test_strings:
    result = dfa.accepts(string)
    print(f"String '{string}' is accepted: {result}")
