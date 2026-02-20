def isPalindrome(self, s: str) -> bool:
        calm_s = "".join(c.lower() for c in s if c.isalnum())
        return calm_s == calm_s[::-1]

# Example usage
input_string = "A man, a plan, a canal: Panama"
print(isPalindrome(None, input_string))
# Output: True
        