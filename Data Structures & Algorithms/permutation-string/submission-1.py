class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        s1Count = Counter(s1)
        need = len(s1Count)
        
        for idx in range(len(s2)):      
            have, s2Count = 0, defaultdict(int)
            for jdx in range(idx, len(s2)):
                char = s2[jdx]
                s2Count[char] += 1

                if s1Count[char] < s2Count[char]:
                    break

                if s2Count[char] == s1Count[char]:
                    have += 1
                
                if have == need:
                    return True
        
        return False

            
            
