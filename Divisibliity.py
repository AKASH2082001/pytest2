def div_5(x):
    if x%5 == 0:
        return True
    else:
        return False
def div_7(x):
    if x%7 == 0:
        return True
    else:
        return False
def div_9(x):
    if x%9 == 0:
        return True
    else:
        return False
def div_10(x):
    if x%10 == 0:
        return True
    else:
        return False

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
