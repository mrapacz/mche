import sys
import operator


def help_calc():
    print("Put the numbers and operators space-separated:\n"
          "e.g. python main.py ( 3 + 5 ) * 8 - 10 / 5\n"
          "Script currently understands: +, -, /, *, (, )\n"
          "Please remember to escape * when using bash [/*]")


def even_args():
    print("Even number of arguments. Please refer to help")


def find_and_resolve_parenthesis(arguments):
    open_sign_pos = find_sign_pos(arguments, "(")
    while open_sign_pos != -1:
        close_sign_pos = find_sign_pos(arguments, ")", True)
        if close_sign_pos == -1:
            raise Exception("Parenthesis not closed!")
        first_part = [] if open_sign_pos == 0 else arguments[:open_sign_pos]
        arguments = first_part + calculate_list(arguments[open_sign_pos + 1:close_sign_pos]) + arguments[
                                                                                               close_sign_pos + 1:]
        open_sign_pos = find_sign_pos(arguments, "(")
    return arguments


def find_sign_pos(arguments, signs, reverse=False):
    run_range = reversed(range(len(arguments))) if reverse else range(len(arguments))
    for i in run_range:
        if str(arguments[i]) in signs:
            return i
    return -1


def calculate_around_sign_position(arguments, sign_pos, func):
    outcome = func(float(arguments[sign_pos - 1]), float(arguments[sign_pos + 1]))
    return arguments[:sign_pos - 1] + [outcome] + arguments[sign_pos + 2:]


def find_and_resolve_function(arguments, function_dict):
    sign_pos = find_sign_pos(arguments, function_dict.keys())
    while sign_pos != -1:
        for sign in function_dict.keys():
            if arguments[sign_pos] == sign:
                arguments = calculate_around_sign_position(arguments, sign_pos, function_dict[sign])
                break
        sign_pos = find_sign_pos(arguments, function_dict.keys())
    return arguments


def calculate_list(arguments):
    arguments = find_and_resolve_parenthesis(arguments)
    arguments = find_and_resolve_function(arguments, {"*": operator.mul, "/": operator.truediv})
    arguments = find_and_resolve_function(arguments, {"+": operator.add, "-": operator.sub})
    return arguments


def calc(arguments):
    arguments = calculate_list(arguments)
    if len(arguments) != 1:
        print("Unable to calc :(")
    else:
        print(arguments[0])


if __name__ == "__main__":
    no_args = len(sys.argv) - 1
    if no_args == 0:
        help_calc()
    elif no_args == 1:
        help_calc()
        if sys.argv[1] == "interactive":
            calc(input("Type in your equation without escaping chars\n").split())
    else:
        if no_args % 2 == 0:
            even_args()
        else:
            calc(sys.argv[1:])
