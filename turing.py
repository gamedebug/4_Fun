class TuringMachine:
    def __init__(self, tape, initial_state, transition_function, final_states):
        self.tape = list(tape)
        self.head_position = 0
        self.current_state = initial_state
        self.transition_function = transition_function
        self.final_states = final_states

    def run(self):
        while self.current_state not in self.final_states:
            symbol = self.tape[self.head_position]
            if (self.current_state, symbol) not in self.transition_function:
                raise Exception("No transition defined for state: {}, symbol: {}".format(
                    self.current_state, symbol))
            new_state, new_symbol, move = self.transition_function[(self.current_state, symbol)]
            self.tape[self.head_position] = new_symbol
            self.current_state = new_state

            if move == 'L':
                self.head_position -= 1
            elif move == 'R':
                self.head_position += 1

            if self.head_position < 0:
                self.tape = ['B'] + self.tape
                self.head_position = 0
            elif self.head_position >= len(self.tape):
                self.tape.append('B')

    def get_tape(self):
        return "".join(self.tape)


# 示例用法
tape = "0101010"
initial_state = "q0"
transition_function = {
    ("q0", "0"): ("q1", "1", "R"),
    ("q0", "1"): ("q2", "0", "R"),
    ("q1", "0"): ("q1", "0", "L"),
    ("q1", "1"): ("q2", "0", "R"),
    ("q2", "0"): ("q2", "1", "R"),
    ("q2", "1"): ("q0", "1", "R"),
}
final_states = {"q0"}

tm = TuringMachine(tape, initial_state, transition_function, final_states)
tm.run()
result = tm.get_tape()
print("Final tape content:", result)
