
def identity_mat(n):
    iden_mat = []

    l1 = []
    for i in range(n):
        for j in range(n):
            l1.append(0)
        iden_mat.append(l1)
        l1 = []    

    for i in range(n): # this is again work, fix that or find a way to better time it!
        iden_mat[i][i] = 1
    return iden_mat

def LU_t(mat1, row, col):
    zero_val = 0.0

    E1 = identity_mat(row)
    E2 = identity_mat(row)
    c = True

    for k in range(col):
        for i in range(k, row-1):            
            zero_val = (mat1[i+1][k] / mat1[k][k]) * (-1)
            
            if c==True:
                E1[i+1][k] = zero_val
            elif c==False:
                E2[i+1][k] = zero_val

            for j in range(col):
                mat1[i+1][j] += zero_val * mat1[k][j]
        c = False
    
    ans = []
    ans.append(mat1)

    print("E1: ", E1)
    print("E2: ", E2)

    return ans


m1 = [ [1,1,0],
       [2,3,1],
       [1,2,3] ]

lm = len(m1[0])

print("iden mat in main: ", LU_t(m1, lm, lm))