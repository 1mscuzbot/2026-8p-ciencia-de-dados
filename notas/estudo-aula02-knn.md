# Aula 2 — K-Nearest Neighbors (KNN)

**Disciplina:** Ciência de Dados (Prof. MSc. Sergio Luiz Marques Filho)  
**Slide:** `material/slides/MachineLearning_Introducao Aula 2.pdf`

---

## Ideia

Classifica um ponto novo pelos **K vizinhos mais próximos** já rotulados (votação / média).

### Para modelar

1. Escolher **K**  
2. Escolher **métrica de distância**  
3. Features **quantificáveis** + labels conhecidos  

### Distâncias

| Métrica | Ideia |
|---------|--------|
| **Euclidiana** | √(Σ Δ²) — “linha reta” |
| **Manhattan** | Σ \|Δ\| — “quarteirões” |

### Características do KNN

- Fácil de treinar (só **armazena** os dados)  
- **Lento** na predição (muitas distâncias)  
- Pode consumir muita **memória** em datasets grandes  

## Treino × teste

1. Ajustar no **treino** (`fit`)  
2. Prever no **teste** (`predict`)  
3. Comparar com `y_test` → métrica de erro  

**Validação cruzada:** várias partições treino/teste para estimar desempenho de forma mais estável.

## Aplicações da aula

| Dataset | Objetivo |
|---------|----------|
| **Iris** | 3 espécies; 4 features (sépalas/pétalas em cm); 50 amostras/classe |
| **Pima Indians Diabetes** | 768 mulheres; 8 features clínicas; classe 0/1 (diabetes) |

---

- Anterior → [Aula 1](estudo-aula01-introducao-ml.md) · Próxima → [Aula 3 — Regressão linear](estudo-aula03-regressao-linear.md)
