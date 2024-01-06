
# Multiplication of two matrices
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


# Change the sign of the values of a matrix
def inverse_mat_sign(mat, n):

    for i in range(1, n):
        for j in range(i):
            mat[i][j] *= (-1)

    return mat



# Create identity matrix
def identity_mat(n):
    iden_mat = []

    l1 = []
    for i in range(n):
        for j in range(n):
            l1.append(0)
        iden_mat.append(l1)
        l1 = []    

    for i in range(n):
        iden_mat[i][i] = 1
    return iden_mat



# Decompose a matrix into L and U
def LU_t(mat1, row, col):
    zero_val = 0.0

    # create identity matrix (To calculate L)
    E1 = identity_mat(row)
    E2 = identity_mat(row)

    c = True


    # Create an upper triangular matrix (Zeroing of value below the main diameter)    
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
    
    # Answer is an array (U & L)
    ans = []
    ans.append(mat1)

    # Change the sign of the values of a matrix
    E1 = inverse_mat_sign(E1, row)
    E2 = inverse_mat_sign(E2, row)

    # Multiplication of two matrices
    m = multi_mats(E1, E2, row, row, row, row)
    ans.append(m)

    return ans
