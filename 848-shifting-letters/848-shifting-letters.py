class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        sum = 0
        new_str = ""

        for i in range(len(shifts)-1, -1 , -1):
            sum += shifts[i]
            new_str = (chr(97 + ((ord(s[i]) + sum - 97) % 26))) + new_str

        return new_str