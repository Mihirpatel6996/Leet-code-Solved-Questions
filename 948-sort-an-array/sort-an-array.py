class Solution:
    @staticmethod
    def split(arr,low,high):
        if low>=high:
            return

        mid = (low+high)//2

        Solution.split(arr,low,mid)
        Solution.split(arr,mid+1, high)
        Solution.merge(arr,low,mid,high)

    @staticmethod
    def merge(arr,low,mid,high):
        temp = []
        left, right = low, mid+1
        while left <= mid and right<=high:
            if(arr[left] <= arr[right]):
                temp.append(arr[left])
                left+=1
            else:
                temp.append(arr[right])
                right+=1
        
        # Bache hue elements
        while left <= mid:
            temp.append(arr[left])
            left += 1
        while right <= high:
            temp.append(arr[right])
            right += 1

        for i in range(low, high+1):
            arr[i] = temp[i-low]
        return        



        
    def sortArray(self, nums: list[int]) -> list[int]:
        Solution.split(nums,0,len(nums)-1)
        return nums
        