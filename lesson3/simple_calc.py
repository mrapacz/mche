import operator

actions = {
    "+": operator.add,
    "-": operator.sub,
    "/": operator.truediv,
    "*": operator.mul,
}

arg1, action, arg2 = input().split()

result = actions[action](
    float(arg1),
    float(arg2),
)
print(result)
