# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()
        pass

    def match(self, word_list):
        anagrams = []

        for candidate in word_list:
            if self._is_anagram(candidate):
                anagrams.append(candidate)

        return anagrams        
        
    def _is_anagram(self, candidate):
        candidate_lower = candidate.lower()

        if candidate_lower == self.word:
            return False
        
        return sorted(candidate_lower) == sorted(self.word)
    pass

