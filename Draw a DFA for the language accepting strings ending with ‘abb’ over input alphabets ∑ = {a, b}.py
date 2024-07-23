# DFA for language ending with 'abb'
dfa = {
    'q0': {'a': 'q1', 'b': 'q0'},   # initial state
    'q1': {'a': 'q1', 'b': 'q2'},   # state after reading 'a'
    'q2': {'a': 'q1', 'b': 'q3'},   # state after reading 'ab'
    'q3': {'a': 'q1', 'b': 'q0'}    # state after reading 'abb'
}

accepting_states = ['q3']  # final state

def is_accepted(input_string):
    current_state = 'q0'  # start at the initial state

    for char in input_string:
        current_state = dfa[current_state][char]

    return current_state in accepting_states

# Test the DFA
test_strings = ['abb', 'aabb', 'bababb', 'ab', 'aab', 'bb']
results = {s: is_accepted(s) for s in test_strings}

for s in results:
    print(f"The string '{s}' is {'accepted' if results[s] else 'not accepted'} by the DFA.")
