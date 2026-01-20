class Solution:
    def longestCommonPrefix(self, strs:list[str]) -> str:
        # Initialize prefix with the first string
        pref = strs[0]
        # Initialize prefix length
        pref_len = len(pref)

        # Iterate through the remaining strings
        for s in strs[1:]:
            # Compare prefix with current string
            while pref != s[0:pref_len]:
                # Reduce prefix length
                pref_len -= 1 
                # If prefix becomes empty
                if pref_len == 0:
                    return ""
                # Update prefix
                pref = pref[0:pref_len]
        # Return the longest common prefix
        return pref
    

q = Solution()
print(q.longestCommonPrefix(["flower","flow","flight"]))
print(q.longestCommonPrefix(["dog","racecar","car"]))