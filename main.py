import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_hollow_cylinder_with_cone(outer_radius, inner_radius, height, cone_height, inner_cone_radius, cylinder_radius, small_cylinder_height, num_points=100):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    theta = np.linspace(0, 2 * np.pi, num_points)

    x_outer = outer_radius * np.cos(theta)
    y_outer = outer_radius * np.sin(theta)
    z_outer = np.linspace(0, height, num_points)

    X_outer, Z_outer = np.meshgrid(x_outer, z_outer)
    Y_outer, Z_outer = np.meshgrid(y_outer, z_outer)

    ax.plot_surface(X_outer, Y_outer, Z_outer, alpha=0.5)

    x_inner = inner_radius * np.cos(theta)
    y_inner = inner_radius * np.sin(theta)

    X_inner, _ = np.meshgrid(x_inner, z_outer)
    Y_inner, _ = np.meshgrid(y_inner, z_outer)

    ax.plot_surface(X_inner, Y_inner, Z_outer, alpha=0.5)

    cone_z = height + (cone_height + small_cylinder_height) - np.linspace(0, (cone_height+small_cylinder_height), num_points)
    cone_theta = np.linspace(0, 2 * np.pi, num_points)

    Cone_Z, Cone_Theta = np.meshgrid(cone_z, cone_theta)
    Cone_Radius = np.linspace(inner_radius, outer_radius, num_points)

    X_cone = Cone_Radius * np.cos(Cone_Theta)
    Y_cone = Cone_Radius * np.sin(Cone_Theta)

    ax.plot_surface(X_cone, Y_cone, Cone_Z, alpha=0.5)

    cone_z = height + cone_height - np.linspace(0, cone_height, num_points)
    cone_theta = np.linspace(0, 2 * np.pi, num_points)

    Cone_Z, Cone_Theta = np.meshgrid(cone_z, cone_theta)
    Cone_Radius = np.linspace(inner_cone_radius, inner_radius, num_points)

    X_cone = Cone_Radius * np.cos(Cone_Theta)
    Y_cone = Cone_Radius * np.sin(Cone_Theta)

    ax.plot_surface(X_cone, Y_cone, Cone_Z, alpha=0.5)

    cylinder_height = small_cylinder_height
    cylinder_z = height + cone_height + (small_cylinder_height/2)
    cylinder_theta = np.linspace(0, 2 * np.pi, num_points)

    Cylinder_Z, Cylinder_Theta = np.meshgrid([cylinder_z - cylinder_height / 2, cylinder_z + cylinder_height / 2], cylinder_theta)
    Cylinder_Radius = inner_cone_radius

    X_cylinder = Cylinder_Radius * np.cos(Cylinder_Theta)
    Y_cylinder = Cylinder_Radius * np.sin(Cylinder_Theta)

    ax.plot_surface(X_cylinder, Y_cylinder, Cylinder_Z, alpha=0.5)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()

plot_hollow_cylinder_with_cone(outer_radius=19, inner_radius=11, height=11.5, cone_height=7.5, inner_cone_radius=0.5, cylinder_radius=3, small_cylinder_height=4)
