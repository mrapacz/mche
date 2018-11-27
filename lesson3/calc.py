import sys
import operator

CURRENTLY_PARSED = "Script currently understands: +, -, /, *, (, )\n"
SPACE_SEPARATED = "Put the numbers and operators space-separated\n"

INTRO = CURRENTLY_PARSED + SPACE_SEPARATED


def help_bash():
    print(INTRO +
          "e.g. python calc.py ( 3 + 5 ) * 8 - 10 / 5\n"
          "Please remember to escape * when using bash [/*]")


def help_interactive():
    print(INTRO);


def even_args():
    print("Even number of arguments. Please refer to help")


def find_and_resolve_parenthesis(arguments):
    open_sign_pos = find_sign_pos(arguments, "(")
    while open_sign_pos is not None:
        close_sign_pos = find_sign_pos(arguments, ")", True)
        if not close_sign_pos:
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
    return None


def calculate_around_sign_position(arguments, sign_pos, func):
    outcome = func(float(arguments[sign_pos - 1]), float(arguments[sign_pos + 1]))
    return arguments[:sign_pos - 1] + [outcome] + arguments[sign_pos + 2:]


def find_and_resolve_function(arguments, function_dict):
    sign_pos = find_sign_pos(arguments, function_dict)
    while sign_pos is not None:
        arguments = calculate_around_sign_position(arguments, sign_pos, function_dict[arguments[sign_pos]])
        sign_pos = find_sign_pos(arguments, function_dict)
    return arguments


def calculate_list(arguments):
    arguments = find_and_resolve_parenthesis(arguments)
    operations_in_order = (
        {"*": operator.mul, "/": operator.truediv},
        {"+": operator.add, "-": operator.sub})
    for operations_group in operations_in_order:
        arguments = find_and_resolve_function(arguments, operations_group)
    return arguments


def calc(arguments):
    arguments = calculate_list(arguments)
    if len(arguments) != 1:
        print("Unable to calc :(")
    else:
        print(arguments[0])


if __name__ == "__main__":
    arg_count = len(sys.argv) - 1
    if arg_count == 0:
        help_bash()
    elif arg_count == 1:
        if sys.argv[1] == "interactive":
            help_interactive()
            calc(input().split())
        else:
            help_bash()
    else:
        if arg_count % 2 == 0:
            even_args()
        else:
            calc(sys.argv[1:])
