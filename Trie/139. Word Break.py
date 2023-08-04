class Node:
    def __init__(self):
        self.children={}
        self.isword=False # to mark that this is a word. Same as end of word
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root=Node()
      #inserting every word in the dictionary in trie
        for word in wordDict:
            cur=root
            for c in word:
                if c not in cur.children:
                    cur.children[c]=Node()
                cur=cur.children[c]
            cur.isword=True

      #initially every value is false
        dp=[False]*len(s)
        for i in range(len(s)):
          #if first letter not in trie then can just return false
          #if a substring is a word, then need to start again from the root so set cur = root
            if i==0 or dp[i-1]:
                cur=root
                for j in range(i,len(s)):
                    c=s[j]
                    if c not in cur.children:
                        break
                    cur=cur.children[c]
                    if cur.isword:
                        dp[j]=True

        return dp[-1]


O(n^2 + m * k)
