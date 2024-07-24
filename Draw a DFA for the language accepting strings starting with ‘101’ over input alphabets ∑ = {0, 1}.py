class DFA:
    def __init__(self):
        self.states = ['q0', 'q1', 'q2']
        self.alphabet = ['0', '1']
        self.final_state=['q3']
        self.dead_stae=['q4']
        self.transition_function = {
            ('q0', '1'): 'q1',
            ('q0', '0'): 'q4',
            ('q1', '0'): 'q2',
            ('q1', '1'): 'q4',
            ('q2', '1'): 'q3',
            ('q2', '0'): 'q4',
            ('q4', '1'): 'q4',
            ('q3', '0'): 'q4',
        }
        self.start_state = 'q0'
        self.dead_stae= ['q4']

    def process_string(self, input_string):
        current_state = self.start_state
        for char in input_string:
            current_state = self.transition_function.get((current_state, char), 'q0')
        return current_state in self.accept_states

# Example usage:
dfa = DFA()
test_string = "xxabba"
print(f"Does '{test_string}' end with 'abba'? {'Yes' if dfa.process_string(test_string) else 'No'}")




