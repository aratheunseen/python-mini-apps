import streamlit as st
import pandas as pd

st.set_page_config("Portfolio - Metaverse Creator", "📚", "wide", "auto")

col1, col2 = st.columns([5,7],gap='large')

with col1:
    st.image('images/verse.bmp')

with col2:
    st.title('Metaverse Creator')
    content = """
    Hi, I'm a Metaverse Creator who is passionate about creating and developing virtual worlds and experiences. I'm a self-taught developer and have been creating virtual worlds for over 10 years. I have a strong background in computer science and am proficient in programming languages such as Python, JavaScript, and C++. I have a strong understanding of 3D modeling and animation, and I'm skilled in using tools such as Blender, Unity, and Unreal Engine. I'm also experienced in creating virtual reality experiences and have a strong understanding of VR hardware and software. I'm passionate about creating immersive and engaging virtual worlds and experiences, and I'm excited to continue pushing the boundaries of what's possible in the metaverse.
    """
    st.info(content)


st.title('Projects I created',anchor='projects')

def project_card(title,description,url,image):
    st.image(f'projects/{image}')
    st.subheader(title)
    st.info(description)
    st.write('GitHub: [Source Code]('+url+'), [Live Demo]('+url+')')
    st.write('---')

col3, col4, col5, col6 = st.columns([3,3,3,3],gap='large')

df = pd.read_csv("data.csv",sep=';')

for row in range(0,20,4):
    for column in range(0,4,4):
        with col3:
            project_card(df.iloc[row,column],df.iloc[row,column+1],df.iloc[row,column+2],df.iloc[row,column+3])
        with col4:
            project_card(df.iloc[row+1,column],df.iloc[row+1,column+1],df.iloc[row+1,column+2],df.iloc[row+1,column+3])
        with col5:
            project_card(df.iloc[row+2,column],df.iloc[row+2,column+1],df.iloc[row+2,column+2],df.iloc[row+2,column+3])
        with col6:
            project_card(df.iloc[row+3,column],df.iloc[row+3,column+1],df.iloc[row+3,column+2],df.iloc[row+3,column+3])

col = st.columns(1)

with col[0]:
    st.info("© 2024 aratheunseen. All rights reserved.")