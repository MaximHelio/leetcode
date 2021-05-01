class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l1 = list(input())
        l1.sort(reverse=True)
        l1_int = "".join(l1)
        l2 = list(input())
        l2.sort(resverse=True)
        l2_int = "".join(l2)
        result = l1_int + l2_int
        list(result)
