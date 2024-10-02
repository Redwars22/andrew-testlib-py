from andtlib import AndrewTestingLibrary

test = AndrewTestingLibrary("Checks if the sum of two numbers is equal to 8")
test.start()

num1 = 4
num2 = 4
sum = num1 + num2

test.shouldBeEqual(sum, 8)
test.stop()