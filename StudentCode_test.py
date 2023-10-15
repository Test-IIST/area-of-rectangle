import SCOPP_tester;
from IOWrapper import IOWrapper
testIO = IOWrapper()
expectedIO = IOWrapper()
def test_hello():
    testLengths = [5.2, 2, 0, 7.5, 11]
    testWidths = [3.8, 4, 10, 1, 25 ]
    expectedList = [19.76, 8, 0, 7.5,275 ]
    i=0
    for expected in expectedList:
        testLength = testLengths[i] 
        testWidth= testWidths[i]                                                                 # use these lOCs while using list object
        print("Testing: Test case",testLength,testWidth,"Expected",expected)
        #print("Testing: Test case","Expected",expected)
        expectedIO.print(expected)
        assert SCOPP_tester.test(testLength,testWidth ,testIO = testIO,expectedIO = expectedIO)
        #assert SCOPP_tester.test(testIO = testIO,expectedIO = expectedIO)
        i+=1
        print("Test case Passed")
    print("Code is correct.All Test cases passed")