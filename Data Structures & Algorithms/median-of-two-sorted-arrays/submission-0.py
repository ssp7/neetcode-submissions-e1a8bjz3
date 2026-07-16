class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A
        
        left, right = 0, len(A) - 1

        while True:
            midA = (left + right) // 2
            midB = half - midA - 2

            leftA = A[midA] if midA >= 0 else float("-inf")
            rightA = A[midA + 1] if midA + 1 < len(A) else float("inf")
            leftB = B[midB] if midB >= 0 else float("-inf")
            rightB = B[midB + 1] if midB + 1 < len(B) else float("inf")

            print(leftA, rightA, leftB, rightB)

            if leftA <= rightB and leftB <= rightA:
                if total % 2 == 0:
                    return (max(leftA, leftB) + min(rightA, rightB)) / 2
                else:
                    return min(rightA, rightB)
            elif leftA > rightB:
                right = midA - 1
            else:
                left = midA + 1 

'''
    1 1 2 2 3 4 4 5 6 7 8
    ans = 4
    
    0  1  2  3
A = 1, 1, 2, 4, 

    0  1  2  3  4  5  6
B = 2, 3, 4, 5, 6, 7, 8

total = 11
half = 5

midA = 1
midB = 



'''