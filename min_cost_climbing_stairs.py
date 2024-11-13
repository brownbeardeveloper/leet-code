# Problem #746


class Solution:
    def climb_stairs_min_cost(cost: list[int]) -> int:
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return cost[0] if cost[0] < cost[1] else cost[1]


if __name__ == "__main__":
    result = Solution.climb_stairs_min_cost([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
    print(result)  # output: 6
