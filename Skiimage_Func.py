from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap, QGuiApplication
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QApplication
import numpy as np
import os
from skimage.color import rgb2gray,rgb2hsv
from skimage.filters import sobel, prewitt, scharr, roberts
from skimage.segmentation import chan_vese
from skimage import io
from skimage.filters import threshold_multiotsu
from skimage import morphology, segmentation
from skimage.segmentation import (morphological_chan_vese,
                                  morphological_geodesic_active_contour,
                                  inverse_gaussian_gradient,
                                  checkerboard_level_set)

from Common_Proc import Common_Proc

class Skiimage_Functions(Common_Proc):
    
    def __init__(self):
        super().__init__()
        
        
        
    def Skiimage_RGB2HSV(self):
        """
        This method takes the RGB raw image and convert it to HSV

        Returns
        -------
        None.

        """
        self.Button_Output_Undo.setEnabled(True)
        self.actionUndo_Output.setEnabled(True)
        
        self.set_image(io.imread(self.get_file_name()))
        # self.image =io.imread(self.file_name)
        #png eklemek için
        self.image=self.image[:,:,:3]
        
        
        hsv_img = rgb2hsv(self.get_image())
        
        #datayı 0-1 den 255e rescale ve data type düzenleme
        image_array = (hsv_img * 255).astype(np.uint8)
        
        self.prev_image.append(image_array)
        
        qimage = QImage(image_array.data, hsv_img.shape[1], hsv_img.shape[0], hsv_img.shape[1] * 3 , QImage.Format_RGB888)

       #siyah beyaz GrayScale16
        

        result = QPixmap.fromImage(qimage)
        print(type(result))
        
        self.previous_output.append(result)
        print(type(self.get_previous_output()))
        
    def Source_gray(self):
        """
        This method takes the RGB raw image and convert it to GrayScale

        Returns
        -------
        None.

        """
        self.set_image(io.imread(self.get_file_name()))
        #png eklemek için
        self.image=self.image[:,:,:3]
        grayscale = rgb2gray(self.image)
        
        return grayscale
        
        
    def Skiimage_RGB2Gray(self):
        """
        This method takes the RGB raw image and convert it to HSV

        Returns
        -------
        None.

        """
        self.Button_Output_Undo.setEnabled(True)
        self.actionUndo_Output.setEnabled(True)
        
        
        grayscale = self.Source_gray()
        
        image_array = (grayscale * 255).astype(np.uint8)
        
        self.prev_image.append(image_array)
        
        qimage = QImage(image_array.data, grayscale.shape[1], grayscale.shape[0], grayscale.shape[1] , QImage.Format_Grayscale8)

        result = QPixmap.fromImage(qimage)
        print(type(result))
        
        self.previous_output.append(result)
        print(type(self.previous_output))
    
    
    
    def Skiimage_Chan_Vese(self):
        """
        This method takes the RGB raw image and convert it to GrayScale then apply the Chan_Cese method

        Returns
        -------
        None.

        """
        
        self.Button_Output_Undo.setEnabled(True)
        self.actionUndo_Output.setEnabled(True)
        
        grayscale = self.Source_gray()
        
        
        print("118 img -> "+str(type(grayscale)))
        
        
        cv = chan_vese(grayscale, mu=0.25, lambda1=1, lambda2=1, tol=1e-3,
                max_num_iter=100, dt=0.5, init_level_set="checkerboard",
                extended_output=True)
        
        temp = cv[0]
        chan_vesee = (temp * 255).astype(np.uint8)
        
        self.prev_image.append(chan_vesee)
        
        qimage = QImage(chan_vesee.data, chan_vesee.shape[1], chan_vesee.shape[0], chan_vesee.shape[1] , QImage.Format_Grayscale8)

        result = QPixmap.fromImage(qimage)
        print(type(result))
        
        self.previous_output.append(result)
        
        print("119 cv[0] -> "+str(type(cv[0])))
        print("119 cv[1] -> "+str(type(cv[1])))
        print("119 cv[2] -> "+str(type(cv[2])))
    
    def Skiimage_Otsu(self):
        """
        This method takes the RGB raw image and convert it to GrayScale then apply the Otsu method

        Returns
        -------
        None.

        """
        
        self.Button_Output_Undo.setEnabled(True)
        self.actionUndo_Output.setEnabled(True)
        
        grayscale = self.Source_gray()
        
        thresholds = threshold_multiotsu(grayscale)
        
        regions = np.digitize(grayscale, bins=thresholds)
        
        otsu = (regions * 255).astype(np.uint8)
        
        self.prev_image.append(otsu)
        
        qimage = QImage(otsu.data, otsu.shape[1], otsu.shape[0], otsu.shape[1] , QImage.Format_Grayscale8)

        result = QPixmap.fromImage(qimage)
        print(type(result))
        
        self.previous_output.append(result)
        
    
    
    def store_evolution_in(self,lst):
        """
        Returns a callback function to store the evolution of the level sets in
        the given list.
        """

        def _store(x):
            lst.append(np.copy(x))

        return _store
    
   
    def Skiimage_Morp_Snake(self):
        """
        This method takes the RGB raw image and convert it to GrayScale then apply the Morphological Snakes method

        Returns
        -------
        None.

        """
        
        self.Button_Output_Undo.setEnabled(True)
        self.actionUndo_Output.setEnabled(True)
        
        grayscale = self.Source_gray()
        
        # Initial level set
        init_ls = checkerboard_level_set(grayscale.shape, 6)
        # List with intermediate results for plotting the evolution
        evolution = []
        callback = self.store_evolution_in(evolution)
        ls = morphological_chan_vese(grayscale, num_iter=35, init_level_set=init_ls,
                                     smoothing=3, iter_callback=callback)
        
        image = (ls * 255).astype(np.uint8)
        
        self.prev_image.append(image)
        
        qimage = QImage(image.data, image.shape[1], image.shape[0], image.shape[1] , QImage.Format_Grayscale8)
        print(type(image))
        result = QPixmap.fromImage(qimage)
        print(type(result))
        
        self.previous_output.append(result)
    
    def Skiimage_Scharr(self):
        """
        This method takes the RGB raw image and convert it to GrayScale then apply the Skiimage_Scharr method

        Returns
        -------
        None.

        """
       
        self.Button_Output_Undo.setEnabled(True)
        self.actionUndo_Output.setEnabled(True)
        
        grayscale = self.Source_gray()
    
        scharr_filtered_candy = scharr(grayscale)
        
        image = (scharr_filtered_candy * 255).astype(np.uint8)
        
        self.prev_image.append(image)
        
        qimage = QImage(image.data, image.shape[1], image.shape[0], image.shape[1] , QImage.Format_Grayscale8)

        result = QPixmap.fromImage(qimage)
        print(type(result))
        
        self.previous_output.append(result)
        
        
    def Skiimage_Roberts(self):
        """
        This method takes the RGB raw image and convert it to GrayScale then apply the Skiimage_Roberts method

        Returns
        -------
        None.

        """
        
        self.Button_Output_Undo.setEnabled(True)
        self.actionUndo_Output.setEnabled(True)
        
        grayscale = self.Source_gray()
        
        robertss = roberts(grayscale)
        
        image = (robertss * 255).astype(np.uint8)
        
        self.prev_image.append(image)
        
        qimage = QImage(image.data, image.shape[1], image.shape[0], image.shape[1] , QImage.Format_Grayscale8)

        result = QPixmap.fromImage(qimage)
        print(type(result))
        
        self.previous_output.append(result)

    def Skiimage_Sobel(self):
        """
        This method takes the RGB raw image and convert it to GrayScale then apply the Skiimage_Sobel method

        Returns
        -------
        None.

        """
        self.Button_Output_Undo.setEnabled(True)
        self.actionUndo_Output.setEnabled(True)
        
        grayscale = self.Source_gray()
        
        robertss = sobel(grayscale)
        
        image = (robertss * 255).astype(np.uint8)
        
        self.prev_image.append(image)
        
        qimage = QImage(image.data, image.shape[1], image.shape[0], image.shape[1] , QImage.Format_Grayscale8)

        result = QPixmap.fromImage(qimage)
        print(type(result))
        
        self.previous_output.append(result)
        
    def Skiimage_Prewitt(self):
        """
        This method takes the RGB raw image and convert it to GrayScale then apply the Skiimage_Prewitt method

        Returns
        -------
        None.

        """
        self.Button_Output_Undo.setEnabled(True)
        self.actionUndo_Output.setEnabled(True)
        
        grayscale = self.Source_gray()
        
        robertss = prewitt(grayscale)
        
        image = (robertss * 255).astype(np.uint8)
        
        self.prev_image.append(image)
        
        qimage = QImage(image.data, image.shape[1], image.shape[0], image.shape[1] , QImage.Format_Grayscale8)

        result = QPixmap.fromImage(qimage)
        print(type(result))
        
        self.previous_output.append(result)
   