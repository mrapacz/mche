import operator

operators = {
    "+": operator.add,
    "-": operator.sub,
    "/": operator.truediv,
    "*": operator.mul,
}

user_command = input()
for operator in operators:
    if operator in user_command:
        arg1, arg2 = (float(arg) for arg in user_command.split(operator))
        result = operators[operator](arg1, arg2)
        print(result)
