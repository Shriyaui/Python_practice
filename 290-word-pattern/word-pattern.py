class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()
        
        # If lengths differ, it's impossible to have a bijection
        if len(pattern) != len(words):
            return False
        
        # Maps for bijection
        char_to_word = {}
        word_to_char = {}
        
        for char, word in zip(pattern, words):
            # Check char -> word mapping
            if char in char_to_word:
                if char_to_word[char] != word:
                    return False
            else:
                char_to_word[char] = word
            
            # Check word -> char mapping
            if word in word_to_char:
                if word_to_char[word] != char:
                    return False
            else:
                word_to_char[word] = char
        
        return True