# Example NDFA
from os import stat


class NDFA: 
    states = {'q0', 'q1', 'q2'}
alphabet = {'0', '1'}
transitions = {
    ('q0', '0'): {'q0', 'q1'},
    ('q0', '1'): {'q0'},
    ('q1', '1'): {'q2'},
}
start_state = 'q0'
accept_states = {'q2'}

ndfa = NDFA(stat, alphabet, transitions, start_state, accept_states)

# Test strings
test_strings = ['011', '1001', '1101', '111']

for string in test_strings:
    if ndfa.is_accepted(string):
        print(f'String "{string}" is accepted.')
    else:
        print(f'String "{string}" is not accepted.')
