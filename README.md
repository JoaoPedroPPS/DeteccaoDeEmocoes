# Detecção de Emoções em Vídeos com Rosto Humano

Bem-vindo ao projeto de Detecção de Emoções em Vídeos com Rosto Humano! Este repositório contém um algoritmo que combina visão computacional e redes neurais para identificar expressões emocionais em vídeos.

## Sobre o Projeto

O objetivo principal deste projeto é criar uma ferramenta capaz de reconhecer emoções humanas em tempo real.

## Como Funciona

O algoritmo utiliza a detecção de rostos por meio da cascata de Haar para identificar áreas faciais nos vídeos. Em seguida, um modelo de rede neural, previamente treinado para reconhecimento de expressões faciais, entra em ação. Este modelo é capaz de classificar emoções como raiva, felicidade, tristeza, surpresa, entre outras.

## Como Usar

1. **Pré-requisitos:**
   - Certifique-se de ter as bibliotecas necessárias instaladas (OpenCV, TensorFlow, Keras).
   - Baixe os arquivos do modelo de rede neural (`fer.json` e `fer.h5`) e o arquivo XML para detecção de rostos (`haarcascade_frontalface_default.xml`).

2. **Execute o Código:**
   - Substitua o caminho do vídeo desejado em `video_path`.
   - Execute o script e observe o algoritmo em ação.

3. **Interpretação dos Resultados:**
   - O vídeo será exibido em uma janela, com os rostos destacados por retângulos coloridos.
   - As emoções identificadas serão sobrepostas aos rostos, proporcionando uma visualização intuitiva.

