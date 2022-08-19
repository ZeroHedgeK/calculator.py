def check(v1, v2, v3):
    msg = ''

    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6
    if (v1 == 1 or v2 == 1) and v3 == '*':
        msg += msg_7
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg += msg_8
    if msg != '':
        msg = msg_9 + msg
    print(msg)


def is_one_digit(v):
    if -10 < v < 10 and v.is_integer():
        return True
    return False


msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
msg_ = [msg_0, msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, msg_7, msg_8, msg_9, msg_10, msg_11, msg_12]
memory = 0.0

result = float
while True:
    print(msg_0)
    calc = input().split()

    try:
        x = memory if calc[0] == 'M' else float(calc[0])
        y = memory if calc[2] == 'M' else float(calc[2])
        operation = calc[1]

        if operation not in '+-*/':
            print(msg_2)
            continue

        check(x, y, operation)

        if operation == '+':
            result = x + y
        elif operation == '-':
            result = x - y
        elif operation == '*':
            result = x * y
        elif operation == '/':
            result = x / y
    except ValueError:
        print(msg_1)
    except ZeroDivisionError:
        print(msg_3)
    else:
        print(result)

        answer1 = str
        while answer1 not in ('y', 'n'):
            print(msg_4)
            answer1 = input()
            if answer1 == 'y':
                if is_one_digit(result):
                    msg_index = 10
                    print(msg_[msg_index])
                    answer3 = input()
                    if answer3 == "y":
                        while msg_index < 12:
                            msg_index = msg_index + 1
                            print(msg_[msg_index])
                            answer3 = input()
                            if answer3 == 'n':

                                break
                            else:
                                memory = result
                                continue
                    else:
                        continue
                else:
                    memory = result
                    break
            else:
                continue

        answer2 = str
        while answer2 not in ('y', 'n'):
            print(msg_5)
            answer2 = input()

        if answer2 == 'y':
            continue

        break
