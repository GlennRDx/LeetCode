class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == 0:
            return ''

        prefix = ''
        shortest_string_length = len(min(strs, key=len))
        for i in range(shortest_string_length):
            temp = ''
            for word in strs:
                temp = temp + word[i]
            if len(set(temp)) == 1:
                prefix = prefix + word[i]
            else:
                return prefix
        return prefix
