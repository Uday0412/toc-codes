class DFA:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2'}
        self.alphabet = {'a', 'b'}
        self.start_state = 'q0'
        self.accept_states = {'q1'}
        self.transitions = {
            ('q0', 'b'): 'q0',
            ('q0', 'a'): 'q1',
            ('q1', 'a'): 'q1',
            ('q1', 'b'): 'q2',
            ('q2', 'a'): 'q1',
            ('q2', 'b'): 'q2',
        }

    def accepts(self, string):
        current_state = self.start_state
        for char in string:
            current_state = self.transitions.get((current_state, char), 'q2')
        return current_state == 'q1'

# Example usage
dfa = DFA()

test_strings = ["a", "ba", "aa", "bba"]
for string in test_strings:
    result = dfa.accepts(string)
    print(f"String '{string}' is accepted: {result}")

#        a
#     +----+
#     |    |
#     v    |
#    (q0) ----> (q1)
#     |  \        ^
#     |   \       |
#     b   b \    a|
#     |      \    |
#     +----> (q2)
