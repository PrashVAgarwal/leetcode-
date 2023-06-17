class TrieNode:
    def __init__(self):
        self.children={}
        self.count=0
        
class Trie:
    def __init__(self):
        self.root=TrieNode()
        
    def insert(self, lst):
        cur=self.root
        
        for i in lst:
            if i not in cur.children:
                cur.children[i]=TrieNode()
            cur=cur.children[i]
        
        cur.count+=1
        
    def search(self, lst):
        cur=self.root
        
        for i in lst:
            if i not in cur.children:
                return 0
            cur=cur.children[i]
            
        return cur.count
        
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        trie=Trie()
        rows=len(grid)
        cols=len(grid[0])
        
        newgrid=[[0]*cols for _ in range(rows)]
        #print(newgrid)
        for r in range(rows):
            for c in range(cols):
                newgrid[c][r]=grid[r][c]
                
        for r in grid:
            trie.insert(r)
            
        count=0
        
        for r in newgrid:
            count+=trie.search(r)
            
        return count
