from collections import Counter

class Solution:
    
    def minimumLength(self, s: str) -> int:
        result = 0

        if len(s) < 3:
            result = len(s)
        else:
            char_count = Counter(s)
            delete_count = 0
            for key in char_count:
                if char_count[key] > 2:
                    if char_count[key] % 2 == 0:
                        delete_count += char_count[key] - 2
                    else:
                        delete_count += char_count[key] - 1

            result = len(s) - delete_count

        return result
