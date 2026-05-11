class Solution:
    def moveZeroes(self, arr):

        k = 0
        for i in range(len(arr)):

            if arr[i] != 0:
                arr[k] = arr[i]
                k += 1

        while k < len(arr):
            arr[k] = 0
            k += 1

        return arr