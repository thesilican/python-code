class Solution:
    def canConstruct(self, ransomNote, magazine):
        r = {}
        m = {}
        for c in ransomNote:
            if c not in r:
                r[c] = 1
            else:
                r[c] += 1
        for c in magazine:
            if c not in m:
                m[c] = 1
            else:
                m[c] += 1
        for k in r:
            if k not in m or m[k] < r[k]:
                return False
        return True
