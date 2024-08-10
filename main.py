class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = (''.join(str(digits))).replace(',', '').replace('[', '').replace(']', '').replace(' ', '')
        s = int(s) + 1
        return ([int(i) for i in str(s)])

