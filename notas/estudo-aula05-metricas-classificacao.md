# Aula 5 — Métricas de erro de classificação

**Disciplina:** Ciência de Dados (Prof. MSc. Sergio Luiz Marques Filho)  
**Slide:** `material/slides/MachineLearning_Introducao Aula 5.pdf`

---

## Matriz de confusão (binária)

|  | Pred. positiva | Pred. negativa |
|--|----------------|----------------|
| **Real positiva** | TP | FN |
| **Real negativa** | FP | TN |

| Sigla | Significado |
|-------|-------------|
| **TP** | previu positivo e era positivo |
| **TN** | previu negativo e era negativo |
| **FP** | previu positivo e era negativo (erro tipo I) |
| **FN** | previu negativo e era positivo (erro tipo II) |

## Métricas

| Métrica | Fórmula (ideia) |
|---------|-----------------|
| **Acurácia** | (TP+TN) / total |
| **Precisão** | TP / (TP+FP) — “dos que marquei positivo, quantos acertei?” |
| **Recall (sensibilidade)** | TP / (TP+FN) — “dos positivos reais, quantos peguei?” |

Em classes desbalanceadas, acurácia sozinha **engana**.

## ROC e AUC

- **ROC:** curva taxa de verdadeiros positivos × taxa de falsos positivos ao variar o limiar.  
- **AUC:** área sob a ROC (quanto mais perto de 1, melhor separação).

---

- Anterior → [Aula 4](estudo-aula04-regressao-logistica.md) · Próxima → [Aula 6 — SVM e PLN](estudo-aula06-svm-e-pln.md)
