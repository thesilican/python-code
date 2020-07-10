class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        possible_answers = []
        n_pos = 0
        running_sum = 0
        # prev_num = nums[0]

        for i, num in enumerate(nums):
            if i==0:
                running_sum += num
                if num > 0:
                    current_min = 0
                    n_pos += 1
                else:
                    current_min = num
                prev_num = num
                continue

            if prev_num > 0:
                if num > 0:
                    running_sum += num
                    n_pos += 1
                    #keep adding
                    if (i+1) == len(nums):
                        diff = running_sum - current_min
                        possible_answers.append(diff)  
                else:
                    # peak - local max
                    diff = running_sum - current_min
                    possible_answers.append(diff)
                    running_sum += num
            else:
                if num > 0:
                    # valley - local min
                    n_pos += 1
                    if running_sum < current_min:
                        current_min = running_sum
                    running_sum +=num
                    if (i+1) == len(nums):
                        diff = running_sum - current_min
                        possible_answers.append(diff)  
                else:
                    running_sum += num
            prev_num = num
        if n_pos==0 or len(nums)==1:
            return(max(nums))
        return(max(possible_answers))
