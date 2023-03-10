def solution(A, B):
    N = len(A)
    count = 0
    end = -1
    for i in range(N):
        if A[i] > end:
            count += 1
            end = B[i]
    return count
