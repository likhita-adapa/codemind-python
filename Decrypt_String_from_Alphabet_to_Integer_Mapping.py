class Solution(object):
   def freqAlphabets(self, s):
      m = {}
      x = 'a'
      for i in range(1, 27):
         m[str(i)] = x
         x = chr(ord(x) + 1)
      ans = ""
      m['']=''
      i = len(s) - 1
      while i >= 0:
         if s[i] == "#":
            temp = ""
            for j in range(i - 2, i):
               temp += s[j]
            ans = m[str(temp)] + ans
            i -= 3
         else:
            ans = m[s[i]] + ans
            i -= 1
      return ans
ob1 = Solution()
print(ob1.freqAlphabets(input()))