# Tipo Tátil 
_[[Wiki](https://github.com/fegvilela/tipo-tatil/wiki) e [README](https://github.com/fegvilela/tipo-tatil/blob/master/README.md) em construção]_

Tipo Tátil é um produto de tecnologia assistiva cujo objetivo é introduzir o deficiente visual ao universo da tipografia.

O produto é composto por alfabeto e caracteres táteis (em MDF) disponíveis em várias tipografias diferentes e um software para guiar o usuário em sua jornada. 

Esse repositório contém o "core" do software: o sistema de reconhecimento e classificação das tipografias contidas no produto. 

## Tecnologias utilizadas

O sistema foi desenvolvido em Python, utilizando principalmente as bibliotecas [OpenCV](https://opencv.org/) (para manipulação das imagens e extração de features) e [scikit-learn](https://scikit-learn.org/stable/) (para treinamento dos modelos).

Para extração de features, o melhor resultado foi obtido com o algoritmo [LBP (Local Binary Pattern)](https://www.pyimagesearch.com/2015/12/07/local-binary-patterns-with-python-opencv/).

No treinamento do modelo, o melhor resultado foi com o algoritmo Random Forest, utilizando também K-Fold para a divisão de subconjuntos durante o processo.

## Dataset

O [dataset](https://github.com/fegvilela/tipo-tatil/tree/master/dataset) foi composto por cerca de 6 mil imagens relativas às nove tipografias contidas nessa fase do projeto. 

Esse dataset foi completamente construído pela equipe, utilizando Python para manipulação dos arquivos, limpeza e preparação das imagens. As imagens foram obtidas principalmente no [FontsInUse](https://fontsinuse.com/).

## Equipe

[@fegvilela](https://github.com/fegvilela) - desenvolvimento de software
[@lucianacruz](https://github.com/lucianacruz) - design do produto e product owner

