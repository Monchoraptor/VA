import argparse
import cv2
import numpy as np
import Imagen

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description='Trains and executes a given detector over a set of testing images')
    parser.add_argument(
        '--detector', type=str, nargs="?", default="", help='Detector string name')
    parser.add_argument(
        '--train_path', default="", help='Select the training data dir')
    parser.add_argument(
        '--test_path', default="", help='Select the testing data dir')

    args = parser.parse_args()

    # Load training data

    imagen = Imagen.Imagen(cv2.imread('./Images/test/00403.jpg'))
    imagen.analizarImagen(cv2.MSER_create(4, 60, 3000, 0.15, 0.2, 200, 1.01, 0.003, 5))
    original = imagen.__copy__()
    imagen.marcar_puntos()
    cv2.imshow('Imagen', imagen.archivo)


    # imagen = cv2.imread('./Images/test/00403.jpg')
    # original = imagen.copy()
    # gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)                     #https://techtutorialsx.com/2018/06/02/python-opencv-converting-an-image-to-gray-scale/
    #
    # scale_percent = 80  # percent of original size                     #https://www.tutorialkart.com/opencv/python/opencv-python-resize-image/
    # width = int(imagen.shape[1] * scale_percent / 100)
    # height = int(imagen.shape[0] * scale_percent / 100)
    # dim = (width, height)
    #
    # mser = cv2.MSER_create(4, 60, 3000, 0.15, 0.2, 200, 1.01, 0.003, 5)                                         #https://answers.opencv.org/question/19015/how-to-use-mser-in-python/
    # mser_areas = mser.detect(gris, None)
    # print(f'Número de puntos clave: {len(mser_areas):,}')               #https://datasmarts.net/es/como-usar-el-detector-de-puntos-clave-mser-en-opencv/
    # for keypoint in mser_areas:
    #     radius = int(0.5 * keypoint.size)
    #     x, y = np.int64(keypoint.pt)
    #     # cv2.rectangle(imagen, ((x-(keypoint.size*0.5),(y-(keypoint.size*0.5)))), (x+(keypoint.size*0.5),(y+(keypoint.size*0.5))), (0, 255, 255), 2)
    #     cv2.circle(imagen, (x, y), radius, (0, 255, 255), 2)
    # resized = cv2.resize(imagen, dim, interpolation=cv2.INTER_AREA)
    # resizedgris = cv2.resize(gris, dim, interpolation=cv2.INTER_AREA)
    # resizedor = cv2.resize(original, dim, interpolation=cv2.INTER_AREA)
    # cv2.imshow('Imagen', resized)
    # cv2.imshow('Original', resizedor)
    # # cv2.imshow('Gris', resizedgris)
    # cv2.waitKey(0)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # Create the detector

    # Load testing data

    # Evaluate sign detections





