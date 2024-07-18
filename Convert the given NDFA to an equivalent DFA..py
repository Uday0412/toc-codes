from collections import defaultdict

class NDFA:
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states

class DFA:
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states

def convert_ndfa_to_dfa(ndfa):
    dfa_states = set()
    dfa_start_state = frozenset([ndfa.start_state])
    dfa_accept_states = set()
    dfa_transitions = {}

    unprocessed_states = [dfa_start_state]
    processed_states = set()

    while unprocessed_states:
        current_dfa_state = unprocessed_states.pop()
        processed_states.add(current_dfa_state)

        if any(state in ndfa.accept_states for state in current_dfa_state):
            dfa_accept_states.add(current_dfa_state)

        for symbol in ndfa.alphabet:
            next_dfa_state = set()
            for state in current_dfa_state:
                next_dfa_state.update(ndfa.transitions[state][symbol])

            next_dfa_state = frozenset(next_dfa_state)

            if next_dfa_state not in processed_states and next_dfa_state not in unprocessed_states:
                unprocessed_states.append(next_dfa_state)

            dfa_transitions[(current_dfa_state, symbol)] = next_dfa_state

    dfa_states = processed_states

    return DFA(dfa_states, ndfa.alphabet, dfa_transitions, dfa_start_state, dfa_accept_states)

# Example NDFA definition
states = {'q0', 'q1', 'q2'}
alphabet = {'0', '1'}
transitions = {
    'q0': {'0': {'q0', 'q1'}, '1': {'q0'}},
    'q1': {'1': {'q2'}},
    'q2': {'0': {'q2'}, '1': {'q2'}}
}
start_state = 'q0'
accept_states = {'q2'}

ndfa = NDFA(states, alphabet, transitions, start_state, accept_states)
dfa = convert_ndfa_to_dfa(ndfa)

print("DFA States:", dfa.states)
print("DFA Start State:", dfa.start_state)
print("DFA Accept States:", dfa.accept_states)
print("DFA Transitions:")
for (state, symbol), next_state in dfa.transitions.items():
    print(f"  δ({state}, {symbol}) = {next_state}")
