class DFA:
    def __init__(self):
        self.states = ['q0', 'q1', 'q2', 'q3', 'q4']
        self.alphabet = ['a', 'b']
        self.transition_function = {
            ('q0', 'a'): 'q1',
            ('q0', 'b'): 'q0',
            ('q1', 'a'): 'q1',
            ('q1', 'b'): 'q2',
            ('q2', 'a'): 'q3',
            ('q2', 'b'): 'q0',
            ('q3', 'a'): 'q1',
            ('q3', 'b'): 'q4',
            ('q4', 'a'): 'q1',
            ('q4', 'b'): 'q0'
        }
        self.start_state = 'q0'
        self.accept_states = ['q4']

    def process_string(self, input_string):
        current_state = self.start_state
        for char in input_string:
            current_state = self.transition_function.get((current_state, char), 'q0')
        return current_state in self.accept_states

# Example usage:
dfa = DFA()
test_string = "xxabba"
print(f"Does '{test_string}' end with 'abba'? {'Yes' if dfa.process_string(test_string) else 'No'}")




'''
I find this diagram by chatgpt

  a   b   a   b
(q0)-->(q1)-->(q2)-->(q3)-->(q4)
 |     /  |    /  |    /  |    /
 |    /   |   /   |   /   |   /
 V   /    V  /    V  /    V  /
(q0) <---(q1) <---(q2) <---(q3)
  b       b        b        a


'''