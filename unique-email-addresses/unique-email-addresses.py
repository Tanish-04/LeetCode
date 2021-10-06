class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result = set()
        
        for i in emails:
            localname, domain = i.split('@')
            s = ""
            for j in localname:
                if j == '.':
                    continue
                elif j == '+':
                    break
                else:
                    s += j
                 
                
            result.add(s + "@" + domain)
        
        return len(result)
        