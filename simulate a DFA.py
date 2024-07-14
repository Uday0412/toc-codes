class DFA:
    def __init__(self, states, alphabet, initial_state, accepting_states, transitions):
        self.states = states
        self.alphabet = alphabet
        self.initial_state = initial_state
        self.accepting_states = accepting_states
        self.transitions = transitions
        
    def accepts(self, input_string):
        current_state = self.initial_state
        for symbol in input_string:
            if symbol not in self.alphabet:
                return False
            current_state = self.transitions.get((current_state, symbol))
            if current_state is None:
                return False
        return current_state in self.accepting_states

# Example usage:
states = {'q0', 'q1', 'q2'}
alphabet = {'0', '1'}
initial_state = 'q0'
accepting_states = {'q1'}
transitions = {
    ('q0', '0'): 'q1',
    ('q0', '1'): 'q0',
    ('q1', '0'): 'q2',
    ('q1', '1'): 'q1',
    ('q2', '0'): 'q2',
    ('q2', '1'): 'q2',
}

dfa = DFA(states, alphabet, initial_state, accepting_states, transitions)
test_strings = ["101", "010", "110", "000", "11"]

for test_string in test_strings:
    if dfa.accepts(test_string):
        print(f"Accepted: {test_string}")
    else:
        print(f"Rejected: {test_string}")
