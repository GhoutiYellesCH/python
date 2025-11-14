import numpy as np

def solve_matrix_equation(A, b):
    """
    Résout l'équation matricielle Ax = b.
    
    Args:
        A (numpy.ndarray): La matrice carrée.
        b (numpy.ndarray): Le vecteur.
    
    Returns:
        numpy.ndarray: La solution x, ou None si l'équation n'a pas de solution unique.
    """
    # Vérifier que la matrice A est carrée
    if A.shape[0] != A.shape[1]:
        raise ValueError("La matrice A doit être carrée.")
    
    # Vérifier que les dimensions de A et b sont compatibles
    if A.shape[0] != b.shape[0]:
        raise ValueError("Les dimensions de A et b ne sont pas compatibles.")
    
    # Calculer l'inverse de A
    try:
        A_inv = np.linalg.inv(A)
    except np.linalg.LinAlgError:
        # Si A n'est pas inversible, l'équation n'a pas de solution unique
        return None
    
    # Calculer la solution x = A^-1 * b
    x = np.dot(A_inv, b)
    
    return x
#########################################################################################