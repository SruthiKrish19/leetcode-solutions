class Solution:
    def vowelStrings(self, words, queries):
        prefix = []
        output = []
        count = 0

        def isVowel(str):
            return str in 'aeiou'

        for word in words:
            if isVowel(word[0]) and isVowel(word[-1]):
                count += 1
            prefix.append(count)

        for query in queries:
            l, r = query
            if l == 0:
                output.append(prefix[r])
            else:
                output.append(prefix[r] - prefix[l - 1])

        return output
      
