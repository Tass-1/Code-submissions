class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        cast = sorted(nums)
        for i in range (len(nums)):
            temp = []
            if i > 0 and cast[i] == cast[i - 1]:
                continue
            k = i+1
            j = len(nums) -1
            
            while( k < j):
                
                if( cast[i] + cast[k] + cast[j] == 0):
                    res.append([cast[i], cast[k], cast[j]])
                    
                    while k < j and cast[k] == cast[k + 1]:
                            k = k + 1
                    while k < j and cast[j] == cast[j - 1]:
                            j = j - 1
                    k = k + 1
                    j = j - 1
                
                elif(cast[i] + cast[k] + cast[j] > 0):
                    j = j -1
                else:
                    k = k +1
            


            
            
        return res
        