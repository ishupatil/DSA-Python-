class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        mapping={")":"(","}":"{","]":"["}
        for ch in s:
            if ch in mapping.values():
               stack.append(ch)
            elif ch in mapping:
                if not stack or stack.pop()!=mapping[ch]:
                   return False
            else:
                 return False
        return not stack


            
        