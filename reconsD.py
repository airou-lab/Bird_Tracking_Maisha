import cv2
import numpy as np

def calibrate_camera(images, chessboard_size):
    obj_points = []  # 3D points in real world space
    img_points = []  # 2D points in image plane

    # Prepare 3D points of the chessboard corners (assuming a flat surface)
    objp = np.zeros((chessboard_size[0] * chessboard_size[1], 3), np.float32)
    objp[:, :2] = np.mgrid[0:chessboard_size[0], 0:chessboard_size[1]].T.reshape(-1, 2)

    for image_path in images:
        img = cv2.imread(image_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Find chessboard corners
        ret, corners = cv2.findChessboardCorners(gray, chessboard_size, None)

        if ret:
            obj_points.append(objp)
            img_points.append(corners)

    _, camera_matrix, distortion_coefficients, _, _ = cv2.calibrateCamera(
        obj_points, img_points, gray.shape[::-1], None, None
    )

    return camera_matrix, distortion_coefficients

def reconstruct_3d_point_cloud(images, camera_matrix, distortion_coefficients):
    obj_points = []  # 3D points in real world space
    img_points = []  # 2D points in image plane

    for image_path in images:
        img = cv2.imread(image_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Find chessboard corners
        ret, corners = cv2.findChessboardCorners(gray, chessboard_size, None)

        if ret:
            obj_points.append(objp)
            img_points.append(corners)

    # Triangulate points
    _, R, T, inliers = cv2.solvePnPRansac(
        np.array(obj_points), np.array(img_points), camera_matrix, distortion_coefficients
    )

    # Project points to 3D
    points_3d = cv2.projectPoints(obj_points, R, T, camera_matrix, distortion_coefficients)[0]

    return points_3d

# Example usage
images = ["24.png", "25.png"]  # Replace with your image paths
chessboard_size = (7, 6)  # Adjust based on your chessboard

# Calibrate the camera
camera_matrix, distortion_coefficients = calibrate_camera(images, chessboard_size)

# Reconstruct the 3D point cloud
point_cloud = reconstruct_3d_point_cloud(images, camera_matrix, distortion_coefficients)

print("Reconstructed 3D Point Cloud:", point_cloud)

