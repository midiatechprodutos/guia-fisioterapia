import streamlit as st
import requests

st.set_page_config(page_title="Guia de Fisioterapia Ortopedica", page_icon="🏥", layout="centered")

st.markdown("<h2 style='text-align: center; color: #2874A6;'>🏥 GUIA INTERATIVO DE FISIOTERAPIA</h2>", unsafe_allow_html=True)
st.write("---")

LINK_BASE = "https://githubusercontent.com"

# Função inteligente que testa qual extensão de imagem existe de verdade no seu GitHub
def obter_link_imagem_valido(nome_base):
    extensoes = [".jpeg", ".jpg", ".png", ".JPEG", ".JPG", ".PNG"]
    for ext in extensoes:
        url_teste = f"{LINK_BASE}{nome_base}{ext}"
        # Verifica se o link realmente existe na internet
        resposta = requests.head(url_teste)
        if resposta.status_code == 200:
            return url_teste
    return None

banco_doencas = {
    "1. Sindrome do Impacto do Manguito Rotador": {
        "definicao": "Compressão mecânica crônica das estruturas que passam pelo espaço subacromial.",
        "clinica": "O espaço subacromial é delimitado superiormente pelo acrômio e inferiormente pela cabeça do úmero.",
        "sintomas": ["Dor profunda no ombro (pior à noite)", "Dor ao elevar o braço acima de 90°"],
        "testes": ["Teste de Neer", "Teste de Hawkins-Kennedy", "Teste de Jobe"],
        "agudo": "Analgesia e controle inflamatório (TENS e crioterapia).",
        "cronico": "Fortalecimento dos rotadores externos e estabilização escapular.",
        "img1": "ombro", "img2": "ombro1"
    },
    "2. Hernia de Disco Lombar": {
        "definicao": "Deslocamento do núcleo pulposo através de fissuras no anel fibroso do disco.",
        "clinica": "Ocorre com maior frequência em L4-L5 e L5-S1, gerando compressão mecânica e inflamação.",
        "sintomas": ["Dor lombar aguda (lombalgia)", "Dor que irradia para o membro inferior (ciatalgia)"],
        "testes": ["Teste de Lasègue / Elevação da Perna Reta (SLR)", "Slump Test"],
        "agudo": "Técnicas de preferência de direção (Método Mackenzie) e tração suave.",
        "cronico": "Exercícios de controle motor profundo e mobilização neural.",
        "img1": "coluna", "img2": "coluna1"
    },
    "3. Osteoartrose de Joelho (Gonartrose)": {
        "definicao": "Doença articular degenerativa crônica caracterizada pelo desgaste da cartilagem.",
        "clinica": "Degradação da cartilagem hialina, levando à fricção osso com osso e esclerose subcondral.",
        "sintomas": ["Dor mecânica (piora com carga)", "Rigidez articular matinal temporária (< 30 min)"],
        "testes": ["Teste de estresse em varo/valgo", "Teste de compressão patelar (Clarke)"],
        "agudo": "Modulação da dor com recursos térmicos e crioterapia conforme o quadro.",
        "cronico": "Fortalecimento progressivo do quadríceps e treino de equilíbrio.",
        "img1": "joelho", "img2": "joelho1"
    },
    "4. Sindrome do Tunel do Carpo": {
        "definicao": "Neuropatia compressiva decorrente da compressão do nervo mediano no punho.",
        "clinica": "O processo inflamatório nos tendões flexores reduz o espaço e comprime o nervo.",
        "sintomas": ["Parestesia na região palmar dos 3 primeiros dedos", "Piora noturna acentuada"],
        "testes": ["Teste de Phalen", "Sinal de Tinel"],
        "agudo": "Uso de órtese de posicionamento noturno e TENS.",
        "cronico": "Mobilização manual dos ossos do carpo e deslizamento neural.",
        "img1": "punho", "img2": "punho1"
    },
    "5. Fascite Plantar": {
        "definicao": "Processo degenerativo ou inflamatório da fáscia plantar por microtraumas proximal.",
        "clinica": "Sob sobrecarga mecânica ocorrem microrrupturas próximas à sua origem óssea.",
        "sintomas": ["Dor aguda no calcanhar nos primeiros passos da manhã", "Piora no final do dia"],
        "testes": ["Teste do Molinete (Windlass Test)", "Palpação focalizada"],
        "agudo": "Crioterapia local e liberação miofascial plantar.",
        "cronico": "Alongamentos do complexo gastrocnêmio-sóleo e fortalecimento intrínseco.",
        "img1": "pe", "img2": "pe1"
    }
}

escolha = st.selectbox("Escolha uma Patologia para Estudar:", list(banco_doencas.keys()))

if escolha:
    dados = banco_doencas[escolha]
    st.markdown(f"### 📋 {escolha.split('. ', 1)[-1]}")
    st.write(f"**Definição:** {dados['definicao']}")
    st.write(f"**Esquema Clínico:** {dados['clinica']}")
    
    st.write("**Sintomas:**")
    for s in dados["sintomas"]: st.write(f"- {s}")
    st.write("**Testes Físicos:**")
    for t in dados["testes"]: st.write(f"🔍 {t}")
    
    st.markdown("<h4 style='color: #2874A6;'>⚡ Tratamento</h4>", unsafe_allow_html=True)
    st.write(f"**Fase Aguda:** {dados['agudo']}")
    st.write(f"**Fase Crônica:** {dados['cronico']}")
    
    st.write("---")
    st.write("**🖼️ Referências Visuais:**")
    
    # Busca dinamicamente os links válidos na internet
    link_foto1 = obter_link_imagem_valido(dados["img1"])
    link_foto2 = obter_link_imagem_valido(dados["img2"])
    
    col1, col2 = st.columns(2)
    with col1:
        if link_foto1: st.image(link_foto1, use_container_width=True)
        else: st.write(f"*(Imagem '{dados['img1']}' não encontrada no GitHub)*")
    with col2:
        if link_foto2: st.image(link_foto2, use_container_width=True)
        else: st.write(f"*(Imagem '{dados['img2']}' não encontrada no GitHub)*")
            
