class AFD:
    def __init__(self):
        self.states = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6']
        self.start_state = 'q0'
        self.accept_states = ['q1', 'q2', 'q5']
        self.transition_table = {
            'q0': {'alphabet': 'q1', 'punctuation_and_space': 'q2', '|': 'q3'},
            'q1': {'alphabet': 'q1', 'punctuation_and_space': 'q2', '|': 'q2'},
            'q2': {'alphabet': 'q1', 'punctuation_and_space': 'q2', '|': 'q2'},
            'q3': {'alphabet': 'q3', 'punctuation_and_space': 'q4', '|': 'q5'},
            'q4': {'alphabet': 'q3', 'punctuation_and_space': 'q4', '|': 'q5'},
            'q5': {'alphabet': 'q6', 'punctuation_and_space': 'q6', '|': 'q3'},
            'q6': {'alphabet': 'q6', 'punctuation_and_space': 'q6', '|': 'q6'},
        }

    def transition(self, state, symbol):
        for key in self.transition_table[state]:
            if self.matches(symbol, key):
                return self.transition_table[state][key]
        return None

    def matches(self, symbol, category):
        if category == 'alphabet':
            return symbol.isalpha()
        if category == 'punctuation_and_space':
            return symbol in ',.¿?!¡ '
        return category == '|' and symbol == '|'

    def process_string(self, input_string):
        current_state = self.start_state
        for symbol in input_string:
            next_state = self.transition(current_state, symbol)
            if next_state is None:
                return False
            current_state = next_state

        if current_state in self.accept_states:
            return current_state
        else:
            return False
