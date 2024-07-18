class NDFA:
    def __init__(self):
        self.states = set()
        self.alphabet = set()
        self.transitions = {}
        self.start_state = None
        self.accept_states = set()

    def add_state(self, state, is_start=False, is_accept=False):
        self.states.add(state)
        if is_start:
            self.start_state = state
        if is_accept:
            self.accept_states.add(state)

    def add_transition(self, from_state, input_char, to_state):
        if (from_state, input_char) not in self.transitions:
            self.transitions[(from_state, input_char)] = []
        self.transitions[(from_state, input_char)].append(to_state)

    def epsilon_closure(self, state):
        stack = [state]
        closure = set(stack)
        while stack:
            current_state = stack.pop()
            if (current_state, '') in self.transitions:
                for next_state in self.transitions[(current_state, '')]:
                    if next_state not in closure:
                        closure.add(next_state)
                        stack.append(next_state)
        return closure

    def move(self, states, input_char):
        next_states = set()
        for state in states:
            if (state, input_char) in self.transitions:
                next_states.update(self.transitions[(state, input_char)])
        return next_states

    def is_accepted(self, input_string):
        current_states = self.epsilon_closure(self.start_state)
        for char in input_string:
            current_states = self.epsilon_closure(set.union(*[self.move(current_states, char)]))
        return not self.accept_states.isdisjoint(current_states)

# Create the NDFA
ndfa = NDFA()

# Add states
ndfa.add_state('q0', is_start=True)
ndfa.add_state('q1')
ndfa.add_state('q2', is_accept=True)

# Add transitions
ndfa.add_transition('q0', 'a', 'q1')
ndfa.add_transition('q0', 'b', 'q2')
ndfa.add_transition('q1', 'b', 'q2')
ndfa.add_transition('q2', 'a', 'q1')

# Test strings
test_strings = ['ab', 'ba', 'aa', 'bb', 'aab', 'bba', 'abab', 'baba', '']

for string in test_strings:
    print(f"The string '{string}' is accepted by the NDFA: {ndfa.is_accepted(string)}")
