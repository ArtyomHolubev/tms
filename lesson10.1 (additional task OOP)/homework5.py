class MyStack:

    def __init__(self, input_list: list = None):
        self.input_list = input_list
        self.internal_list = [1, 2, 3]
        self.internal_list.extend(self.input_list)

    def push(self, new_argument):
        self.internal_list.insert(0, new_argument)
        return self.internal_list

    def pop(self):
        element = self.internal_list[0]
        self.internal_list.pop(0)
        return element

    def is_empty(self):
        if len(self.internal_list) == 0:
            return False
        else:
            return True


# stack = MyStack([4, 5, 6])
# print(stack.push(56))
# print(f"*******************************************************")
# print(stack.pop())
# print(stack.internal_list)
# print(f"*******************************************************")
# print(f"*******************************************************")
# print(stack.pop())
# print(stack.internal_list)
# print(stack.is_empty())
# print(f"*******************************************************")
# print(f"*******************************************************")
# print(stack.pop())
# print(stack.internal_list)
# print(stack.is_empty())
# print(f"*******************************************************")
# print(f"*******************************************************")
# print(stack.pop())
# print(stack.internal_list)
# print(stack.is_empty())
# print(f"*******************************************************")
# print(f"*******************************************************")
# print(stack.pop())
# print(stack.internal_list)
# print(stack.is_empty())
# print(f"*******************************************************")
# print(f"*******************************************************")
# print(stack.pop())
# print(stack.internal_list)
# print(stack.is_empty())
# print(f"*******************************************************")
# print(f"*******************************************************")
# print(stack.pop())
# print(stack.internal_list)
# print(stack.is_empty())
