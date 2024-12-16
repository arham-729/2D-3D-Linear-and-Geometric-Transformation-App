import numpy as np

def reflection_matrix_2D(axis):
    if axis == 'x':
        return np.array([[1, 0],
                         [0, -1]])
    elif axis == 'y':
        return np.array([[-1, 0],
                         [0, 1]])
    else:
        return np.identity(2)

def rotation_matrix_2D(angle):
    theta = np.radians(angle)
    return np.array([[np.cos(theta), -np.sin(theta)],
                     [np.sin(theta), np.cos(theta)]])

def translation_matrix_2D(units):
    return np.array([[1, 0, units[0]],
                     [0, 1, units[1]],
                     [0, 0, 1]])



# 3D transformation functions
def reflection_matrix_3D(axis):
    if axis == 'xz':
        return np.array([[1, 0, 0],
                         [0, -1, 0],
                         [0, 0, 1]])
    elif axis == 'yz':
        return np.array([[-1, 0, 0],
                         [0, 1, 0],
                         [0, 0, 1]])
    elif axis == 'xy':
        return np.array([[1, 0, 0],
                         [0, 1, 0],
                         [0, 0, -1]])
    else:
        return np.identity(3)

def rotation_matrix_3D(angle, axis):
    theta = np.radians(angle)
    if axis == 'x':
        return np.array([[1, 0, 0],
                         [0, np.cos(theta), -np.sin(theta)],
                         [0, np.sin(theta), np.cos(theta)]])
    elif axis == 'y':
        return np.array([[np.cos(theta), 0, np.sin(theta)],
                         [0, 1, 0],
                         [-np.sin(theta), 0, np.cos(theta)]])
    elif axis == 'z':
        return np.array([[np.cos(theta), -np.sin(theta), 0],
                         [np.sin(theta), np.cos(theta), 0],
                         [0, 0, 1]])
    else:
        return np.identity(3)

def translation_matrix_3D(units):
    return np.array([[1, 0, 0, units[0]],
                     [0, 1, 0, units[1]],
                     [0, 0, 1, units[2]],
                     [0, 0, 0, 1]])



def main():
    dimension = int(input("Enter 2 for 2D or 3 for 3D transformations: "))

    original_point = list(map(float, input("Enter the point coordinates (separated by spaces): ").split()))
    point = np.array(original_point)

    while True:
        print("\nMenu:")
        print("1. Reflect Point")
        print("2. Rotate Point")
        print("3. Translate Point")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            
            if dimension == 2:
                axis = input("Enter axis to reflect about:")
                reflection = reflection_matrix_2D(axis)
            else:
                axis = input("Enter plane to reflect about:")
                reflection = reflection_matrix_3D(axis)
            point = np.dot(reflection, point)
            print("Point after Reflection:")
            print(point)
        elif choice == '2':
            angle = float(input("Enter angle for rotation: "))
            if dimension == 2:
                rotation = rotation_matrix_2D(angle)
            else:
                axis = input("Enter axis to rotate about (x, y, z): ")
                rotation = rotation_matrix_3D(angle, axis)
            point = np.dot(rotation, point)
            print("Point after Rotation:")
            print(point)
        elif choice == '3':
            units = list(map(float, input("Enter units for translation: ").split()))
            if dimension == 2:
                translation = translation_matrix_2D(units)
            else:
                translation = translation_matrix_3D(units)
            point = np.append(point, 1)  # Convert point to homogeneous coordinates
            point = np.dot(translation, point)
            point = point[:-1]  # Convert back to 2D or 3D coordinates
            print("Point after Translation:")
            print(point)
        elif choice == '4':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please enter a valid option (1-4).")

if __name__ == "__main__":
    main()