#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        largest=-1
        second=-1
        for i in range(len(arr)):
            if arr[i]>largest:
                largest=arr[i]
        for i in range(len(arr)):
            if arr[i]>second and arr[i]!=largest:
                second=arr[i]
        return second        
        # Code Here


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends