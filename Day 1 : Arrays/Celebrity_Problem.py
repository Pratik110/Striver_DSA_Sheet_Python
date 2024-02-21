def knows(A,B):
    arr  = [A,B]
    knows = [[0,1],[0,2],[0,3],[1,2],[1,0],[1,2],[1,4],[3,1],[3,2],[3,0],[3,4],[4,1]]
    return arr in knows

def findCelebrity(n):
    celeb = [True] * n

    for i in range(n):
        for j in range(n):
            if i!=j and celeb[i]:
                if knows(i,j):
                    celeb[i] = False
    print(celeb)

                



findCelebrity(5)