# Problem 1184


class Solution:
    def distance_between_bus_stops(
        distance: list[int], start: int, destination: int
    ) -> int:
        whole_circle = sum(distance)
        distance_between = 0

        for i in range(min(start, destination), max(start, destination)):
            distance_between += distance[i]

        return (
            distance_between
            if distance_between < whole_circle - distance_between
            else whole_circle - distance_between
        )


if __name__ == "__main__":
    result = Solution.distance_between_bus_stops([7, 6, 3, 0, 3], 0, 3)
    print(result)  # output: 3
