class Solution:
    def define_best(self, start_int : int, nums : list[int], addition=0) -> int:
        if len(nums) == 1: return addition
        if addition == 0:
            for i in range(len(nums)):
                nums[i] = i + nums[i]
        best_option = max(nums)
        best_option_index = len(nums) - nums[::-1].index(best_option) - 1
        if best_option_index == 0 and start_int - best_option == 1:
            return Solution().define_best(start_int - 1, nums[1:], addition + 1)
        return best_option_index + addition
    

    def jump(self, nums: list[int]) -> int:
        if len(nums) == 1: return 0
        i = k = 0
        while True:
            if nums[i] >= len(nums) - i - 1:
                return k + 1
            # print(i, "|", nums[i], nums[i + 1:i + nums[i] + 1], "|", self.define_best(nums[i], nums[i + 1:i + nums[i] + 1]))
            i += self.define_best(nums[i], nums[i + 1:i + nums[i] + 1]) + 1
            k += 1
            if i >= len(nums) - 1:
                return k


print(Solution().jump([7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]))
print(Solution().jump([4,3,2,0,2,1]))