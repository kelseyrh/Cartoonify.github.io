def lines(img):
    gray = cv2.bilateralFilter(img, 15, 80, 80)
    #sigma 0.2 low 0.1 high 0.3
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    sobelx = cv2.Sobel(gray,cv2.CV_64F,1,0,ksize=5)
    sobely = cv2.Sobel(gray,cv2.CV_64F,0,1,ksize=5)
    #energyImage = sobelx ** 2 + sobely ** 2
    #energyImage = np.sqrt(energyImage)
    energyImage = abs(sobelx) + abs(sobely)
    energyImage = energyImage / np.amax(energyImage)
    idx = energyImage[:,:] < 0.2
    img[idx] = [0, 0, 0]
    
    return img

img = imread('res\images\chair.jpg')
img = lines(img)
plt.imshow(img, cmap='gray')
plt.show()
img = imread('res\images\city.jpg')
img = lines(img)
plt.imshow(img, cmap='gray')
plt.show()