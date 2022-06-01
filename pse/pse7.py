nums = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20],[17,18,19,20]]
r = 3
c = 8
# nums = [[1,2],[3,4]]
# r = 1
# c=4


def reshape_matrix(nums, r, c):
    flat_list = sum(nums, [])
    new_len = len(nums)* len(nums[0])
    if r*c == new_len: 
        return [flat_list[i:i+c]for i in range(0 , new_len, c)]
    else:
        return nums
print(reshape_matrix(nums, r, c))








# 0 -- 4 -- 4
# 0, 1, 2, 3 -> 1, 2, 3, 4


# class Solution:
#     def reshape_matrix(self,nums, r, c):
#         m=len(nums) ; n=len(nums[0]) ; ans=[] ; M=sum(nums, [])
#         if r*c!=m*n: return nums
#         for i in range(0,m*n,c): ans.append(M[i:i+c])
#         return ans

# b = Solution()
# print(b.reshape_matrix(nums, r, c))

# nums = [[1,2],[3,4],[5,6],[7,8]]
# r = 2 
# c = 4


# def reshape_matrix(nums, r, c):
#     w = sum(nums, [])
#     #return list(map(lambda x: nums [c*x:(x+1)*c], range (r)))
#     result =[]
#     i=0
#     while i <(len(w)-(c-1)):
#         result.append(w[i:i+c])
#         i+=c
#     return result
# print(reshape_matrix(nums, r, c))


