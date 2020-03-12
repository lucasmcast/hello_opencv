import cv2

def show_message():
    print("Se essa menssagem esta aparecendo, significa que seu pacote foi instalado com sucesso!")

def load_image(path):
    img = cv2.imread(path)
    return img

def show_image(image):
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    

