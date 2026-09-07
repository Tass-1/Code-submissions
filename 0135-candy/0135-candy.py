class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) == 1:
            return 1
        nums = [1]*len(ratings)
        for i in range(len(ratings)):
            if i != 0 and i <len(ratings)-1:
                prev = ratings[i-1]
                next = ratings[i+1]
                curr = ratings[i]
                if curr > prev:
                    if nums[i] <= nums[i-1]:
                        nums[i] = nums[i-1] + 1
                if curr > next:
                    if nums[i] <= nums[i+1]:
                        nums[i] = nums[i+1] + 1
                        
                
            elif i == 0:
                print("i 0")
                curr = ratings[i]
                next = ratings[i+1]
                if curr > next:
                    if nums[i] <= nums[i+1]:
                        nums[i] = nums[i+1] + 1
            elif i == len(ratings)-1:
                print("end ")
                curr = ratings[i]
                prev = ratings[i-1]
                if curr > prev:
                    if nums[i] <= nums[i-1]:
                        nums[i] = nums[i-1] + 1
        n = len(ratings)
        for j in range(n-1, -1,-1):
            if j != n-1 and j != 0:
                curr = ratings[j]
                next = ratings[j-1]
                prev = ratings[j+1]
                if curr > prev:
                    if nums[j] <= nums[j+1]:
                        nums[j] = nums[j+1] + 1
                if curr > next:
                    if nums[j] <= nums[j-1]:
                        nums[j] = nums[j-1] + 1
            
            elif j == 0:
                print("i 0")
                curr = ratings[j]
                prev = ratings[j+1]
                if curr > prev:
                    if nums[j] <= nums[j+1]:
                        nums[j] = nums[j+1] + 1
            elif i == len(ratings)-1:
                print("end ")
                curr = ratings[i]
                next = ratings[i-1]
                if curr > next:
                    if nums[i] <= nums[i-1]:
                        nums[i] = nums[i-1] + 1
        print(nums)
        return sum(nums)

        