import pandas as pd
import streamlit as st

df = pd.read_excel('posts1.xlsx')

dudu_df = df[df['Profile'] == 'Eduardo Paes']

st.set_page_config(page_title="Análise do Instagram de Eduardo Paes", page_icon="📐", layout="wide")

st.title('Análise do Instagram de Eduardo Paes')

df2 = dudu_df.sort_values(by='Post interaction rate', ascending=False).head(10)

st.header("Nuvem de palavras das legendas escritas pelo pré-candidato em suas publicações:")

url_imagem = 'fotodudu.png'
st.image(url_imagem)

st.header("As 10 publicações com maior taxa de engajamento:")
st.markdown("Na análise eu foquei apenas nas três primeiras publicações:")
st.markdown("1° https://www.instagram.com/reel/Ctw-f3kLfTJ/")
st.markdown("2° https://www.instagram.com/reel/Co4WaSBNF6X/")
st.markdown("3° https://www.instagram.com/reel/CnHYwB-JwDd/")

st.dataframe(df2)
