class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_cnt = 0
        cur_cnt = 0
        for e in nums:
            if e == 1:
                cur_cnt += 1
                max_cnt = max(max_cnt,cur_cnt)
            elif e == 0:
                max_cnt = max(max_cnt,cur_cnt)
                cur_cnt = 0
        return max_cnt
