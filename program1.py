# class Solution:
   
#     def getTotalIsles(self, grid: list[list[str]]) -> int:
#     #    write your code here
                    
#         return 0


from typing import List

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        # Your island-counting logic goes here
        # ...

        return 0  # Placeholder value; replace with the actual count

# Example usage:
grid_example = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

solution = Solution()
result = solution.numIslands(grid_example)
print(f"Number of islands: {result}")
