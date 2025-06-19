class Solution:
    # def summaryRanges(self, nums: List[int]) -> List[str]:
    #     if not nums:
    #         return []
    #     res = []
    #     temp_range = []
    #     for i in range(len(nums) - 1):
    #         temp_range.append(nums[i])
    #         if nums[i + 1] - nums[i] != 1:
    #             if len(temp_range) == 1:
    #                 res.append(str(temp_range[0]))
    #             else:
    #                 res.append(f"{str(temp_range[0])}->{str(temp_range[-1])}")
    #             temp_range = []

    #     temp_range.append(nums[-1])
    #     if temp_range:
    #         if len(temp_range) == 1:
    #             res.append(str(temp_range[0]))
    #         else:
    #             res.append(f"{str(temp_range[0])}->{str(temp_range[-1])}")

    #     return res



    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        res = []
        # temp_range = []
        temp = []
        counter = 0
        for i in range(len(nums) - 1):
            if not temp:
                temp.append(nums[i])
                counter = 0
            if nums[i + 1] - nums[i] != 1:
                if not counter:
                    res.append(str(temp[0]))
                else:
                    res.append(f"{str(temp[0])}->{str(nums[i])}")
                temp = []
            counter += 1

        if not temp:
            res.append(str(nums[-1]))
        else:
            res.append(f"{str(temp[0])}->{str(nums[-1])}")

        return res

                
