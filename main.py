

# def select_operation(choice):
#     if choice == 1:
#         return lambda a, b: a + b
#     elif choice == 2:
#         return lambda a, b: a - b
#     else:
#         return lambda a, b: a * b


# operation = select_operation(1)  # operation = sum
# print(operation(10, 6))  # 16
#
# operation = select_operation(2)  # operation = subtract
# print(operation(10, 6))  # 4
#
# operation = select_operation(3)  # operation = multiply
# print(operation(10, 6))  # 60
#
from Ass import Ass

a = "2"
b = 3
c = int(a) + b
print(c)

def test():
    print(a)

test()
#b=Ass()
a = Ass(4,1)
a.a=123
print(a.a)
#b.print()
a.print()


