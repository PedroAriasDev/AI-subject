# Guía de Uso - AG Optimizado para WSL

## Problema Resuelto

El algoritmo genético original causaba que WSL/Ubuntu se corrompiera por consumo excesivo de memoria. Esta versión optimizada soluciona ese problema.

## Cambios Principales

### 1. Parámetros Reducidos
- **Población**: 100 → **30** (70% menos memoria)
- **Generaciones**: 20 → **10** por ejecución
- **Epochs**: 30 → **20**
- **Batch size**: 64 → **32**

### 2. Sistema de Checkpoints
Después de cada generación se guardan:
- `ag_checkpoint.pkl` - Estado completo del AG
- `best_model_config_temp.json` - Mejor configuración actual (cada 2 gen)

### 3. Limpieza Agresiva de Memoria
- `gc.collect()` después de cada individuo
- `tf.keras.backend.clear_session()` periódicamente
- Liberación explícita de objetos

## Cómo Usar

### Primera Ejecución

```python
# En el notebook, ejecutar la celda del AG:
best_individual, ga_history = genetic_algorithm(
    X_train_repr, y_train_repr, X_test_repr, y_test_repr,
    mae_baseline=mae_baseline,
    population_size=30,
    generations=10,
    resume_from_checkpoint=True
)
```

Esto ejecutará 10 generaciones y guardará checkpoints.

### Si WSL se Cae

1. **Reinicia WSL/Ubuntu**
2. **Abre el notebook de nuevo**
3. **Ejecuta SOLO la celda del AG** (la que tiene `genetic_algorithm(...)`)
4. El AG se reanudará automáticamente desde la última generación completada

### Ejecutar Más Generaciones

Si quieres 20 generaciones totales:
1. Ejecuta la celda del AG (hace 10 generaciones)
2. Vuelve a ejecutar la misma celda (hace 10 más, total 20)

El checkpoint se actualiza automáticamente.

## Archivos Generados

### Durante el Entrenamiento
- `ag_checkpoint.pkl` - Estado actual del AG
- `best_model_config_temp.json` - Mejor config temporal

### Al Finalizar
- `best_model_config.json` - Configuración final óptima
- `genetic_algorithm_evolution.png` - Gráfico de evolución

## Ventajas

✅ **No se pierde progreso** - Checkpoint después de cada generación
✅ **WSL no se cae** - Uso de memoria controlado
✅ **Pausable** - Puedes detener y reanudar cuando quieras
✅ **Flexible** - Ejecuta las generaciones que necesites
✅ **Automático** - Todo se guarda y carga solo

## Monitoreo

Durante la ejecución verás:
```
--- Generación 5/10 ---
  Evaluados: 30/30
  MAE: 1234.5678 | Fitness: 0.000810 | Tiempo: 45.2s
  3 capas: [128, 64, 32], relu
  ✓ Checkpoint guardado: generación 5
  ✓ Config temporal guardada
```

## Si Algo Sale Mal

1. **Checkpoint corrupto**: Elimina `ag_checkpoint.pkl` y empieza de nuevo
2. **Error de memoria**: Reduce más la población a 20
3. **WSL sigue cayendo**: Ejecuta solo 5 generaciones por vez

## Tiempos Estimados (WSL típico)

- **1 individuo**: ~15-30 segundos
- **1 generación (30 ind)**: ~8-15 minutos
- **10 generaciones**: ~1.5-2.5 horas

## Recomendaciones

1. **Cierra otras aplicaciones** mientras entrena
2. **No uses WSL para otra cosa** durante el entrenamiento
3. **Monitorea la RAM** en el administrador de tareas de Windows
4. **Si llega a 90% RAM**, detén y reinicia

## Ejemplo Completo

```bash
# Terminal 1: Monitorear memoria
watch -n 5 free -h

# Terminal 2: Ejecutar notebook
jupyter notebook
```

En el notebook:
1. Ejecutar celdas hasta el AG
2. Ejecutar celda del AG
3. Esperar 1-2 horas
4. Si se interrumpe, volver a ejecutar celda del AG
5. Al completar, ejecutar celdas de visualización y guardado

## Notas Técnicas

- Los checkpoints usan `pickle` para serializar objetos Python
- No guardes el modelo de Keras en el checkpoint (muy pesado)
- El mejor individuo se guarda en cada generación
- La población completa se guarda para permitir reproducción

---

**Autor**: Claude AI
**Fecha**: 2025
**Versión**: 2.0 - Optimizada para WSL
