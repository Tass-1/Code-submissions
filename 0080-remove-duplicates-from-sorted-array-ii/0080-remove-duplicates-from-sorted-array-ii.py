class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        j = 2
        un = 1
        while j < len(nums):
            if (nums[i] == nums[j]):
                if(nums[i-1] == nums[i]) or nums[i-1] == "po":
                    print(f'{un} aur 3 element rem {nums[i-1]}')
                    print(f'popping {nums[i-1]}')
                    nums[i-1] = "po"
                    i +=1
                    j+=1
                    
                    
                else:
                    un += 1
                    print(f'{un} i and j equal {nums[i]} and {nums[j]}')
                    i += 1
                    j += 1
            elif (nums[i] != nums[j]):
                un += 1
                print(f'{un} i and h unequal {nums[i]} and {nums[j]}')
                i += 1
                j += 1
        l=0
        for i in range(len(nums)):
            
            if str(nums[i])!="po":
                nums[l] , nums[i] = nums[i] , nums[l]
                l+=1
        print(un)
        return un+1

