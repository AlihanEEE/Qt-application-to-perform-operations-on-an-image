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



class Common_Proc:
    def __init__(self):
        """
        This constructor contains the all attributes for the project

        Returns
        -------
        None.

        """
        
        
        self.next_output = []
        self.previous_output = []
        self.prev_image = []
        self.next_image = []
        
        self.extension = ""
        
        self.output_image = None
        self.source_image = None
        self.file_name = ""
        self.image = None
        
        self.source_save_image= None
        
    def set_next_output(self,data):
        """
        This method sets the next_scene attribute 

        Parameters
        ----------
        data : data for assign to next_scene attribute

        Returns
        -------
        None.

        """
        self.next_output = data
    
    def get_next_output(self):
        """
        This method returns the next_scene attribute 

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        return self.next_output
    
    
    def set_previous_output(self,data):
        """
        This method sets the previous_output attribute 

        Parameters
        ----------
        data : data for assign to previous_output attribute

        Returns
        -------
        None.

        """
        self.previous_output = data
    
    def get_previous_output(self):
        """
        This method returns the previous_output attribute 

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        return self.previous_output
    
    
    def set_prev_image(self,data):
        """
        This method sets the prev_image attribute 

        Parameters
        ----------
        data : data for assign to prev_image attribute

        Returns
        -------
        None.

        """
        self.prev_image = data
    
    def get_prev_image(self):
        """
        This method returns the prev_image attribute 

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        return self.prev_image
    
    
    def set_next_image(self,data):
        """
        This method sets the next_image attribute 

        Parameters
        ----------
        data : data for assign to next_image attribute

        Returns
        -------
        None.

        """
        self.next_image = data
    
    def get_next_image(self):
        """
        This method returns the next_image attribute 

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        return self.next_image
    
    
    def set_extension(self,data):
        """
        This method sets the extension attribute 

        Parameters
        ----------
        data : data for assign to extension attribute

        Returns
        -------
        None.

        """
        self.extension = data
    
    def get_extension(self):
        """
        This method returns the extension attribute 

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        return self.extension
    
    
    def set_output_image(self,data):
        """
        This method sets the output_image attribute 

        Parameters
        ----------
        data : data for assign to output_image attribute

        Returns
        -------
        None.

        """
        self.output_image = data
    
    def get_output_image(self):
        """
        This method returns the output_image attribute 

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        return self.output_image
     
    
    def set_source_image(self,data):
        """
        This method sets the source_image attribute 

        Parameters
        ----------
        data : data for assign to source_image attribute

        Returns
        -------
        None.

        """
        self.source_image = data
    
    def get_source_image(self):
        """
        This method returns the source_image attribute 

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        return self.source_image
    
    def set_file_name(self,data):
        """
        This method sets the file_name attribute 

        Parameters
        ----------
        data : data for assign to file_name attribute

        Returns
        -------
        None.

        """
        self.file_name = data
    
    def get_file_name(self):
        """
        This method returns the file_name attribute 

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        return self.file_name
    
    def set_image(self,data):
        """
        This method sets the image attribute 

        Parameters
        ----------
        data : data for assign to image attribute

        Returns
        -------
        None.

        """
        self.image = data
    
    def get_image(self):
        """
        This method returns the image attribute 

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        return self.image
    
    def set_source_save_image(self,data):
        """
        This method sets the source_save_image attribute 

        Parameters
        ----------
        data : data for assign to source_save_image attribute

        Returns
        -------
        None.

        """
        self.source_save_image = data
    
    def get_source_save_image(self):
        """
        This method returns the source_save_image attribute 

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        return self.source_save_image

    def File(self):
        """
        This method opens the searchig file window,The selected file assigned the source_image attribute.  The selected file must be *jpg or *png extensions

        Returns
        -------
        None.

        """
        self.statusbar.showMessage('File Searching')
        
        searching_window = QFileDialog()
        file_filter = "Image Files (*.jpg *.png)"
        searching_window.setNameFilter(file_filter)
        searching_window.setFileMode(QFileDialog.ExistingFile)
        
        if searching_window.exec_():
            
            temp_file = searching_window.selectedFiles()[0]
            split_tup = os.path.splitext(temp_file)
            self.set_extension(split_tup[-1])
            
            if temp_file:
                if self.extension in ('.jpg', '.png'):
                    self.set_file_name(temp_file)
                    # Seçilen dosya uzantısı desteklenmiyor, tekrar seçtirin
                    self.statusbar.showMessage('Source selected sucessfully. Source Name: ' + self.get_file_name() )
                    
                    self.set_source_image(QPixmap(self.get_file_name()))
                    
                    # original_width = self.Label_Source_Image.width()
                    # original_height = self.Label_Source_Image.height()
                    
                    self.Label_Source_Image.setPixmap(self.source_image.scaled(self.Label_Source_Image.width(), self.Label_Source_Image.height(), Qt.AspectRatioMode.KeepAspectRatio))
                    
                    # self.output_image = self.source_image
                    
                    print(type(self.get_source_image()))
                    
                    # self.previous_source.append(self.source_image)
                    # self.previous_output.append(self.output_image)
                    
                    self.Enable_After_FileSelected()
                    
                    self.set_source_save_image(io.imread(self.get_file_name()))
                    
                else:
                    # Dosya uzantısı destekleniyor, burada seçilen dosyayı kullanabilirsiniz
                    self.statusbar.showMessage("You've selected wrong file extension please try again")
            else:
                # Herhangi bir dosya seçilmedi
                self.statusbar.showMessage("File didnt select")
                
    

    def Output_Show(self):
        """
        This method Shows the manipulated source_image data on the output screen

        Returns
        -------
        None.

        """
                
        self.Enable_Saving_Funcs_Output()
        
        if self.previous_output:
            self.Button_Output_Undo.setEnabled(True)
            self.actionUndo_Output.setEnabled(True)
            self.actionClear_Output.setEnabled(True)
            self.Button_Output_Clear.setEnabled(True)
            
            
            
            
        else:
            self.Label_Output_Image.clear()
            self.Disable_Saving_Funcs_Output()
            
            
        
        # original_width = self.previous_output[-1].width()
        # original_height = self.previous_output[-1].height()
        self.Label_Output_Image.setPixmap(self.get_previous_output()[-1].scaled(self.Label_Source_Image.width(), self.Label_Source_Image.height(), Qt.AspectRatioMode.KeepAspectRatio))
        # self.Label_Output_Image.setPixmap(self.previous_output[-1].scaled(original_width, original_height, Qt.AspectRatioMode.KeepAspectRatio))
 
    def Undo(self):
        """
        This method show the previous output on the screen if there is no previous output, the action and button of the undo are set disabled

        Returns
        -------
        None.

        """
        
        self.Button_Output_Redo.setEnabled(True)
        self.actionRedo_Output.setEnabled(True)
        
        temp = self.get_previous_output().pop()
        self.get_next_output().append(temp)
        
        
        if self.get_previous_output():
            pass
            
        else:
            self.Button_Output_Undo.setEnabled(False)
            self.actionUndo_Output.setEnabled(False)
        
        
        temp_save = self.get_prev_image().pop()
        self.get_next_image().append(temp_save)
        
            
    def Redo(self):
        """
        This method is Redo method. Redo button or action becomes available when the undo button or action are executed . It shows the next output on the screen if there is no next output, the action and button of the redo are set disabled

        Returns
        -------
        None.

        """
        temp = self.get_next_output().pop()
        self.get_previous_output().append(temp)
        
        
        
        if self.get_next_output():
            pass
            
        else:
            self.Button_Output_Redo.setEnabled(False)
            self.actionRedo_Output.setEnabled(False)
        
        temp_save = self.get_next_image().pop()
        self.get_previous_image().append(temp_save)
        
    def Clear_Source(self):
        """
        This method Clears the source screen and output screen

        Returns
        -------
        None.

        """
        #inputu ve outputu clearla
        #prev_outputu sıfırla
        #her şeyi disable et
        self.Label_Output_Image.clear()
        self.Label_Source_Image.clear()
        self.previous_output = []
        self.next_output = []
        self.next_image = []
        self.previous_image = [] 
        self.Disable_After_Clear_Input()
        
    def Clear_Output(self):
        """
        This method Clears the output screen

        Returns
        -------
        None.

        """
        #outputu clearla
        #prev_outputu sıfırla
        self.Label_Output_Image.clear()
        self.previous_output = []
        self.next_output = []
        self.next_image = []
        self.previous_image = []
        
        self.Button_Output_Redo.setEnabled(False)
        self.actionRedo_Output.setEnabled(False)
        self.Button_Output_Undo.setEnabled(False)
        self.actionUndo_Output.setEnabled(False)
        self.Button_Output_Clear.setEnabled(False)
        self.actionClear_Output.setEnabled(False)
        
        self.Disable_Saving_Funcs_Output()
        
    def Save_As_Output(self):
        """
        This method Saves as the output 

        Returns
        -------
        None.

        """
        save_path,_ = QFileDialog.getSaveFileName(self.centralwidget,"Save Output","","Image Files (*{})".format(self.extension))
        if save_path:
            io.imsave(save_path, self.prev_image[-1])
        print("save")
    def Save_Output(self):
        """
        This method save the output

        Returns
        -------
        None.

        """
        io.imsave(self.file_name, self.prev_image[-1])
        print("save")
    
    def Export_As_Output(self):
        """
        This method Export the output

        Returns
        -------
        None.

        """
        if self.extension == ".jpg":
            import_as_extension =".png"
        else:
            import_as_extension = ".jpg"
            
        save_path,_ = QFileDialog.getSaveFileName(self.centralwidget,"Save Output","","Image Files (*{})".format(import_as_extension))
        if save_path:
            io.imsave(save_path, self.prev_image[-1])
        print("export_as")
        
    def Export_As_Source(self):
        """
        This method export the input

        Returns
        -------
        None.

        """
        if self.extension == ".jpg":
            import_as_extension =".png"
        else:
            import_as_extension = ".jpg"
            
        save_path,_ = QFileDialog.getSaveFileName(self.centralwidget,"Save Output","","Image Files (*{})".format(import_as_extension))
        if save_path:
            io.imsave(save_path, self.source_save_image)
        print("export_as")
   
        
    def Disable_After_Clear_Input(self):
        """
        This method disables the necessery buttons and actions on the screen when Clean Input executed

        Returns
        -------
        None.

        """
        
        self.actionSource_menuExport_As.setEnabled(False)
        self.actionOutput_menuExport_As.setEnabled(False)
        self.actionSave_Output.setEnabled(False)
        self.actionSave_As_Output.setEnabled(False)
        self.actionExit.setEnabled(False)
        self.actionClear_Source.setEnabled(False)
        self.actionClear_Output.setEnabled(False)
        self.actionUndo_Output.setEnabled(False)
        self.actionRedo_Output.setEnabled(False)
        self.actionChan_Vese_Segmentation.setEnabled(False)
        self.actionOtsu_Segmentation.setEnabled(False)
        self.actionMorpSnakes_Segmentation.setEnabled(False)
        self.actionScharr.setEnabled(False)
        self.actionRoberts.setEnabled(False)
        self.actionSobel.setEnabled(False)
        self.actionPrewit.setEnabled(False)
        self.actionRGB_to_HSV.setEnabled(False)
        self.actionRGB_Grey.setEnabled(False)
        self.Button_Color_RGB2HSV.setEnabled(False)
        self.Button_Color_RGB2Grey.setEnabled(False)
        self.Button_Edge_Scharr.setEnabled(False)
        self.Button_Seg_ChanVese.setEnabled(False)
        self.Button_Seg_Otsu.setEnabled(False)
        self.Button_Seg_Morp.setEnabled(False)
        self.Button_Edge_Roberts.setEnabled(False)
        self.Button_Edge_Sobel.setEnabled(False)
        self.Button_Edge_Prewitt.setEnabled(False)
        self.Button_Output_Clear.setEnabled(False)
        self.Button_Source_Clear.setEnabled(False)
        self.Button_Output_Undo.setEnabled(False)
        self.Button_Source_Export.setEnabled(False)
        self.Button_Output_Save.setEnabled(False)
        self.Button_Output_SaveAs.setEnabled(False)
        self.Button_Output_ExportAs.setEnabled(False)
        self.Button_Output_Redo.setEnabled(False)
        self.actionRedo_Output.setEnabled(False)
        
    def Enable_After_FileSelected(self):
        """
        This method enables the necessery buttons and actions on the screen when File selection executed

        Returns
        -------
        None.

        """
        self.statusbar.showMessage("Functions Enabled")
        
        self.actionSource_menuExport_As.setEnabled(True)
        self.actionExit.setEnabled(True)
        self.actionClear_Source.setEnabled(True)
        # self.actionClear_Output.setEnabled(True)
        # self.actionUndo_Output.setEnabled(True)
        self.actionRedo_Output.setEnabled(True)
        self.actionChan_Vese_Segmentation.setEnabled(True)
        self.actionOtsu_Segmentation.setEnabled(True)
        self.actionMorpSnakes_Segmentation.setEnabled(True)
        self.actionScharr.setEnabled(True)
        self.actionRoberts.setEnabled(True)
        self.actionSobel.setEnabled(True)
        self.actionPrewit.setEnabled(True)
        self.actionRGB_to_HSV.setEnabled(True)
        self.actionRGB_Grey.setEnabled(True)
        self.Button_Color_RGB2HSV.setEnabled(True)
        self.Button_Color_RGB2Grey.setEnabled(True)
        self.Button_Edge_Scharr.setEnabled(True)
        self.Button_Seg_ChanVese.setEnabled(True)
        self.Button_Seg_Otsu.setEnabled(True)
        self.Button_Seg_Morp.setEnabled(True)
        self.Button_Edge_Roberts.setEnabled(True)
        self.Button_Edge_Sobel.setEnabled(True)
        self.Button_Edge_Prewitt.setEnabled(True)
        # self.Button_Output_Clear.setEnabled(True)
        self.Button_Source_Clear.setEnabled(True)
        # self.Button_Output_Undo.setEnabled(True)
        self.Button_Source_Export.setEnabled(True)
        
    def Enable_Saving_Funcs_Output(self):
        """
        This method enables the necessery buttons and actions on the screen when the output image occurs on the screen

        Returns
        -------
        None.

        """
        self.actionOutput_menuExport_As.setEnabled(True)
        self.actionSave_Output.setEnabled(True)
        self.actionSave_As_Output.setEnabled(True)
        
        self.Button_Output_Save.setEnabled(True)
        self.Button_Output_SaveAs.setEnabled(True)
        self.Button_Output_ExportAs.setEnabled(True)
        
    def Disable_Saving_Funcs_Output(self):
        """
        This method disables the necessery buttons and actions on the screen when there is no output image on the screen

        Returns
        -------
        None.

        """
        self.actionOutput_menuExport_As.setEnabled(False)
        self.actionSave_Output.setEnabled(False)
        self.actionSave_As_Output.setEnabled(False)
        
        self.Button_Output_Save.setEnabled(False)
        self.Button_Output_SaveAs.setEnabled(False)
        self.Button_Output_ExportAs.setEnabled(False)