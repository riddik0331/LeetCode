class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        counter = [i for i in counter if counter[i] == 1]
        if counter:
            return s.index(counter[0])
        else:
            return -1


    # def firstUniqChar(self, s: str) -> int:
    #     counter = Counter(s)
    #     for letter, count in counter.items():
    #         if count == 1:
    #             return s.index(letter)
    #     return -1
