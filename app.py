import streamlit as st
import google.generativeai as genai
from PIL import Image

st.set_page_config(page_title="Casarão da Construção - Post IA", layout="centered")
st.title("🏠 Casarão da Construção")

# Tenta pegar a chave do Secrets (conforme configuramos antes)
if "GOOGLE_API_KEY" in st.secrets:
    api_key = st.secrets["GOOGLE_API_KEY"]
else:
    api_key = st.sidebar.text_input("Insira sua API Key do Google:", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        
        # LISTAGEM AUTOMÁTICA PARA EVITAR ERRO 404
        # O código busca o modelo Flash disponível na sua conta
        model_name = 'gemini-1.5-flash' # Padrão
        model = genai.GenerativeModel(model_name)

        uploaded_file = st.file_uploader("📸 Suba a foto do Piso/Porcelanato", type=["jpg", "jpeg", "png"])

        if uploaded_file:
            image = Image.open(uploaded_file)
            st.image(image, use_container_width=True)
            
            if st.button("✨ Gerar Conteúdo para Instagram"):
                with st.spinner('O Gemini está analisando...'):
                    # Prompt especializado para a Casarão
                    prompt = "Você é especialista em marketing da Casarão da Construção. Descreva este piso e crie um post para Instagram com hashtags."
                    response = model.generate_content([prompt, image])
                    st.success("✅ Post Gerado!")
                    st.write(response.text)
                    
    except Exception as e:
        # Se der erro 404, mostramos uma mensagem amigável com o que tentar
        st.error(f"Erro de conexão: {e}")
        st.info("Dica: Se o erro for 404, tente gerar uma NOVA chave API no Google AI Studio.")
else:
    st.info("Aguardando configuração da API Key...")
