class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = 0
        
        for i in range(len(accounts)):
            curr = 0
            for j in range(len(accounts[i])):
                curr += accounts[i][j]
            wealth = max(wealth, curr)
        
        return wealth