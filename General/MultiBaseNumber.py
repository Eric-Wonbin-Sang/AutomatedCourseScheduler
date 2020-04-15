
class MultiBaseNumber:

    def __init__(self, base_list):

        self.base_list = base_list
        self.length = len(base_list)
        self.value_list = [0] * self.length

        self.possible_iteration_count = self.get_possible_iteration_count()

    def get_possible_iteration_count(self):
        possible_iteration_count = 1
        for base in self.base_list:
            possible_iteration_count *= base
        return possible_iteration_count

    def iterate(self):

        self.value_list[-1] += 1

        for i in range(self.length):
            curr_i = self.length - i - 1
            if self.value_list[curr_i] >= self.base_list[curr_i]:
                self.value_list[curr_i] = 0
                if curr_i < self.length:
                    self.value_list[curr_i - 1] += 1

    def __str__(self):
        ret_str = "["
        for i, value in enumerate(self.value_list):
            if i != 0:
                ret_str += ", "
            ret_str += "{}: {}".format(self.base_list[i], self.value_list[i])
        return ret_str + "]"
