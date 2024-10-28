import numpy as np
import matplotlib.pyplot as plt

# Load data
A = np.loadtxt('training_data.txt')
B = np.loadtxt('validation_data.txt')

# Prepare data for training and validation
X = np.hstack((np.ones((A.shape[0], 1)), A[:, [0]], A[:, [0]]**2))
T = A[:, [0]]
C = A[:, [1]]

Xv = np.hstack((np.ones((B.shape[0], 1)), B[:, [0]], B[:, [0]]**2))
Tv = B[:, [0]]
Cv = B[:, [1]]

# Least squares method
v, av, bv = np.linalg.lstsq(X, C, rcond=None)[0]
n_lsq = np.zeros((3, 1))
n_lsq[0][0] = v
n_lsq[1][0] = av
n_lsq[2][0] = bv

# Plot training data and fitted curve
plt.plot(T, X@n_lsq, label='Fitted Curve')
plt.plot(T, C, 'k.', label='Training Data')

# Find corresponding points on the fitted curve for training data
C_fitted = X @ n_lsq

# Plot points with same x-coordinate on fitted curve
for i in range(len(T)):
    x_val = T[i]
    y_val = C_fitted[i]
    plt.plot([x_val, x_val], [C[i], y_val], 'b-', alpha=0.3)  # Blue dashed line

plt.grid()
plt.ylabel('Output Voltage (V)')
plt.xlabel('Temperature ($^{\circ}$C)')
plt.legend()
plt.tight_layout()
plt.savefig('../figs/train.png')
plt.close()

# Plot validation data and fitted curve (similar approach)
plt.plot(Tv, Xv@n_lsq, label='Fitted Curve')
plt.plot(Tv, Cv, 'k.', label='Validation Data')

for i in range(len(Tv)):
    x_val = Tv[i]
    y_val = Xv[i] @ n_lsq
    plt.plot([x_val, x_val], [Cv[i], y_val], 'b-', alpha=0.3)  # Blue dashed line

plt.grid()
plt.ylabel('Output Voltage (V)')
plt.xlabel('Temperature ($^{\circ}$C)')
plt.legend()
plt.tight_layout()
plt.savefig('../figs/valid.png')
