import streamlit as st

import pandas as pd
import numpy as np

from PIL import Image

# Overall setting

st.set_page_config(layout="wide")

st.title("Experiment Results of the Contrastive Loss Model from Team Small Rice") 

paper_result_img = Image.open('paper_result.png')
st.image(paper_result_img)

exp_result_df = pd.read_csv("exp_result.csv", delimiter=',')
st.write(exp_result_df)