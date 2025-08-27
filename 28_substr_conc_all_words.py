class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        L = len(words[0])
        total = L * len(words)
        if total > len(s):
            return []

        need = Counter(words)
        res = []

        
        for offset in range(L):
            left = offset
            seen = Counter()
            count = 0 

        
            for right in range(offset, len(s) - L + 1, L):
                w = s[right:right + L]
                if w in need:
                    seen[w] += 1
                    count += 1

                  
                    while seen[w] > need[w]:
                        lw = s[left:left + L]
                        seen[lw] -= 1
                        left += L
                        count -= 1

                   
                    if count == len(words):
                        res.append(left)
                        lw = s[left:left + L]
                        seen[lw] -= 1
                        left += L
                        count -= 1
                else:
                  
                    seen.clear()
                    count = 0
                    left = right + L

        return res