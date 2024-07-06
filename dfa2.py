class DFA:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2','q3','q4'}
        self.alphabet = {'0', '1'}
        self.start_state = 'q0'
        self.accept_states = {'q1'}
        self.accept_states = {'q2'}
        self.accept_states = {'q3'}
        self.transitions = {
            ('q0', '1'): 'q1',
            ('q0', '0'): 'q4',
            ('q1', '1'): 'q2',
            ('q1', '0'): 'q4',
            ('q2', '0'): 'q3',
            ('q2', '1'): 'q4',
            ('q3', '0'): 'q3',
            ('q3', '1'): 'q3',
            ('q4', '1'): 'q4',
            ('q4', '0'): 'q4',
        }

    def accepts(self, string):
        current_state = self.start_state
        for char in string:
            current_state = self.transitions.get((current_state, char), 'q2')
        return current_state in self.accept_states

# Example usage
dfa = DFA()

test_strings = ["1", "10", "1101", "001", "101", "0", "111"]
for string in test_strings:
    result = dfa.accepts(string)
    print(f"String '{string}' is accepted: {result}")
