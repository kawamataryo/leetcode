#
# @lc app=leetcode id=1971 lang=python3
#
# [1971] Find if Path Exists in Graph
#

# @lc code=start
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        edge_map = {}
        for num1, num2 in edges:
            if num1 in edge_map:
                edge_map[num1].add(num2)
            else:
                edge_map[num1] = set([num2])
            if num2 in edge_map:
                edge_map[num2].add(num1)
            else:
                edge_map[num2] = set([num1])

        self.result = False
        def traverse(edge: int, visited: Set[int]):
            if edge in visited:
                return
            if destination in edge_map[edge]:
                self.result = True
                return
            visited.add(edge)
            for next_edge in edge_map[edge]:
                traverse(next_edge, visited)

        traverse(source, set([]))

        return self.result

# @lc code=end
