from django.shortcuts import render
from typing import List
# Create your views here.


def arrays_view(request):
    return render(request, 'arrays/arrays_list.html')


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return


# y = Solution()
# lst = [1, 2, 5, 3]
# print(y.twoSum(lst, 4))


class MaxProfit:
    def max_profit(self, prices: List[int]) -> int:
        left, right = 0, 1
        max_profit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else:
                left = right
            right += 1
        return max_profit


# lst = [3, 7, 9, 5, 3, 1, 2, 4, 7, 6, 10, 8]
# x = MaxProfit()
# print(x.max_profit(lst))


class ProductExceptSelf:
    def product_except_self(self, nums: List[int]) -> List[int]:
        result = [1] * (len(nums))

        prefix = 1
        for idx in range(len(nums)):
            result[idx] = prefix
            prefix *= nums[idx]

        postfix = 1
        for idx in range(len(nums) - 1, -1, -1):
            result[idx] *= postfix
            postfix *= nums[idx]
        return result


# lst = [1, 2, 3, 4]
# y = ProductExceptSelf()
# print(y.product_except_self(lst))

class MaxSubArraySum:
    def max_sum_sub_array(self, nums: List[int]) -> List[int]:
        maxSub = nums[0]
        curSum = 0

        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            maxSub = max(curSum, maxSub)
        return maxSub


# lst = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# y = MaxSubArraySum()
# print(y.max_sum_sub_array(lst))


class MaxSubArrayProduct:
    def max_sub_array_product(self, nums: List[int]) -> List[int]:
        result = max(nums)
        current_max, current_min = 1, 1

        for num in nums:
            if num == 0:
                current_max, current_min = 1, 1
                continue

            temp_max = num * current_max
            current_max = max(current_max * num, current_min * num, num)
            current_min = min(temp_max, current_min * num, num)
            result = max(current_max, result)
        return result


# lst = [2, 3, -1, 5, -2, 4]
# y = MaxSubArrayProduct()
# print(y.max_sub_array_product(lst))


class RotateList:
    def rotate_list_number(self, nums: List[int], n: int) -> List[int]:
        for index in range(n):
            temp = nums[0]

            for idx in range(len(nums) - 1):
                nums[idx] = nums[idx + 1]
            nums[len(nums) - 1] = temp
        return nums

    def find_min_sort_list(self, nums: List[int]) -> List[int]:
        result = min(nums)
        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] < nums[right]:
                result = min(result, nums[left])

            mid_point = (left + right) // 2
            result = min(result, nums[mid_point])
            if nums[mid_point] >= nums[left]:
                left = mid_point + 1
            else:
                right = mid_point - 1
        return result

    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid_point = (left + right) // 2

            if target == nums[mid_point]:
                return mid_point

            if nums[left] <= nums[mid_point]:
                if target < nums[left] or target > nums[mid_point]:
                    left = mid_point + 1
                else:
                    right = mid_point - 1
            else:
                if target > right or target < nums[mid_point]:
                    right = mid_point - 1
                else:
                    left = mid_point + 1
        return -1


# lst = [4, 5, 6, 7, 0, 1, 2]
lst = [4, 5, 6, 7, 0, 1, 2]

# lst = [0, 3, 4, 5, 6, 8, 9, 10, 13]
obj = RotateList()
# y = obj.rotate_list_number(lst, 0)
x = obj.search(lst, 7)
print(x)
# print(x)
# Find Minimum in Rotated Sorted Array - Binary Search
