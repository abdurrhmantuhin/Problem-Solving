class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Converts a Roman numeral string to an integer.
        
        Core idea:
        - Map each Roman symbol to its value
        - Traverse left to right
        - If current value < next value → subtract current (subtractive notation)
        - Otherwise → add current
        - This handles both normal addition and subtraction cases cleanly
        
        Time:  O(n)  → single pass through the string
        Space: O(1)  → fixed-size lookup table
        """
        # Roman symbol to value mapping
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        n = len(s)
        
        for i in range(n):
            # Get current value
            current = roman_values[s[i]]
            
            # If there's a next character and current < next → subtract
            if i + 1 < n and current < roman_values[s[i + 1]]:
                total -= current
            else:
                # Otherwise add
                total += current
        
        return total
    

w = Solution()
print(w.romanToInt("XXXI"))
print(w.romanToInt("I"))
print(w.romanToInt("MMVIII"))