import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

_x = np.arange(4)
_y = np.arange(3)
_z = np.arange(6)

_xx, _yy, _zz = np.meshgrid(_x, _y, _z)
x, y, z = _xx.ravel(), _yy.ravel(), _zz.ravel()

top = x * y * z
bottom = np.zeros_like(top)
width = depth = height = 1

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

ax.bar3d(x, y, bottom, width, depth, top, shade=True)

ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z axis')

ax.view_init(elev=20., azim=-35)

plt.title('3D Bar Plot with 3D Meshgrid')
plt.tight_layout()
plt.show()