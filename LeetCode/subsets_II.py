import itertools

class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        ans = []
        i=0
        while i < 2**len(nums):
            a = list(map(int, bin(i).split('b')[1]))
            while len(nums)>len(a):
                diff = len(nums)-len(a)
                temp = [0 for i in range(diff)]
                temp.extend(a)
                a=temp
            temp = list(itertools.compress(nums, a))
            if temp not in ans:
                ans.append(temp)
            i+=1
        return ans


if __name__ == "__main__":
    sol = Solution()
    ans1 = sol.subsetsWithDup(nums=[4,4,4,1,4])
    print(ans1)
