def div_5(x):
    div5 = x%5 == 0
    return div5
def div_7(x):
    div7 = x%7 == 0
    return div7
def div_9(x):
    div9 = x%9 == 0
    return div9
def div_10(x):
    div10 = x%10 == 0
    return div10

if __name__ == "__main__":

    x = int(input("Enter the value of x: "))

    div5 = div_5(x)
    print(div5)
    div7 = div_7(x)
    print(div7)
    div9 = div_9(x)
    print(div9)
    div10 = div_10(x)
    print(div10)
