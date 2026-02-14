import streamlit as st
import google.generativeai as genai
from PIL import Image

# Configuração da Página
st.set_page_config(page_title="Casarão da Construção - Post IA", layout="centered")

st.title("🏠 Casarão da Construção")
st.subheader("Gerador de Posts para Instagram")

# Configurar a API Key na barra lateral
api_key = st.sidebar.text_input("Insira sua API Key do Google:", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')

        # Upload da Imagem - CORRIGIDO AQUI
        uploaded_file = st.file_uploader("📸 Tire uma foto ou suba a imagem do Piso/Porcelanato", type=["jpg", "jpeg", "png"])

        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption="Produto Selecionado", use_container_width=True)
            
            if st.button("✨ Gerar Conteúdo para Instagram"):
                with st.spinner('Analisando o piso e criando o post...'):
                    prompt = """
                    Você é o especialista em marketing da loja Casarão da Construção. 
                    Analise esta imagem de piso/porcelanato e:
                    1. Descreva as características visuais (cor, brilho, estilo).
                    2. Crie uma legenda persuasiva para o Instagram com título, benefícios e sugestão de ambiente.
                    3. CTA: 'Visite o Casarão da Construção ou chame no direct!'
                    4. Hashtags: #CasarãoDaConstrução #Reforma #Porcelanato
                    """
                    
                    response = model.generate_content([prompt, image])
                    st.success("✅ Post Gerado!")
                    st.markdown("---")
                    st.write(response.text)
    except Exception as e:
        st.error(f"Erro de configuração: {e}")
else:
    st.info("Por favor, insira sua API Key na barra lateral para ativar o sistema.")
