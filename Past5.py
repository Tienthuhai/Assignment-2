import numpy as np
import matplotlib.pyplot as plt
import pickle as pkl

# Part A: Load the coords.pkl file
with open('coords.pkl', 'rb') as fh:
    coords = pkl.load(fh)

print("Shape of coords:", coords.shape)  # Should be (296, 2)

# Plotting the coordinates
fig, ax = plt.subplots(figsize=(15, 15))
ax.scatter(coords[:, 0], coords[:, 1], c='blue', s=10)  # Scatter plot
ax.set_title('2D Coordinates')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_aspect(1)  # Equal aspect ratio
plt.grid()
plt.show()

# Part B: Define the transformation functions
def apply_transform(coords, transformation_matrix):
    return coords @ transformation_matrix.T  # Apply transformation using matrix multiplication

# Define transformation matrices
def rotation_matrix(theta):
    return np.array([[np.cos(theta), -np.sin(theta)],
                     [np.sin(theta), np.cos(theta)]])

def scaling_matrix(sx, sy):
    return np.array([[sx, 0],
                     [0, sy]])

def shear_matrix(sh):
    return np.array([[1, sh],
                     [0, 1]])

# Parameters for transformations
theta = np.pi / 4  # 45 degrees rotation
sx, sy = 1.5, 0.5  # Scaling factors
sh = 0.5  # Shear factor

# Apply transformations
rotated_coords = apply_transform(coords, rotation_matrix(theta))
scaled_coords = apply_transform(coords, scaling_matrix(sx, sy))
sheared_coords = apply_transform(coords, shear_matrix(sh))

# Plotting the transformed coordinates
fig, axs = plt.subplots(1, 3, figsize=(20, 7))

axs[0].scatter(rotated_coords[:, 0], rotated_coords[:, 1], c='red', s=10)
axs[0].set_title('Rotated Coordinates')
axs[0].set_aspect(1)

axs[1].scatter(scaled_coords[:, 0], scaled_coords[:, 1], c='green', s=10)
axs[1].set_title('Scaled Coordinates')
axs[1].set_aspect(1)

axs[2].scatter(sheared_coords[:, 0], sheared_coords[:, 1], c='purple', s=10)
axs[2].set_title('Sheared Coordinates')
axs[2].set_aspect(1)

plt.show()

# Part C: Compose transformations
shear_matrix = shear_matrix(0.5)
rotation_matrix = rotation_matrix(np.pi / 6)  # 30 degrees

# Compose transformations
shear_then_rotate = apply_transform(apply_transform(coords, shear_matrix), rotation_matrix)
rotate_then_shear = apply_transform(apply_transform(coords, rotation_matrix), shear_matrix)

# Plotting the composed transformations
fig, axs = plt.subplots(1, 2, figsize=(20, 7))

axs[0].scatter(shear_then_rotate[:, 0], shear_then_rotate[:, 1], c='orange', s=10)
axs[0].set_title('Shear then Rotate')
axs[0].set_aspect(1)

axs[1].scatter(rotate_then_shear[:, 0], rotate_then_shear[:, 1], c='cyan', s=10)
axs[1].set_title('Rotate then Shear')
axs[1].set_aspect(1)

plt.show()
