#MIT License

#Copyright (c) 2024 AndrewNation

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

class AndrewTestingLibrary:
    def __init__(self, label):
        self.label = label
        self.testFailure = False
        self.report = []

    def __intro(self):
        print("🧪 Andrew Testing Library for Python - ALPHA")
        print("Initializing tests...")
        print("Running test suit \"" + self.label + "\"")

    def start(self):
        self.__intro()

    def stop(self):
        if not self.testFailure:
            print("✅ All tests passed!")
        else:
            print("❌ One or more tests failed")

        if len(self.report) > 0:
            i = 0
            while i < len(self.report):
                print(self.report[i])
                i = i + 1

    def __failTest(self):
        self.testFailure = True
        pass

    def __passTest(self):
        if not self.testFailure:
            self.testFailure = False
        else:
            return
        pass

    def __compare(self, expr, msgIfErr):
        if expr:
            self.__passTest()
        else:
            self.__failTest()
            self.report.append("Expected " + msgIfErr)

    def shouldBeEqual(self, arg1, arg2):
        self.__compare(arg1 == arg2, str(arg1) + " to be equal to " + str(arg2))

    def shouldBeGreaterThan(self, arg1, arg2):
        self.__compare(arg1 > arg2, str(arg1) + " to be greater than " + str(arg2))

    def shouldBeGreaterOrEqual(self, arg1, arg2):
        self.__compare(arg1 > arg2 or arg1 == arg2, str(arg1) + " to be greater than or equal to " + str(arg2))

    def shouldBeLessThan(self, arg1, arg2):
        self.__compare(arg1 < arg2, str(arg1) + " to be less than " + str(arg2))

    def shouldBeLessOrEqual(self, arg1, arg2):
        self.__compare(arg1 < arg2 or arg1 == arg2, str(arg1) + " to be less than or equal to " + str(arg2))

    def shouldNotBeEqual(self, arg1, arg2):
        self.__compare(not (arg1 == arg2), str(arg1) + " not to be equal to " + str(arg2))
        pass

    def shouldBeStrictEqual(self, arg1, arg2):
        self.__compare(type(arg1) == type(arg2), "the two values aren't exactly the same")

    def shouldBeNull(self, expr):
        self.__compare(expr == None, str(expr) + " to be null")

    def shouldNotBeNull(self, expr):
        self.__compare(not(expr == None), str(expr) + " not to be null")

    def shouldBeTruthy(self, expr):
        self.__compare(expr == True, str(expr) + " to be truthy")

    def shouldBeFalsy(self, expr):
        self.__compare(expr == False, str(expr) + " not to be falsy")

    #for objects
    def shouldBeTheSame(self, arr1, arr2):
        """
        It compares two lists and checks if all their values are the same.
        arr1 -- the first list
        arr2 -- the second list
        """
        i = 0
        areListsEqual = True
        while i < len(arr1) and i < len(arr2):
            if not arr1[i] == arr2[i]:
                areListsEqual = False
                break
            i = i + 1

        if areListsEqual:
            self.__passTest()
        else:
            self.__compare(areListsEqual, "the lists are not the same")

    def triggerFail(self, errCode):
        self.__failTest()
        self.report.append(errCode)