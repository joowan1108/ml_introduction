import numpy as np
np.set_printoptions(precision=4, suppress=True)

x = np.array([-1, 0, 1, 1])
t = np.array([1, 1, 1, 0])

def solve_regression(Phi, t):
    # w = (Phi^T * Phi)^-1 * Phi^T * t
    phi_t = Phi.T
    inverse = np.linalg.inv(Phi.T @ Phi)
    mid_cal = inverse @ phi_t
    print(f"phi \n {Phi}")
    print(f"phi_t \n {phi_t}")
    print(f"Phi.T @ Phi \n {Phi.T @ Phi}")
    print(f"Phi.T @ Phi inverse \n {inverse}")
    print(f"inverse @ phi_t \n {mid_cal}")
    return mid_cal @ t


print("============== A ==============")
# a) f(x) = w1*x + w0
Phi_a = np.column_stack([x, np.ones_like(x)])
w_a = solve_regression(Phi_a, t)
print(f"a) w1: {w_a[0]:.4f}, w0: {w_a[1]:.4f} \n\n\n")


print("============== B ==============")
# b) f(x) = w1*cos(pi*x) + w0
Phi_b = np.column_stack([np.cos(np.pi * x), np.ones_like(x)])
w_b = solve_regression(Phi_b, t)
print(f"b) w1: {w_b[0]:.4f}, w0: {w_b[1]:.4f} \n\n\n")


print("============== C ==============")
# c) f(x) = w2*x^2 + w1*x + w0
Phi_c = np.column_stack([x**2, x, np.ones_like(x)])
w_c = solve_regression(Phi_c, t)
print(f"c) w2: {w_c[0]:.4f}, w1: {w_c[1]:.4f}, w0: {w_c[2]:.4f} \n\n\n")



print("============== D ==============")
# d) f(x) = w2*exp(-(x+1)^2) + w1*exp(-x^2) + w0
Phi_d = np.column_stack([np.exp(-(x+1)**2), np.exp(-x**2), np.ones_like(x)])
w_d = solve_regression(Phi_d, t)
print(f"d) w2: {w_d[0]:.4f}, w1: {w_d[1]:.4f}, w0: {w_d[2]:.4f}")



