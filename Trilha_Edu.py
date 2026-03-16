import streamlit as st
import pandas as pd
import os
from pathlib import Path

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Trilha do Respeito e Diversidade", layout="wide")

# Localiza a pasta onde o script está rodando (Crucial para o GitHub não dar tela branca)
caminho_base = Path(__file__).parent

# Estilo Visual (CSS)
st.markdown("""
    <style>
    [data-testid="stImage"] img { 
        border-radius: 50%; 
        width: 120px; 
        height: 120px; 
        object-fit: cover; 
        border: 4px solid #2ecc71;
    }
    .card-pergunta { 
        background-color: #f0f9ff; 
        padding: 25px; 
        border-radius: 20px; 
        text-align: center; 
        border-left: 10px solid #3498db;
        margin-bottom: 20px;
    }
    .stButton>button { 
        border-radius: 20px; 
        font-weight: bold; 
        height: 3.5em;
        background-color: #ffffff;
        border: 2px solid #3498db;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #3498db;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. PERSONAGENS (Caminhos revisados e corrigidos)
personagens = {
    "Ana": {"raca": "Branca", "path": str(caminho_base / "fotos" / "ana.jpg")},
    "Tiago": {"raca": "Negra", "path": str(caminho_base / "fotos" / "tiago.jpg")},
    "Léo": {"raca": "Branca", "path": str(caminho_base / "fotos" / "leo.jpg")},
    "Bia": {"raca": "Negra", "path": str(caminho_base / "fotos" / "bia.jpg")}
}

# 3. ESTADO DO JOGO (Memória do navegador)
if 'passo' not in st.session_state:
    st.session_state.passo = 0
if 'pontos' not in st.session_state:
    st.session_state.pontos = 0

# 4. LISTA DE SITUAÇÕES (Você pode aumentar essa lista depois!)
trilha = [
    {
        "texto": "Na hora do recreio, você percebe que ninguém chamou o Tiago para jogar bola. O que você faz?",
        "opcoes": ["Vou até ele e o convido para entrar no meu time.", "Continuo jogando com meus amigos de sempre."],
        "correta": 0
    },
    {
        "texto": "Um colega diz que o cabelo da Bia é 'estranho'. Como você reage?",
        "opcoes": ["Digo que o comentário foi chato e que o cabelo dela é lindo!", "Dou risada para não parecer o 'estranho' da turma."],
        "correta": 0
    },
    {
        "texto": "A professora quer ler um livro sobre heróis negros e indígenas. Qual sua reação?",
        "opcoes": ["Acho ótimo! Quero conhecer histórias novas e diferentes.", "Digo que prefiro as histórias que já conheço."],
        "correta": 0
    },
    {
        "texto": "Você vê um colega sendo tratado de forma injusta por um monitor. O que você faz?",
        "opcoes": ["Tento ajudar o colega ou aviso um professor sobre a injustiça.", "Não faço nada, pois não é comigo."],
        "correta": 0
    }
]

# --- LÓGICA DA INTERFACE ---
if st.session_state.passo < len(trilha):
    st.title("🏃‍♂️ Trilha do Respeito e da Amizade")
    st.write("Cada escolha correta ajuda a criar uma escola melhor!")
    
    # Barra de progresso visual
    progresso = (st.session_state.passo / len(trilha))
    st.progress(progresso)
    
    pergunta = trilha[st.session_state.passo]
    
    # Exibição da pergunta em destaque
    st.markdown(f'<div class="card-pergunta"><h2>🤔 O que você faria?</h2><p style="font-size: 20px;">{pergunta["texto"]}</p></div>', unsafe_allow_html=True)
    
    # Ex