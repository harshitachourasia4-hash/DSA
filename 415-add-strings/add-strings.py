class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i=len(num1)-1
        j=len(num2)-1
        ans=""
        carry=0
        while i>=0 or j>=0 or carry>0:
            total=carry
            if i>=0:
                total+=ord(num1[i])-ord('0')
                i-=1
            if j>=0:
                total+=ord(num2[j])-ord('0')
                j-=1
            carry=total//10
            ans+=str(total%10)
          
        return ans[::-1]
            





