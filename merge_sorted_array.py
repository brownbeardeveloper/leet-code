# Problem 88


class Solution:
    def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(len(nums2)):
            nums1[m + i] = nums2.pop(0)
        nums1.sort()


if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [1, 9, 11]
    Solution.merge(nums1=nums1, m=3, nums2=nums2, n=3)
    print(nums1)  # output: [1, 1, 2, 3, 9, 11]
