class Solution(object):
    def reverseVowels(self, s):
        vowels = "aeiouAEIOU"

        # Store all vowels
        v = []
        for ch in s:
            if ch in vowels:
                v.append(ch)

        # Reverse vowels
        v.reverse()

        result = ""
        i = 0

        for ch in s:
            if ch in vowels:
                result += v[i]
                i += 1
            else:
                result += ch

        return result