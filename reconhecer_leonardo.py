# -*- coding: utf-8 -*-
import cv2
import numpy as np
from deepface import DeepFace
import re

def reconhecer_leonardo(caminho_imagem):

    imagem_original_path = re.sub(r'\..*$', '', caminho_imagem) 

     # Carregar imagens
    imagem_a_reconhecer = cv2.imread(caminho_imagem)
    imagem_referencia = cv2.imread('imagens/leonardo1.jpg')

    # Definicoes do texto
    fonte = cv2.FONT_HERSHEY_SIMPLEX

    # Cria o texto baseado na identificação
    if DeepFace.verify(img1_path=imagem_referencia, img2_path=imagem_a_reconhecer)['verified']:
        texto = "Isso! o Leonardo!"
        cor = (255, 0, 0) # cor do texto em BGR (branco neste exemplo)
        escala_fonte = 3
        espessura_linha = 4
        posicao = (100, 80) # coordenadas (x, y) onde o texto será adicionado

    else:
        texto = "Errado! So pode ser o Ragnar!"
        cor = (0, 0, 255)
        escala_fonte = 1.5
        espessura_linha = 3
        posicao = (1, 50) # coordenadas (x, y) onde o texto será adicionado
    

    # Adicionar o texto à imagem
    imagem_com_texto = cv2.putText(imagem_a_reconhecer, texto, posicao, fonte, escala_fonte, cor, espessura_linha)

    cv2.imwrite(f'{imagem_original_path}_labeled.jpg', imagem_com_texto)

reconhecer_leonardo('imagens/leonardo2.jpg')
reconhecer_leonardo('imagens/ragnar.jpg')