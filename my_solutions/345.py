class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        s_list = list(s)
        start = 0
        end = len(s) - 1
        while start < end:
            while start < end and s[start] not in vowels:
                start += 1
            while start < end and s[end] not in vowels:
                end -= 1
            if s[start] in vowels and s[end] in vowels:
                s_list[start], s_list[end] = s_list[end], s_list[start]
            start += 1
            end -= 1
        
        return ''.join(s_list)
