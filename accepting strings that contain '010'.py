class DFA:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2', 'q3'}  # set of states
        self.alphabet = {'0', '1'}              # input alphabet
        self.start_state = 'q0'                 # start state
        self.accept_states = {'q3'}             # set of accept states
        self.transitions = {
            ('q0', '0'): 'q1',                  # transition function δ
            ('q0', '1'): 'q0',
            ('q1', '1'): 'q2',
            ('q1', '0'): 'q1',
            ('q2', '0'): 'q3',
            ('q2', '1'): 'q0',
            ('q3', '0'): 'q3',
            ('q3', '1'): 'q3'
        }

    def is_accepted(self, input_string):
        current_state = self.start_state
        for symbol in input_string:
            if symbol not in self.alphabet:
                return False
            current_state = self.transitions.get((current_state, symbol), None)
            if current_state is None:
                return False
        return current_state in self.accept_states

# Example usage:
dfa = DFA()
test_string = "101010"
if dfa.is_accepted(test_string):
    print(f"The string '{test_string}' is accepted by the DFA.")
else:
    print(f"The string '{test_string}' is not accepted by the DFA.")
