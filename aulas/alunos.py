import streamlit as st
import pandas as pd

def main():
    st.title("Acelera Dev Data Science!")
    st.image('logo.png')
    file = st.file_uploader('Upload your file', type='csv')
    if file:
        slider = st.slider('Valores', 1,100)
        df = pd.read_csv(file)
        st.dataframe(df.head(slider))
        st.markdown("...")
        st.table(df.head(slider))
        st.markdown("Colunas do Dataframe")
        st.write(df.columns)
        st.table(df.groupby('species')['petal_width'].mean())

if __name__ == '__main__':
    main()