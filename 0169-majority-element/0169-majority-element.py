class Solution(object):
    def majorityElement(self, arr):

        count_dict = {}
        ans = 0
        majority = arr[0]

        for item in arr:

            if item in count_dict:
                count_dict[item] += 1
            else:
                count_dict[item] = 1

            if count_dict[item] > ans:
                ans = count_dict[item]
                majority = item

        return majority