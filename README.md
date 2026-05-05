# Classificação de Dígitos MNIST com CNN e Otimização para Edge AI

## Descrição

Este projeto implementa um modelo de Visão Computacional para classificar dígitos manuscritos (0-9) do dataset MNIST usando uma Rede Neural Convolucional (CNN). O modelo é treinado em Python com TensorFlow/Keras e posteriormente otimizado para execução em dispositivos Edge usando TensorFlow Lite com Dynamic Range Quantization.

## Estrutura do Projeto

- `train_model.py`: Script para carregar o dataset MNIST, pré-processar os dados, construir e treinar a CNN, avaliar a acurácia e salvar o modelo em formato Keras (.h5).
- `optimize_model.py`: Script para carregar o modelo treinado (.h5), converter para TensorFlow Lite (.tflite) com otimização de quantização dinâmica, e salvar o modelo otimizado.
- `requirements.txt`: Lista de dependências Python necessárias.
- `model.h5`: Arquivo do modelo treinado gerado pelo `train_model.py`.
- `model.tflite`: Arquivo do modelo otimizado gerado pelo `optimize_model.py`.
- `README.md`: Este arquivo de documentação.

## Como Executar

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

2. Execute o treinamento do modelo:
   ```bash
   python train_model.py
   ```
   Isso irá treinar a CNN no dataset MNIST e salvar o modelo como `model.h5`, exibindo a acurácia final no terminal.

3. Execute a otimização do modelo:
   ```bash
   python optimize_model.py
   ```
   Isso irá carregar `model.h5`, converter para TensorFlow Lite com Dynamic Range Quantization e salvar como `model.tflite`.

## Arquitetura do Modelo

A Rede Neural Convolucional implementada tem a seguinte estrutura:

- **Entrada**: Imagens de 28x28 pixels em escala de cinza (reshaped para 28x28x1).
- **Camada Convolucional 1**: 32 filtros de 3x3, ativação ReLU.
- **Pooling 1**: MaxPooling de 2x2.
- **Camada Convolucional 2**: 64 filtros de 3x3, ativação ReLU.
- **Pooling 2**: MaxPooling de 2x2.
- **Flatten**: Converte a saída 2D em vetor 1D.
- **Camada Densa 1**: 64 neurônios, ativação ReLU.
- **Camada de Saída**: 10 neurônios (um para cada dígito), ativação Softmax.

O modelo é compilado com otimizador Adam, loss sparse_categorical_crossentropy e métrica de acurácia.

## Pré-processamento dos Dados

- Carregamento do dataset MNIST via TensorFlow.
- Normalização dos pixels: divisão por 255.0 para escala [0,1].
- Reshape das imagens para formato adequado à CNN.

## Resultados

- **Acurácia no conjunto de teste**: Aproximadamente 98.39%.
- O modelo foi treinado com 1 época para demonstração, mas pode ser ajustado para mais épocas se necessário.

## Otimização para Edge AI

- **Técnica utilizada**: Dynamic Range Quantization.
- **Objetivo**: Reduzir o tamanho do modelo e acelerar a inferência, mantendo desempenho adequado para dispositivos embarcados e IoT.
- O modelo .tflite resultante é compatível com TensorFlow Lite Interpreter em plataformas como Raspberry Pi, ESP32, etc.

## Dependências

- TensorFlow >= 2.12
- NumPy

## Notas

- O treinamento é realizado em CPU.
- O código foi desenvolvido para ser executado de forma automatizada, sem intervenção manual.
- Este projeto demonstra o fluxo completo: treinamento → salvamento → conversão → otimização para Edge AI.