class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        if len(A) < 3:
            return None; # Invalid case
        if len(A) == 3:
            return A[0]+A[1]+A[2]
        A.sort()
        
        # difference and nearest sum of first 3 elements of the list
        diff = abs(A[0] + A[1] + A[2] - B)
        nearest = A[0] + A[1] + A[2]
        
        # counting the minimum difference using 2 pointer method 
        for a in range(len(A)):
            b = a+1
            c = len(A)-1
            while b < c:
                new = abs(A[a] + A[b] + A[c] - B)
                if new < diff:
                    diff = new
                    nearest = A[a] + A[b] + A[c]
                if A[b]+A[c] < B-A[a]:
                    b += 1
                else:
                    c -= 1
        
        return nearest
