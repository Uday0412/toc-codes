class DFA:
    def __init__(self):
        self.start_state = 'q0'
        self.accept_states = {'q4'}
        self.transition = {
            'q0': {'a': 'q1', 'b': 'q0'},
            'q1': {'a': 'q1', 'b': 'q2'},
            'q2': {'a': 'q3', 'b': 'q0'},
            'q3': {'a': 'q1', 'b': 'q4'},
            'q4': {'a': 'q4', 'b': 'q4'}
        }
        self.current_state = self.start_state

    def reset(self):
        self.current_state = self.start_state

    def process(self, input_string):
        for char in input_string:
            if char in self.transition[self.current_state]:
                self.current_state = self.transition[self.current_state][char]
            else:
                return False
        return self.current_state in self.accept_states


dfa = DFA()
strings = ['aabba', 'abb', 'abbaa', 'bbaab', 'abbab']
for string in strings:
    dfa.reset()
    if dfa.process(string):
        print(f'The string "{string}" is accepted by the DFA.')
    else:
        print(f'The string "{string}" is rejected by the DFA.')
