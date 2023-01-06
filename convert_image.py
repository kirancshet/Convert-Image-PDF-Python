#-------------------------------------------------------------------------------
# Name:         convert_image.py
# Purpose:      This Python script convert image into PDF 
# Author:       Kiran Chandrashekhar
# Created:      18-Dec-2022
#-------------------------------------------------------------------------------

import os
from random import randint
from PIL import Image

class CnvertImagePDF:
    def __init__(self):
        pass

    
    def get_all_files(self, directory:str)->list:
        """
        Get all the files from the directory
        """
        complete_file_list = []
        for dirname, subdirs, files in os.walk(directory):                
            file_list = [os.path.join(dirname, file) for file in files]
            complete_file_list.extend(file_list)
      
        return complete_file_list

    #------------------------------
    #   Convert all the images in the input/ directory
    #------------------------------

    def convert_all_images(self, directory:str)->list:
        file_list = self.get_all_files(directory)

        pdf_files = []
        for image_path in file_list:
            pdf_path = self.convert_image_pdf(image_path)
            pdf_files.append(pdf_path)

        return pdf_files
            
    #------------------------------------------
    #   Convert multiple images into single PDF
    #------------------------------------------
    def convert_multiple_images_pdf(self, directory:str)->list:
        file_list = self.get_all_files(directory)
        pdf_file = f"{os.getcwd()}/output/combined_{randint(100_000,999_999)}.pdf"

        img_list = [Image.open(image_path) for image_path in file_list]
        img_list[0].save(pdf_file, "PDF", optimize=True, save_all=True, append_images=img_list[1:])

        return pdf_file
        
    #------------------------------
    #   Convert image to PDF
    #------------------------------
    def convert_image_pdf(self, image_path):
        
        image_name = os.path.basename(image_path)
        file_name = os.path.splitext(image_name)[0]
        pdf_file = f"{os.getcwd()}/output/{file_name}_{randint(100_000,999_999)}.pdf"

        img = Image.open(image_path)
        im_1 = img.convert('RGB')
        im_1.save(pdf_file)
        return pdf_file


    
def main():
    obj = CnvertImagePDF()
    directory = f"{os.getcwd()}/input/"
    #obj.convert_all_images(directory)
    obj.convert_multiple_images_pdf(directory)
    
    
if __name__ == '__main__':
    main()
    print("Done")