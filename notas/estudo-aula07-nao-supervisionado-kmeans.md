# Aula 7 — Aprendizado não-supervisionado e K-Means

**Disciplina:** Ciência de Dados (Prof. MSc. Sergio Luiz Marques Filho)  
**Slide:** `material/slides/MachineLearning_Introducao Aula 7.pdf`

---

## Diferença-chave

Pontos **sem rótulo** (saída desconhecida). O modelo procura **estrutura** nos dados.

| Tipo | Objetivo |
|------|----------|
| **Clustering** | agrupar exemplos semelhantes |
| **Redução de dimensionalidade** | simplificar features mantendo estrutura |

## K-Means

1. Escolher **K** centroides  
2. Cada ponto → centroide mais próximo  
3. Recalcular centroides; repetir até estabilizar  

**Inércia:** soma das distâncias aos centroides — tende a cair quando K sobe. Usada para ajudar a escolher K (cotovelo / elbow).

Fluxo: dados sem label → `fit` → estrutura → novos dados mapeados aos clusters (`predict`).

## Aplicações

- Agrupamento **MNIST** (dígitos sem usar o rótulo no treino não-supervisionado)  
- **Séries temporais** (ex.: passagens aéreas) — citadas no módulo

---

## Pandas / Data Cleaning (material extra no repo)

Arquivos: `material/DATAFRAMES EM PYTHON.pdf` e `… DATA CLEANING.pdf`

- 30–40% do tempo de projeto em preparação de dados  
- Nulos: `dropna()`, `fillna()`  
- Erros: corrigir com `loc`  
- Duplicados: `drop_duplicates()`

---

- Anterior → [Aula 6](estudo-aula06-svm-e-pln.md) · Índice → [README](../README.md)
