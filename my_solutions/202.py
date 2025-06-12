class Solution:
    def isHappy(self, n: int) -> bool:
        n_set = set()
        #  Repeat while...
        while n > 1 and n not in n_set:
            #  Add n to the set
            n_set.add(n)
            n = str(n)
            # print(n)
            n =  sum(int(i) ** 2 for i in n)

        if n == 1:
            return True
        else:
            return False
