class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)

        for s in strs:
            sorted_str = self.sortStr(s)
            map[sorted_str].append(s) 

        return list(map.values())


    def sortStr(self, s):
        return "".join(sorted(s))
