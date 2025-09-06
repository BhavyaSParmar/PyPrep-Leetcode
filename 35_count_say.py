class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"
        
        for _ in range(1, n):
            i = 0
            new_result = []
            
            while i < len(result):
                count = 1
               
                while i + 1 < len(result) and result[i] == result[i + 1]:
                    i += 1
                    count += 1
               
                new_result.append(str(count))
                new_result.append(result[i])
                i += 1
            
            result = "".join(new_result)
        
        return result