from sklearn import datasets, svm
from skimage.feature import hog
import cv2

# Load digit dataset
digits = datasets.load_digits()
features = [hog(img, pixels_per_cell=(4, 4), cells_per_block=(2, 2)) for img in digits.images]

# Train SVM
clf = svm.SVC()
clf.fit(features, digits.target)

# Predict from image
img_path = input("Enter image path:\n> ").strip()
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (8, 8))
hog_feat = hog(img, pixels_per_cell=(4, 4), cells_per_block=(2, 2))
print("Predicted Digit:", clf.predict([hog_feat])[0])
