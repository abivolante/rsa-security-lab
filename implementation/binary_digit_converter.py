#We need a way to compute the binary form of any number

#Algorithm to compute any number into its binary form
#We use stacks

class Stack:
  def __init__(self):
    self.stack = []

  def push(self, element):
    self.stack.append(element)

  def pop(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.stack.pop()

  def peek(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.stack[-1]

  def isEmpty(self):
    return len(self.stack) == 0

  def size(self):
    return len(self.stack)


def conv_to_bin(number):
    binary_digits = Stack()

    while number>0:
        remainder = number % 2
        binary_digits.push(remainder)
        number= number // 2

    bin_form = ""
    while not binary_digits.isEmpty():
        bin_form = bin_form + str(binary_digits.pop())

    print(bin_form)

