class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(char.lower() for char in s if char.isalnum())
        for i in range (len(cleaned)):
            if i != 0:
                if cleaned[i] != cleaned[-(i+1)]:
                    return False
            if i == 0:
                if cleaned[i] != cleaned[-1]:
                    return False
        return True