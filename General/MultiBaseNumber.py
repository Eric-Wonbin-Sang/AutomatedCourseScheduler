
class MultiBaseNumber:

    def __init__(self, base_list):

        self.base_list = base_list
        self.length = len(base_list)
        self.value_list = [0] * self.length

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
