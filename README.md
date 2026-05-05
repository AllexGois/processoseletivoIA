# Desafio de Deep Learning: Classificação MNIST para TinyML

Este projeto apresenta a implementação de uma solução de Visão Computacional focada em **TinyML**, otimizada para execução em dispositivos de hardware limitado (Edge AI), como o microcontrolador **ESP32-S3**.

## 📋 Resumo do Desafio
O objetivo foi desenvolver uma Rede Neural Convolucional (CNN) capaz de classificar dígitos manuscritos (0-9) utilizando o dataset MNIST, respeitando restrições severas de engenharia para garantir a eficiência em sistemas embarcados.

## 🛠️ Requisitos Técnicos Obedecidos
De acordo com as restrições do projeto:
- **Arquitetura de Rede:** Implementação de uma CNN com menos de 3 camadas convolucionais para reduzir a carga computacional.
- **Processamento de Imagem:** Entradas normalizadas de 28x28 pixels em escala de cinza.
- **Otimização (TinyML):** Conversão do modelo para o formato `.tflite` utilizando **Quantização Inteira (int8)**.
- **Entrada/Saída Quantizada:** O modelo foi configurado para receber e entregar tensores do tipo `int8`, eliminando a necessidade de emulação de ponto flutuante no hardware alvo.

## 🧠 Estrutura da CNN
A rede foi desenhada com a seguinte hierarquia:
1.  **Conv2D (16 filtros, 3x3)** + MaxPooling2D.
2.  **Conv2D (32 filtros, 3x3)** + MaxPooling2D.
3.  **Flatten** + Camada Densa (32 neurônios).
4.  **Saída (Softmax)** com 10 classes.

## 📈 Resultados e Validação
Os resultados obtidos durante o treinamento e a validação técnica foram:
- **Acurácia de Validação:** ~98.82%.
- **Loss de Validação:** ~0.0375.
- **Status da Conversão:** Sucesso na geração do artefato quantizado para deploy imediato.

## 📂 Estrutura do Repositório
Seguindo a estrutura de projeto solicitada:
- `/models`: Contém o arquivo `modelo_quantizado.tflite`.
- `/src`: Códigos-fonte da aplicação.
- `/data`: Referências ao conjunto de dados MNIST.

## 🚀 Como utilizar
1. O modelo está pronto para ser integrado via biblioteca **TensorFlow Lite for Microcontrollers**.
2. Utilize o script de treinamento no Google Colab para replicar os resultados ou ajustar hiperparâmetros.

---
**Desenvolvido como parte do Desafio Técnico de Inteligência Artificial.**