import os
import streamlit as st
import pandas as pd
from hydralit import HydraHeadApp

class References(HydraHeadApp):
    def __init__(self, title='Welcome to CTsGAN', **kwargs):
        self.__dict__.update(kwargs)
        self.title = title
        super().__init__()
    
    def run(self):
        try:
            st.markdown("<h1 style='text-align:center;padding: 0px 0px;color:black;fontsize200%'>Welcome to CTsGAN</h1>", unsafe_allow_html=True)
            st.markdown("<h2 style='text-align: center;'>Image Enhancement for portable CT Scanner using Super Resolution</h2>",unsafe_allow_html=True)
            st.markdown("<h2 style='text-align: center;'>The following table displays the references that helped in creation of this project</h2>",unsafe_allow_html=True)
            df = pd.read_csv('Ref.csv')
            st.dataframe(df, use_container_width=True)

        except Exception as e:
            st.error('An error has occured, we apologize for your inconvenience and request you to try again.')
            st.error('Error details: {}'.format(e)) 