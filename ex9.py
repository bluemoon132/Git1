def factorial(num):
    if num == 1:
        return num
    else:
        return (num * factorial(num - 1))


print(factorial(4))


def rprint(n):
    if n == 0:
        return
    else:
        rprint(n - 1)
        print(n)


rprint(3)


def tower_of_hanoi(n, tower1, tower2, tower3):
    if n == 1:
        print("Move", n, "from", tower1, "to", tower3)
    else:
        tower_of_hanoi(n - 1, tower1, tower3, tower2)
        print("Move", n, "from", tower1, "to", tower3)
        tower_of_hanoi(n - 1, tower2, tower1, tower3)


tower_of_hanoi(3, "tower 1", "tower 2", "tower 3")
