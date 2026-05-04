class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x = list(s)
        y = list(t)
        if (len(x)!= len(y)):
            return False
        x.sort()
        y.sort()

        cnt = 0
        for i in range (len(x)):
            if (x[i] == y[i]):
                cnt+=1
        if cnt == len(x):
            return True
        return False

        