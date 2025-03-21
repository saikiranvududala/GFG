#User function Template for python3

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        n=len(arr)
        d=d%n
        self.reverseArray(arr,0,d-1)
        self.reverseArray(arr,d,n-1)
        self.reverseArray(arr,0,n-1)
        
        #Your code here
    def reverseArray(self,arr,left,right):
        while left<right:
            arr[left],arr[right]=arr[right],arr[left]
            left +=1
            right -=1
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())

    while (T > 0):
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ob.rotateArr(A, D)

        for i in A:
            print(i, end=" ")

        print()

        T -= 1

        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends