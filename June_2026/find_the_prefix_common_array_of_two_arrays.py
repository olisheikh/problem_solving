# A = [1,3,2,4]
# B = [3,1,2,4]
# C = []

# for i in range(len(A)):
#     count = 0
#     for j in A[:i + 1]:
#         if j in B[:i+1]:
#             count += 1
            
#     C.append(count)
    
# print(C)

def prefix_array(A, B):
        n = len(A)
        seen = [0] * (n + 1)
        common = 0
        ans = []

        for i in range(n):
            if A[i] == B[i]:
                seen[A[i]] += 2
                common += 1
            else:
                seen[A[i]] += 1
                if seen[A[i]] == 2:
                    common += 1

                seen[B[i]] += 1
                if seen[B[i]] == 2:
                    common += 1

            ans.append(common)

        return ans
    
print(prefix_array(A = [1,3,2,4],B = [3,1,2,4]))
