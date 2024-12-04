class Solution:
    def remove_element(nums: list[int], val: int) -> int:
        write_index, read_index = 0, 0

        while read_index <= len(nums)-1:
            if nums[read_index] != val:
                nums[write_index], nums[read_index] = nums[read_index], nums[write_index]
                write_index +=1
                read_index +=1
            else:
                nums[read_index] = "_"
                read_index +=1
        return write_index

if __name__ == "__main__":
    nums_list = [0,1,2,2,3,0,4,2]
    result = Solution.remove_element(nums=nums_list, val=2)
    print(result) # output: 5
    print(nums_list) # output: [0, 1, 3, 0, 4, '_', '_', '_']
