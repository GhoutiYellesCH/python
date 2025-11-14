import numpy as np

def determinant(matrix):
    """
    Calcule le déterminant d'une matrice carrée.
    
    Args:
        matrix (numpy.ndarray): La matrice carrée.
    
    Returns:
        float: Le déterminant de la matrice.
    """
    
    if matrix.shape[0] != matrix.shape[1]: # verification
        raise ValueError("La matrice doit etre carree.")
    
    # Calculer le déterminant en utilisant la fonction numpy.linalg.det()
    det = np.linalg.det(matrix)
    
    return det

matrix_1 = np.array([[1, 2], [4, 5 ]])
det1=determinant(matrix_1)
print(det1)
