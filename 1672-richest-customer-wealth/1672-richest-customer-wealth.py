class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = 0
        
        for bank_set in accounts:
            wealth = max(wealth, sum(bank_set))
        
        return wealth