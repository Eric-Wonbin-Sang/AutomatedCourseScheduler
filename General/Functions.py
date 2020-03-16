import pickle
import os


def string_to_length(some_str, length, flush="left", dots=False):
    new_str = some_str[:min(length, len(some_str))]
    if flush == "left":
        new_str += max(0, length - len(some_str)) * " "
    else:
        new_str = max(0, length - len(some_str)) * " " + new_str

    if dots and length < len(some_str) and flush == "left":
        new_str = new_str[:-3] + "..."
    return new_str


def string_to_alternating_letter_to_num(some_string):
    some_string = some_string.replace(" ", "")
    ret_list = []
    temp_string = ""
    is_letter = some_string[0].isalpha()
    prev_is_letter = is_letter
    for letter in some_string:
        temp_string += letter
        is_letter = letter.isalpha()
        if is_letter != prev_is_letter:
            ret_list.append(temp_string[:-1])
            temp_string = temp_string[-1]
        prev_is_letter = is_letter
    ret_list.append(temp_string)
    return ret_list


def dict_to_string(data_dict, dict_name=""):
    ret_str = "Dict: " + dict_name
    for key in data_dict:
        ret_str += "\n\t" + str(key) + ": " + str(data_dict[key])
    return ret_str


def clean_dict(data_dict):
    new_dict = {}
    for key in remove_empty_values(data_dict):
        new_key = ""
        for i, letter in enumerate(str(key)):
            if letter.isupper() and i != 0:
                new_key += "_" + letter.lower()
            else:
                new_key += letter.lower()
        new_dict[new_key] = data_dict[key]
    return new_dict


def is_connected():
    return False


def multiply_list(data_list):
    ret_int = 1
    for data in data_list:
        ret_int *= data
    return ret_int


# Dict funcs ---------------------------------------------------------------------


def find_first_occurrence_in_dicts(key, *dict_list):
    for data_dict in dict_list:
        if key in data_dict:
            return data_dict[key]
    return None


def remove_empty_values(data_dict):
    ret_dict = {}
    for key in data_dict:
        if type(data_dict[key]) == str and data_dict[key].strip() != "":
            ret_dict[key] = data_dict[key]
    return ret_dict


def tab_string(data_str):
    return "\t" + data_str.replace("\n", "\n\t")


def remove_from_dict(data_dict, *keys):
    ret_dict = {}
    for key in data_dict:
        if key not in keys:
            ret_dict[key] = data_dict[key]
    return ret_dict


# GUI funcs ---------------------------------------------------------------------

def clear_layout(layout):
    for child in layout.children:
        layout.remove_widget(child)
    return layout


def add_to_layout(layout, *widget_list):
    for widget in widget_list:
        layout.add_widget(widget)
    return layout

# ---------------------------------------------------------------------


def txt_doc_to_str(some_path):
    if os.path.exists(some_path):
        txt_doc = open(some_path, "r")
        str_ret = txt_doc.read()
        txt_doc.close()
    else:
        str_ret = "Path {} not found".format(some_path)
    return str_ret


def pickle_object(obj, path):
    print("Pickling {}".format(obj))
    pickle_out = open(path, "wb")
    pickle.dump(obj, pickle_out)
    pickle_out.close()
    print("Done pickling")


def remove_none_from_list(data_list):
    return [data for data in data_list if data is not None]


def string_to_command_list_list(string, command_name_list):

    raw_command_list = [part for part in string.lower().split(" ") if part != ""]

    start_index = None
    command_list_list = []
    for c_i, command in enumerate(raw_command_list):
        if command in command_name_list:
            if start_index is not None:
                command_list_list.append(raw_command_list[start_index:c_i])
            start_index = c_i
    last_command_list = raw_command_list[start_index:]
    if last_command_list:
        command_list_list.append(last_command_list)
    return command_list_list


def decrement_repeating_returns(string):
    str_ret = ""
    for part in string.split("\n"):
        str_ret += part
        if part == "":
            str_ret += "\n"
    return str_ret


def get_nice_time_format(some_time):
    return some_time.strftime("%I:%M%p")


def shift_string_block(string_block, spacer):
    return spacer + string_block.replace("\n", "\n{}".format(spacer))


def txt_to_dict(txt_path):
    ret_dict = {}
    for line in open(txt_path):
        key, value = [obj.strip() for obj in line.split(":")]
        ret_dict[key] = value
    return ret_dict


def get_curr_parent_dir(path_addition=None):
    return os.path.dirname(os.getcwd()) + path_addition if path_addition is not None else ""


def rotate_list_list(data_list_list):
    return [list(x) for x in zip(*data_list_list)]
