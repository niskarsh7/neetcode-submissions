class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=''.join(char for char in s if char.isalnum() ).lower()#Learn To remove space punctuation, numeric etc from string
        if s==s[::-1]:
            return True
        else:
            return False
        