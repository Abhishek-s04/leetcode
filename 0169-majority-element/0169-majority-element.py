class Solution(object):
    def majorityElement(self, arr):

        count_dict = {}
        for item in arr:
            if item in count_dict:
                count_dict[item] += 1
            else:
                count_dict[item] = 1
            if count_dict[item] > len(arr)//2:
                return item