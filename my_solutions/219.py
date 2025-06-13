class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        temp_dict = {}
        for i in range(len(nums)):
            # print(f"nums[i] = {nums[i]}, temp_dict = {temp_dict}")
            if nums[i] in temp_dict:
                if i - temp_dict[nums[i]] <= k:
                    return True
                else:
                    temp_dict[nums[i]] = i
            else:
                temp_dict[nums[i]] = i
        return False
