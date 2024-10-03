from andtlib import AndrewTestingLibrary

test = AndrewTestingLibrary("Tests if ATL for Python is okay")
test.start()

num1 = 4
num2 = 4
sum = num1 + num2

test.shouldBeEqual(sum, 8)
test.shouldBeFalsy(9 == 9)
test.stop()