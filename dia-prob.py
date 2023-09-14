#Diagnostic Problem 1:
#Joseph and Jane are making a contest for apes. During the process, they have to communicate
#frequently with each other. Since they are not completely human, they cannot speak properly.
#They have to transfer messages using postcards of small sizes.
#To save space on the small postcards, they devise a string compression algorithm:
#● If a character occurs n times in a row, then it will be represented by {char}{n} where {n} is
#the value of occurrence. For example, if the substring is a sequence of 'a' ("aaaa"), it will
#be represented as "a4".
#● If a character occurs exactly one time in a row, then it will be simply represented as the
#character itself. For example, if the substring is "a", then it will be represented as "a".
#Help Joseph to compress a message, msg.
#Input
#The only line of input contains a string, msg.
#Output
#Print the string msg as a compressed message.
#Constraints
#● 1 >= length(msg)
#● Msg consists of lowercase English letters (a-z) only
#ample Input#1
#abcaaabbb
#Sample Output#1
#abca3b3
#Sample Input#2
#abcd
#Sample Output#2
#abcd

def solve(s):
   res = ""
   count = 1
   for i in range(1, len(s)):
      if s[i - 1] == s[i]:
         count += 1
      else:
         res = res + s[i - 1]
         if count > 1:
            res += str(count)
         count = 1
   res = res + s[-1]
   if count > 1:
      res += str(count)
   return res

s = "abcaaabbb"
print(solve(s))
s = "abcd"
print(solve(s))