class Solution:
    def isValid(self, s: str) -> bool:
        openingTemp = []
        openings = ['(', '{', '[']

        if len(s) <= 1:
            return False
        elif s[0] not in openings:
            return False
        
        for i in range(len(s)):
            if s[i] in openings:
                openingTemp.append(s[i])
            else:
                if s[i] == '}':
                    if len(openingTemp) == 0:
                        return False
                    else:
                        if openingTemp.pop() == '{':
                            pass
                        else:
                            return False
                elif s[i] == ')':
                    if len(openingTemp) == 0:
                        return False
                    else:
                        if openingTemp.pop() == '(':
                            pass
                        else:
                            return False
                elif s[i] == ']':
                    if len(openingTemp) == 0:
                        return False
                    else:
                        if openingTemp.pop() == '[':
                            pass
                        else:
                            return False

        if len(openingTemp) >= 1:
            return False
        else:
            return True


        