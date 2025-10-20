import cv2
import numpy as np
import glob

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

chessboard_size = (9, 6)
objp = np.zeros((chessboard_size[0] * chessboard_size[1], 3), np.float32)
objp[:, :2] = np.mgrid[0:chessboard_size[0], 0:chessboard_size[1]].T.reshape(-1, 2)

objpoints = []  
imgpoints = [] 

img_shape = None

images = glob.glob('calib_images/*.jpg')

for fname in images:
    img = cv2.imread(fname)
    if img is None:
        continue  

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(gray, chessboard_size, None)

    if ret:
        objpoints.append(objp)
        corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        imgpoints.append(corners2)
        
        if img_shape is None:
            img_shape = gray.shape[::-1]  # (width, height)

        cv2.drawChessboardCorners(img, chessboard_size, corners2, ret)
        cv2.imshow('Chessboard Corners', img)
        cv2.waitKey(500)

cv2.destroyAllWindows()

if img_shape is None:
    print("No valid calibration images were found. Check your images and chessboard pattern.")
    exit()

ret, camera_matrix, dist_coeffs, rvecs, tvecs = cv2.calibrateCamera(
    objpoints, imgpoints, img_shape, None, None
)

print("Camera matrix:\n", camera_matrix)
print("Distortion coefficients:\n", dist_coeffs)

np.savez('calibration_data.npz', camera_matrix=camera_matrix, dist_coeffs=dist_coeffs)
