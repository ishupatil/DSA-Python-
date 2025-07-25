class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        k=k % n
        self.reverse(nums,n-k,n-1)
        self.reverse(nums,0,n-k-1)
        self.reverse(nums,0,n-1)
    
       

    def reverse(self, nums: List[int], left: int, right: int) -> None:
        
        while left < right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
sol=Solution()

sol.rotate(nums,k)
print(nums)
