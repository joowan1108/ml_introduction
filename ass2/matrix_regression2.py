import numpy as np
np.set_printoptions(precision=4, suppress=True)

#cars
data = np.array([
    [2, 200, 4, 27], 
    [5, 150, 3, 35], 
    [3, 180, 4, 25], 
    [1, 230, 2, 10], 
    [5, 180, 5, 40], 
    [4, 210, 3, 30]  
])

# target
t = np.array([30000, 20000, 25000, 21000, 38000, 31000])

age   = data[:, 0]
hp    = data[:, 1]
brand = data[:, 2]
mpg   = data[:, 3]

# model = w3*(HP/Age) + w2*log(HP) + w1*(Brand*MPG) + w0
phi_3 = hp / age
phi_2 = np.log(hp)
phi_1 = brand * mpg
phi_0 = np.ones_like(age) # Intercept term

Phi = np.column_stack([phi_3, phi_2, phi_1, phi_0])


phi_t = Phi.T
gram = phi_t @ Phi
gram_inv = np.linalg.inv(gram)
weights = gram_inv @ phi_t @ t

print(f"Phi:\n{Phi}\n")
print(f"Phi Transpose:\n{phi_t}\n")
print(f"Phi.T @ Phi:\n{gram}\n")
print(f"Inverse:\n{gram_inv}\n")
print(f"inverse @ transpose: \n{gram_inv @ phi_t}]\n")

print("---  답 ---")
print(f"w3 (HP/Age):      {weights[0]:.4f}")
print(f"w2 (log HP):      {weights[1]:.4f}")
print(f"w1 (Brand * MPG): {weights[2]:.4f}")
print(f"w0 (Intercept):   {weights[3]:.4f}")

