# test_installation.py
"""
Script para verificar que todas las librerías estén correctamente instaladas
"""

import sys
print(f"Python version: {sys.version}")
print("-" * 50)

# Verificar librerías base
try:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    print("✓ Librerías base: OK")
except ImportError as e:
    print(f"✗ Error en librerías base: {e}")

# Verificar scikit-learn
try:
    import sklearn
    print(f"✓ Scikit-learn version: {sklearn.__version__}")
except ImportError as e:
    print(f"✗ Error en scikit-learn: {e}")

# Verificar lógica difusa
try:
    import skfuzzy as fuzz
    print("✓ Lógica difusa (scikit-fuzzy): OK")
except ImportError as e:
    print(f"✗ Error en lógica difusa: {e}")

# Verificar algoritmos genéticos
try:
    import deap
    print("✓ Algoritmos genéticos (DEAP): OK")
except ImportError as e:
    print(f"✗ Error en algoritmos genéticos: {e}")

# Verificar TensorFlow
try:
    import tensorflow as tf
    print(f"✓ TensorFlow version: {tf.__version__}")
    print(f"  GPU disponible: {tf.config.list_physical_devices('GPU')}")
except ImportError as e:
    print(f"✗ Error en TensorFlow: {e}")

# Verificar PyTorch
try:
    import torch
    print(f"✓ PyTorch version: {torch.__version__}")
    print(f"  CUDA disponible: {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print(f"  GPU: {torch.cuda.get_device_name(0)}")
except ImportError as e:
    print(f"✗ Error en PyTorch: {e}")

# Verificar JAX
try:
    import jax
    import jax.numpy as jnp
    print(f"✓ JAX disponible")
    print(f"  Dispositivos: {jax.devices()}")
except ImportError as e:
    print(f"✗ Error en JAX: {e}")

print("-" * 50)
print("Verificación completada!")