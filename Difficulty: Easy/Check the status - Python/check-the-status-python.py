class Solution:
    def checkStatus(self, a, b, flag):
        # code hereclass Solution:
        return (flag and a < 0 and b < 0) or (not flag and ((a >= 0 and b < 0) or (a < 0 and b >= 0)))
        