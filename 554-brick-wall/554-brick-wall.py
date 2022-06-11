class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
      _map = {}
      # lines = 0
      #find number of possible lines
      # for num in wall[0]:
        # lines += num
      # lines -= 1
      
      for row in wall:
        cum_sum = 0
        for b in row[:-1]:
            cum_sum += b
            _map[cum_sum] = _map.get(cum_sum, 0) + 1

      if not _map:
          return len(wall)
      return len(wall) - max(_map.values())