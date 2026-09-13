class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            curr = numbers[i]
            diff = target - curr
            left = i+1
            right = len(numbers)-1
            
            while left <= right:
                mid = left + ((right - left)//2)
                if numbers[mid] == diff:
                    return [i+1,mid+1]
                    break
                elif numbers[mid] > diff:
                    right = mid -1
                elif numbers[mid] < diff:
                    left = mid + 1
            