import streamlit as st
import pandas as pd

def main():
    st.title("Hello World!!")
    st.markdown('Botao')
    
    st.header("This is a header")
    st.subheader("This is a subheader")
    st.text("This is a text")
    #st.image('logo.png')
    #st.audio('record.wav')
    #st.video('asadssda.mp4')

    botao = st.button('Botao')
    if botao:
        st.text('clicado')

    check = st.checkbox('Checkbox')
    if check:
        st.markdown('Checado')

    radio = st.radio('Escolhas as opções',('Opt 1', 'Opt 2'))
    if radio == 'Opt 1':
        st.markdown('Opt 1')
    if radio == 'Opt 2':
        st.markdown('Opt 2')

    select = st.selectbox("Escolha:", ('Opt 1', 'Opt 2'))
    if select == 'Opt 1':
        st.markdown('Opt 1')
    if select == 'Opt 2':
        st.markdown('Opt 2')

    multi = st.multiselect('Escolha', ('Opt 1', 'Opt 2'))
    if multi == 'Opt 1':
        st.markdown('Opt 1')
    if multi == 'Opt 1':
        st.markdown('Opt 2')
    
    file = st.file_uploader('Escolha seu arquivo', type='csv')
    if file is not None:
        number = st.slider('Escolha o numero de linhas que deseja ver', min_value=1, max_value=20)
        df = pd.read_csv(file)
        st.dataframe(df.head(number))

if __name__ == '__main__':
    main()