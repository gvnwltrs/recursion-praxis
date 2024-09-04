
def print_hello(num):
    if num == 0:
        return
    print("Hello!")
    num -= 1
    print_hello(num)

print_hello(5)

def iterate_list(lst):
    if not lst:
        return
    print(lst[0])
    iterate_list(lst[1:])

iterate_list([1, 2, 3, 4, 5])