import os
import streamlit as st
from hydralit import HydraHeadApp

class goGitHub(HydraHeadApp):
    def __init__(self, title='Welcome to CTsGAN', **kwargs):
        self.__dict__.update(kwargs)
        self.title = title
        super().__init__()
    
    def run(self):
        try:
            st.markdown("<h1 style='text-align: center;color:black;fontsize200%'>Welcome to CTsGAN</h1>", unsafe_allow_html=True)
            st.markdown("<h2 style='text-align: center;'>Image Enhancement for portable CT Scanner using Super Resolution</h2>",unsafe_allow_html=True)
            st.markdown("<h4 style='text-align: center;'>The documentation and source code for the project can be found in our <a href = https://github.com/Sidhved/CTSGAN_Repo>GitHub Repository</a></h2>",unsafe_allow_html=True)
        except Exception as e:
            st.image(os.path.join(".", "resources", "failure.png"), width=50,)
            st.error('An error has occured, we apologize for your inconvenience and request you to try again.')
            st.error('Error details: {}'.format(e)) 
            
