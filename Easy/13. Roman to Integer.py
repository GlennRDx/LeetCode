class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        subtractions = {
        'IV' : 4,
        'IX' : 9,
        'XL' : 40,
        'XC' : 90,
        'CD' : 400,
        'CM' : 900
        }

        for key in subtractions.keys():
            if key in s:
                count = s.count(key)
                total += subtractions[key] * count
                s = s.replace(key, "")

        for char in s:
            if char == 'I':
                total += 1
            elif char == 'V':
                total += 5
            elif char == 'X':
                total += 10
            elif char == 'L':
                total += 50
            elif char == 'C':
                total += 100
            elif char == 'D':
                total += 500
            elif char == 'M':
                total += 1000
            
        return total
