import cv2
import numpy as np


class Imagen:

    def __init__(self, archivo):
        self.archivo = archivo

    def analizarImagen(self, mser):
        self.gris = cv2.cvtColor(self.archivo, cv2.COLOR_BGR2GRAY)
        self.mser = mser
        self.mser_areas = mser.detect(self.gris, None)

    def __copy__(self):
        nueva_imagen = Imagen(self.archivo)
        if self.mser!=None:
            nueva_imagen.gris = self.gris
            nueva_imagen.mser = self.mser
            nueva_imagen.mser_areas = self.mser_areas
        return nueva_imagen;

    def marcar_puntos(self):
        imagen_copia = Imagen.__copy__(self)
        print(
            f'Número de puntos clave: {len(imagen_copia.mser_areas):,}')  # https://datasmarts.net/es/como-usar-el-detector-de-puntos-clave-mser-en-opencv/
        for keypoint in imagen_copia.mser_areas:
            radius = int(0.5 * keypoint.size)
            x, y = np.int64(keypoint.pt)
            # cv2.rectangle(imagen, ((x-(keypoint.size*0.5),(y-(keypoint.size*0.5)))), (x+(keypoint.size*0.5),(y+(keypoint.size*0.5))), (0, 255, 255), 2)
            cv2.circle(imagen_copia.archivo, (x, y), radius, (0, 255, 255), 2)