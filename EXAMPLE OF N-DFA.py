class NFA:
    def __init__(self, num_states, final_states):
        self.num_states = num_states
        self.final_states = set(final_states)
        self.transitions = {}
        for i in range(num_states):
            self.transitions[i] = {}

    def add_transition(self, state, symbol, next_states):
        if symbol not in self.transitions[state]:
            self.transitions[state][symbol] = set()
        self.transitions[state][symbol].update(next_states)

    def is_accepted(self, input_string):
        current_states = set([0])
        for symbol in input_string:
            next_states = set()
            for state in current_states:
                if symbol in self.transitions[state]:
                    next_states.update(self.transitions[state][symbol])
            current_states = next_states
        return len(current_states & self.final_states) > 0

# Example usage
nfa = NFA(4, [3])
nfa.add_transition(0, 'a', [1, 2])
nfa.add_transition(1, 'b', [1])
nfa.add_transition(1, 'c', [3])
nfa.add_transition(2, 'c', [3])
nfa.add_transition(2, 'a', [2])

print(nfa.is_accepted('abcc'))  # True
print(nfa.is_accepted('aab'))   # False
print(nfa.is_accepted('ac'))    # True
