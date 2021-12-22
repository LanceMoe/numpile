from numpile import autojit


@autojit
def add(a, b):
    for i in range(100):
        a += 1
    return a + b


a = 3.1415926
b = 2.7182818
result = add(a, b)
print(result)
