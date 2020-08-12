# Tipo Tátil 
[Wiki e README em construção]

Tipo Tátil é um produto de tecnologia assistiva cujo objetivo é introduzir o deficiente visual ao universo da tipografia.

O produto é composto por alfabeto e caracteres táteis (em MDF) disponíveis em várias tipografias diferentes e um software para guiar o usuário em sua jornada. 

Esse repositório contém o "core" do software: o sistema de reconhecimento e classificação das tipografias contidas no produto. 

## Tecnologias utilizadas

O sistema foi desenvolvido em Python, utilizando principalmente as bibliotecas OpenCV (para manipulação das imagens e extração de features) e scikit-learn (para treinamento dos modelos).

Para extração de features, o melhor resultado foi obtido com o algoritmo LBP (Local Binary Pattern).

No treinamento do modelo, o melhor resultado foi com o algoritmo Random Forest, utilizando também K-Fold para a divisão de subconjuntos durante o processo.

## Dataset

O dataset foi composto por cerca de 6 mil imagens relativas às nove tipografias contidas nessa fase do projeto. 

Esse dataset foi completamente construído pela equipe, utilizando Python para manipulação dos arquivos, limpeza e preparação das imagens. As imagens foram obtidas principalmente no FontsInUse.

## Equipe

@fegvilela - desenvolvimento de software
@lucruz - design do produto e product owner

