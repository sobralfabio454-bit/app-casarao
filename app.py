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
        
        # AJUSTE AQUI: Tentando o modelo mais atualizado disponível
        # O sistema testará o Gemini 1.5 Flash que é o padrão estável atual
       model = genai.GenerativeModel('models/gemini-1.5-flash-latest')
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
        # Se o modelo 1.5 falhar, ele avisará aqui, mas o 'models/' costuma resolver
        st.error(f"Erro ao conectar com o Gemini: {e}")
        st.info("Dica: Verifique se sua chave API está ativa no Google AI Studio.")
else:
    st.info("Por favor, insira sua API Key na barra lateral para ativar o sistema.")
