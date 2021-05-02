# User function Template for python3

class Solution:
    def minRepeats(self, A, B):
        # code here
        i = 0
        while i < len(A):
            if A[i] == B[0]:
                break;
            else:
                i += 1
        if i == len(A):
            return -1
        temp = list(A)
        count = 1
        j = 0
        while j < len(B):
            if j + i >= len(temp):
                temp.extend(list(A))
                count += 1
            if temp[j + i] == B[j]:
                j += 1
            else:
                return -1
        if j == len(B):
            return count


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        A = input()
        B = input()

        ob = Solution()
        print(ob.minRepeats(A, B))
# } Driver Code Ends


