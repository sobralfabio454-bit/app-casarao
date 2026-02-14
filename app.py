import streamlit as st
import google.generativeai as genai
from PIL import Image

# Configuração da Página
st.set_page_config(page_title="Casarão da Construção - Post IA", layout="centered")

st.title("🏠 Casarão da Construção")
st.subheader("Gerador de Posts para Instagram")

# Configurar a API Key (O usuário insere na barra lateral ou deixamos fixa)
api_key = st.sidebar.text_input("Insira sua API Key do Google:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    # Upload da Imagem
    uploaded_file = st.file_input("📸 Tire uma foto ou suba a imagem do Piso/Porcelanato", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Imagem carregada", use_container_width=True)
        
        if st.button("✨ Gerar Conteúdo para Instagram"):
            with st.spinner('Analisando o produto e criando a mágica...'):
                # O Prompt Estratégico (Instrução para a IA)
                prompt = """
                Você é o especialista em marketing da loja Casarão da Construção. 
                Analise esta imagem de piso/porcelanato e:
                1. Descreva as características visuais (cor, estilo, acabamento).
                2. Crie uma legenda persuasiva para o Instagram com:
                   - Título impactante.
                   - Benefícios do produto.
                   - Sugestão de onde usar (ex: sala, cozinha).
                   - CTA: 'Transforme sua casa hoje! Visite o Casarão da Construção ou clique no link da bio.'
                   - Hashtags: #CasarãoDaConstrução #Reforma #Decoração #Porcelanato
                3. Sugira uma ideia de 'Ambientação' (ex: 'Imagine este piso com móveis de madeira e paredes off-white').
                """
                
                response = model.generate_content([prompt, image])
                
                st.success("✅ Post Gerado com Sucesso!")
                st.markdown("---")
                st.markdown(response.text)
else:
    st.info("Por favor, insira sua API Key do Google na barra lateral para começar.")
