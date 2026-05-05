import tensorflow as tf
import os

# Carregar o modelo treinado
model = tf.keras.models.load_model('model.h5')

# Converter para TensorFlow Lite com Dynamic Range Quantization
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]  # Dynamic Range Quantization

# Converter o modelo
tflite_model = converter.convert()

# Salvar o modelo otimizado
with open('model.tflite', 'wb') as f:
    f.write(tflite_model)

print("Modelo otimizado salvo como model.tflite")
