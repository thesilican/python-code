from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strsF = (("".join(sorted(s)), s) for s in strs)
        d = {}
        for s in strsF:
            if s[0] in d:
                d[s[0]].append(s[1])
            else:
                d[s[0]] = [s[1]]
        output = []
        for key in d:
            output.append(d[key])
        return output


if __name__ == "__main__":
    sol = Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(sol)
