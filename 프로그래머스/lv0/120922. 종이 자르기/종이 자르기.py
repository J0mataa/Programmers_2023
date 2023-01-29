def solution(M, N):
    #접어서 못자름
    # M*N
    ans = 0
    if (M-1)+M*(N-1)==0:
        return 0
    else:
        ans = (M-1)+M*(N-1)
        return ans