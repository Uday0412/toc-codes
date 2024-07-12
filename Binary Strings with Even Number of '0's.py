class DFA:
    def __init__(self):
        self.start_state = 'q0'
        self.accept_states = {'q0'}
        self.transition = {
            'q0': {'0': 'q1', '1': 'q0'},
            'q1': {'0': 'q0', '1': 'q1'}
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
binary_strings = ['1001', '1100', '1010', '0101', '111']
for binary in binary_strings:
    dfa.reset()
    if dfa.process(binary):
        print(f'The string {binary} is accepted by the DFA.')
    else:
        print(f'The string {binary} is rejected by the DFA.')
