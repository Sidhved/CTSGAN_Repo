import os
import streamlit as st
from hydralit import HydraHeadApp
import glob
from subprocess import call
from PIL import Image
import numpy as np
import os
import io
import cv2
import sys
import matplotlib.pyplot as plt
import psutil
import hydralit_components as hc
import zipfile
import shutil
import time

class HomeApp(HydraHeadApp):
    def __init__(self, title='Welcome to CTsGAN', **kwargs):
        self.__dict__.update(kwargs)
        self.title = title
    
    def run(self):
        try:
            st.markdown("<h1 style='text-align:center;padding: 0px 0px;color:black;fontsize200%'>Welcome to CTsGAN</h1>", unsafe_allow_html=True)
            st.markdown("<h2 style='text-align: center;'>Image Enhancement for portable CT Scanner using Super Resolution</h2>",unsafe_allow_html=True)
            
            input_dir = "tmp\input"
            output_dir = "tmp\output"
            model_name = "CTSGAN_x4"
            denoise = "Medium"
            tile = 0
            
            def run_cmd(command):
                try:
                    print(command)
                    call(command, shell=True)
                except KeyboardInterrupt:
                    print("Process interrupted")
                    sys.exit(1)

            shutil.rmtree('tmp\input')
            shutil.rmtree('tmp\output')
            run_cmd("mkdir tmp\input")
            run_cmd("mkdir tmp\output")
            
            run_cmd("python app_inference.py -i " + input_dir + " -o " + output_dir + " -n " + model_name + " -t " + str(tile))

            @st.cache
            def load_image(image_file):
                img = Image.open(image_file)
                return img

            #sidebar
            st.sidebar.title("**CTsGAN**")
            input_image = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
            if st.sidebar.checkbox("**Customize Settings**"):
                model_name = st.sidebar.radio("**Scaling Factor:**", ["CTSGAN_x4", "CTSGAN_x2"], help="Scale to x times the original size")
                denoise = st.sidebar.selectbox("**Restoration Strength:** ", ["High", "Medium (default)", "Low"], index=1)
                tile = st.sidebar.select_slider("Tiles", [0.0, 0.5, 1.0], value=0.0, help="Change Tiles only if image too large")

            #Columns
            col1, col2 = st.columns(2)

            input_dir = "tmp\input"
            output_dir = "tmp\output"

            def infer(input_dir="tmp\input", output_dir="tmp\output", model_name="CTSGAN_x4", tile=0):
                if denoise == "Low":
                    denoise_strength = 0.0
                elif denoise == "Medium":
                    denoise_strength = 0.5
                elif denoise == "High":
                    denoise_strength = 1.0
                run_cmd("python app_inference.py -i " + input_dir + " -o " + output_dir + " -n " + model_name + " -t " + str(tile))


            #ip_col
            if input_image is not None:
                file_details = {"FileName":input_image.name,"FileType":input_image.type}
                img = load_image(input_image)
                col1.image(img, caption="Input Image", use_column_width=True)
                with open(os.path.join(input_dir, input_image.name),"wb") as f: 
                    f.write(input_image.getbuffer()) 
                infer(input_dir=input_dir, output_dir=output_dir, model_name=model_name, tile=int(tile))
                output_path = "tmp\output\\"+input_image.name.split(".")[0]+"_out."+input_image.name.split(".")[1]
                img2 = Image.open(output_path)
                col2.image(img2, caption="Output Image", use_column_width=True)
                zip_filename = 'CTsGAN_output.zip'
                if os.path.exists(zip_filename):
                    os.remove(zip_filename)
                zip_obj = zipfile.ZipFile(zip_filename, "w")
                zip_obj.write(output_path, compress_type = zipfile.ZIP_DEFLATED)
                zip_obj.close()

                with open(zip_filename, 'rb') as z:
                    b = col2.download_button(label="Download Image (Full Size)", data=z, file_name=zip_filename, mime="application/zip")

            else:
                im1 = Image.open("tmp\default_input\image1.jpg")
                col1.image(im1, caption="Input Image", use_column_width=True)
                col1.write("**Name:** *image1*")
                col1.write("**Type:** *JPG*")
                im2 = Image.open("tmp\default_output\image1_out.jpg")
                col2.image(im2, caption="CTsGAN Output", use_column_width=True)


        except Exception as e:
            st.error('An error has occured, we apologize for your inconvenience and request you to try again.')
            st.error('Error details: {}'.format(e))    