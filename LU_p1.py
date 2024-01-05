
def multi_mats(mat1, mat2, row1, col1, row2, col2):

    ans = []
    for i in range(row1):
        c = []
        for j in range(col2):
            s = 0
            for k in range(row2):
                s += (mat1[i][k] * mat2[k][j])
            c.append(s)
        ans.append(c)

    return ans



def inverse_mat_sign(mat, n):

    for i in range(1, n):
        for j in range(i):
            mat[i][j] *= (-1)

    return mat




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

    E1 = inverse_mat_sign(E1, row)
    E2 = inverse_mat_sign(E2, row)

    

    return ans


m1 = [ [1,1,0],
       [2,3,1],
       [1,2,3] ]

m2 = [ [1,4,2],
       [1,1,1],
       [3,1,7] ]

lm = len(m1[0])


a = multi_mats(m1, m2, 3,3,3,3)
print("This is mat: ", a)

print()
for i in range(lm):
    print(a[i])