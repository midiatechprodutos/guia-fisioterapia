import streamlit as st

# Configuração da página da internet moderna
st.set_page_config(
    page_title="Guia Interativo de Fisioterapia Ortopédica",
    page_icon="🏥",
    layout="centered"
)

# Estilização visual básica em azul clínico
st.markdown("""
    <style>
    .main-title { font-size:28px !important; color:#2874A6; font-weight:bold; text-align:center; }
    .section-title { font-size:18px !important; color:#2874A6; font-weight:bold; margin-top:15px; }
    .content-box { background-color:#F2F4F4; padding:15px; border-radius:8px; margin-bottom:10px; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🏥 GUIA INTERATIVO DE FISIOTERAPIA ORTOPÉDICA</div>', unsafe_allow_html=True)
st.write("---")
st.write("Selecione uma patologia abaixo no menu para carregar instantaneamente a ficha clínica estruturada, testes especiais e conduta de tratamento.")

# BANCO DE DADOS INTEGRADO E EXPANDIDO (8 DOENÇAS COMPLETAS)
banco_doencas = {
    "1. Síndrome do Impacto do Manguito Rotador": {
        "definicao": "Compressão mecânica crônica das estruturas que passam pelo espaço subacromial (tendão do supraespinhal, bursa subacromial e tendão da cabeça longa do bíceps) sob o arco coracoacromial.",
        "clinica": "O espaço subacromial é delimitado superiormente pelo acrômio, processo coracoide e ligamento coracoacromial; inferiormente pela cabeça do úmero. Alterações no formato do acrômio (ganchoso) ou fraqueza muscular diminuem esse espaço, gerando atrito e inflamação crônica.",
        "sintomas": ["Dor profunda no ombro (frequentemente pior à noite ou ao deitar sobre o braço)", "Incapacidade ou dor ao elevar o braço acima de 90°", "Perda progressiva de força funcional."],
        "testes": ["Teste de Neer", "Teste de Hawkins-Kennedy", "Teste de Jobe (isometria do supraespinhal)"],
        "tratamento_agudo": "Analgesia and controle inflamatório (TENS e crioterapia), repouso relativo de movimentos acima da cabeça.",
        "tratamento_cronico": "Fortalecimento dos rotadores externos (infraespinhal e redondo menor) e depressores da cabeça umeral (subescapular), associado à estabilização escapular (serrátil anterior e trapézio inferior) para readequar a biomecânica.",
        "foto1": "imagem-lesao-manguito-1-1", "foto2": "ombro1"
    },
    "2. Hérnia de Disco Lombar": {
        "definicao": "Deslocamento do núcleo pulposo através de fissuras no anel fibroso do disco intervertebral, podendo comprimir raízes nervosas adjacentes.",
        "clinica": "Ocorre com maior frequência nos níveis L4-L5 e L5-S1. O núcleo herniado comprime mecanicamente e gera uma cascata química inflamatória sobre a raiz nervosa que emerge pelo forame intervertebral.",
        "sintomas": ["Dor lombar aguda (lombalgia)", "Dor que irradia para o membro inferior (ciatalgia)", "Parestesia (formigamento), queimação e perda de força muscular no dermátomo afetado."],
        "testes": ["Teste de Lasègue / Elevação da Perna Reta (SLR - positivo entre 35° e 70°)", "Slump Test para tensionamento neural generalizado"],
        "tratamento_agudo": "Técnicas de preferência de direção (Método Mackenzie) para centralização da dor, tração lombar manual suave, TENS e terapia manual para alívio do espasmo protetor.",
        "tratamento_cronico": "Exercícios de controle motor profundo (ativação do transverso do abdômen e multífidos), mobilização neural para restaurar a complacência do tecido nervoso e fortalecimento global.",
        "foto1": "coluna", "foto2": "coluna1"
    },
    "3. Osteoartrose de Joelho (Gonartrose)": {
        "definicao": "Doença articular degenerativa crônica caracterizada pelo desgaste progressivo da cartilagem articular do joelho, remodelação óssea (osteófitos) e inflamação sinovial secundária.",
        "clinica": "Degradação da matriz extracelular da cartilagem hialina nos compartimentos tibiofemoral e/ou patelofemoral, levando à perda do espaço articular e fricção osso com osso, gerando esclerose subcondral e dor periosteal.",
        "sintomas": ["Dor mecânica (piora ao carregar peso ou caminhar e alivia com repouso)", "Rigidez articular matinal temporária (geralmente dura menos de 30 minutos)", "Crepitação palpável ou audível e redução da amplitude de movimento."],
        "testes": ["Teste de estresse em varo/valgo", "Teste de compressão patelar (Clarke)", "Palpação das interlinhas articulares"],
        "tratamento_agudo": "Modulação da dor com recursos térmicos (calor na fase crônica para diminuir rigidez), hidroterapia para redução do impacto gravitacional e eletroanalgesia.",
        "tratamento_cronico": "Fortalecimento progressivo do quadríceps (essencial para absorção de carga), alongamento de isquiotibiais e tríceps sural, e treino de equilíbrio/propriocepção para estabilizar dinamicamente.",
        "foto1": "joelho", "foto2": "joelho 1"
    },
    "4. Síndrome do Túnel do Carpo": {
        "definicao": "Neuropatia compressiva decorrente da compressão do nervo mediano à sua passagem pelo canal osteofibroso do carpo na região anterior do punho.",
        "clinica": "O túnel do carpo é delimitado profundamente pelos ossos do carpo e superficialmente pelo retináculo dos flexores (ligamento carpal transverso). Qualquer processo inflamatório nos 9 tendões flexores reduz o espaço e comprime mecanicamente o nervo mediano.",
        "sintomas": ["Parestesia e hipoestesia na região palmar dos dedos polegar, indicador, médio e metade lateral do anular", "Piora noturna acentuada dos sintomas", "Fraqueza na pinça digital e atrofia da musculatura tenar em casos graves."],
        "testes": ["Teste de Phalen (flexão máxima dos punhos por 60 segundos)", "Sinal de Tinel (percussão leve sobre o canal do carpo)"],
        "tratamento_agudo": "Uso de órtese de posicionamento noturno (punho em neutro), TENS para controle da dor e repouso de atividades manuais repetitivas.",
        "tratamento_cronico": "Mobilização manual dos ossos do carpo, exercícios de mobilização/deslizamento do nervo mediano, alongamento dos flexores do punho e dedos, orientações ergonômicas.",
        "foto1": "punho", "foto2": "punho1"
    },
    "5. Fascite Plantar": {
        "definicao": "Processo degenerativo ou inflamatório da fáscia plantar (aponeurose) decorrente de microtraumas repetitivos na sua inserção proximal no calcâneo.",
        "clinica": "A fáscia plantar estende-se da tuberosidade medial do calcâneo até as bases das falanges proximais. Sob sobrecarga mecânica (como obesidade, pé plano/cavo ou calçados inadequados), há microrrupturas e espessamento do tecido conjuntivo próximo à sua origem óssea.",
        "sintomas": ["Dor aguda e intensa na região plantar interna do calcanhar logo ao dar os primeiros passos pela manhã", "Dor que tende a diminuir após os primeiros minutos de marcha", "Piora acentuada no final do dia após esforço ou ortostatismo prolongado."],
        "testes": ["Teste do Molinete (Windlass Test)", "Palpação focalizada na tuberosidade medial do calcâneo"],
        "tratamento_agudo": "Crioterapia local (rolar garrafa de gelo sob o pé), liberação miofascial plantar manual ou com instrumentos, aplicação de bandagem funcional (tapping) para suporte do arco.",
        "tratamento_cronico": "Alongamentos excêntricos e estáticos do complexo gastrocnêmio-sóleo e da própria fáscia, e fortalecimento da musculatura intrínseca do pé (recolher a toalha com os dedos).",
        "foto1": "pe", "foto2": "pe1"
    },
    "6. Lesão do Ligamento Cruzado Anterior (LCA)": {
        "definicao": "Ruptura parcial ou completa do LCA, principal estabilizador primário contra a translação tibial anterior e estresse rotacional do joelho, comum em entorses esportivos.",
        "clinica": "O LCA cruza o interior da articulação do joelho. Sua lesão ocorre tipicamente por mecanismo de desaceleração com mudança brusca de direção e o pé fixo ao solo, gerando pivotamento forçado para fora.",
        "sintomas": ["Estalo audível no momento da lesão seguido de sensação de falseio articular", "Edema intra-articular imediato (hemartrose nas primeiras horas)", "Dor intensa e incapacidade funcional de apoiar o peso do corpo."],
        "testes": ["Teste de Lachman (mais sensível)", "Teste da Gaveta Anterior", "Pivot-Shift Test"],
        "tratamento_agudo": "Controle do quadro álgico e do edema (protocolo PRICE: proteção, repouso, gelo, compressão e elevação), uso de muletas e crioterapia.",
        "tratamento_cronico": "Fortalecimento intensivo de isquiotibiais (sinergistas funcionais do LCA), quadríceps e tríceps sural, associado a um treino rigoroso de propriocepção e ganho de amplitude de movimento.",
        "foto1": "lca", "foto2": "lca1"
    },
    "7. Entorse de Tornozelo (Inversão)": {
        "definicao": "Lesão por estiramento ou ruptura dos ligamentos da região lateral do tornozelo (principalmente talofibular anterior) devido ao movimento excessivo de inversão.",
        "clinica": "Ocorre quando o pé dobra excessivamente para dentro com a planta voltada para o outro pé. Oligamento talofibular anterior é o mais fraco do complexo lateral e o primeiro a sofrer estiramento ou ruptura.",
        "sintomas": ["Dor na linha articular lateral do tornozelo", "Equimose (mancha roxa) e edema localizados nas primeiras 24 horas", "Dificuldade importante para realizar a marcha ou descarregar peso no calcanhar."],
        "testes": ["Teste da Gaveta Anterior do Tornozelo", "Teste do Estresse em Inversão (Talar Tilt)"],
        "tratamento_agudo": "Aplicação imediata de crioterapia, compressão elástica para controle do edema, elevação do membro e repouso relativo com descarga de peso conforme tolerância.",
        "tratamento_cronico": "Exercícios de fortalecimento de fibulares (eversores), ganho de amplitude em dorsiflexão e treinamento proprioceptivo em superfícies instáveis (disco de equilíbrio) para prevenção de instabilidade crônica.",
        "foto1": "tornozelo", "foto2": "tornozelo1"
    },
