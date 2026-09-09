# Ciência de Dados

**Universidade Tuiuti do Paraná — BCC**
**Professor:** MSc. Sergio Luiz Marques Filho
**Material:** Equipe no Microsoft Teams

## Estrutura
- `material/slides/` — slides das aulas
- `material/provas/` — provas e gabaritos
- `material/exercicios/` — listas de exercícios e notebooks
- `projetos/` — trabalhos práticos
- `notas/` — anotações e resumos

## Notas de estudo
- [Aula 1 — Introdução ao ML](notas/estudo-aula01-introducao-ml.md)
- [Aula 2 — KNN](notas/estudo-aula02-knn.md)
- [Aula 3 — Regressão linear](notas/estudo-aula03-regressao-linear.md)
- [Aula 4 — Regressão logística](notas/estudo-aula04-regressao-logistica.md)
- [Aula 5 — Métricas de classificação](notas/estudo-aula05-metricas-classificacao.md)
- [Aula 6 — SVM e PLN](notas/estudo-aula06-svm-e-pln.md)
- [Aula 7 — Não-supervisionado e K-Means](notas/estudo-aula07-nao-supervisionado-kmeans.md)

## Avaliação
- **Prova:** peso 7,0 (prova é PRÁTICA — participar das aulas é essencial)
- **Estudo Dirigido:** peso 3,0

## Conteúdo das aulas

### Aula Inaugural
- Regras da disciplina, uso de IA generativa
- Material disponibilizado no Teams
- Avaliação: prova prática 70% + estudo dirigido 30%

### Machine Learning — Introdução (7 aulas)
**Aula 1 — Introdução ao Aprendizado de Máquina**
- Tipos: supervisionado (saída conhecida) e não-supervisionado (saída desconhecida)
- Regressão (saída contínua) vs Classificação (saída categórica)
- Vocabulário: target, características, exemplo, label
- Google Colab, Pandas (DataFrames/Series)
- KNN, Regressão Linear/Logística, métricas, Árvores de Decisão, SVM, PLN, K-Means, séries temporais

**Aula 2 — K-Nearest Neighbors (KNN)**
- Distância Euclidiana e Manhattan
- Divisão treinamento/teste, validação cruzada
- Aplicações: Iris (classificação de flores) e Diabetes (Pima Indians)

**Aula 3 — Regressão Linear**
- Modelo: y(x) = β0 + β1·x
- Erro quadrático médio (MSE)
- Aplicações: Boston House Prices, Consumo de Combustível

**Aula 4 — Regressão Logística**
- Classificação com sigmoide: y = 1/(1+e^-x)
- Aplicações: Marks (admissão em universidades), MNIST (dígitos manuscritos)

**Aula 5 — Métricas de Erro de Classificação**
- Matriz de confusão (TP, TN, FP, FN; erros tipo I e II)
- Acurácia, Precisão, Recall
- Curva ROC e AUC

**Aula 6 — Support Vector Machine (SVM)**
- Hiperplano de separação: f(x) = w·x + b = 0
- Aplicações: Labeled Faces in the Wild, Breast Cancer Wisconsin
- **PLN:** tokenização, stemming, bag of words, cosine similarity, TF-IDF, análise de sentimentos (Tweets), South Park

**Aula 7 — Aprendizado não-supervisionado**
- Clustering e redução de dimensionalidade
- Algoritmo K-Means (inércia, escolha de K)
- Aplicação: agrupamento MNIST, séries temporais (passagens aéreas)

## Pandas — DataFrames em Python
- Estruturas: Series (1D) e DataFrame (2D)
- Leitura de CSV, ordenação, filtros, seleção de colunas/linhas (loc/iloc)
- Sumarização: count, sum, min, max, mean
- Gráficos: histograma (plot.hist), dispersão (plot.scatter)

### Data Cleaning (Limpeza de Dados)
- 30-40% do tempo de um projeto é gasto preparando dados
- Tratamento de dados nulos: `dropna()`, `fillna()`
- Correção de valores errados (`loc`), remoção de duplicados (`drop_duplicates`)

## Arquivos no repositório
| Arquivo | Descrição |
|---------|-----------|
| `material/slides/Aula Inaugural UTP.pdf` | Regras, avaliação e avisos da disciplina |
| `material/slides/MachineLearning_Introducao Aula 1-7.pdf` | 7 aulas de introdução a ML (sumário + exemplos) |
| `material/DATAFRAMES EM PYTHON.pdf` | Operações com DataFrames (pandas) |
| `material/DATAFRAMES EM PYTHON - DATA CLEANING.pdf` | Limpeza de dados (dropna, fillna, duplicados) |
| `material/exercicios/Aula30072026.ipynb` | Notebook da aula (Colab) |
| `material/exercicios/Datasets/student_scores.csv` | Dataset de exemplo (horas de estudo vs score) |

## Bases de dados usadas nas aulas
- Espécies de flores Iris | Diabetes (Pima Indians) | Câncer de Mama (Wisconsin)
- Preços de Residências (Boston) | Consumo de Combustível | Admissão em Universidades (Marks)
- Dígitos Manuscritos (MNIST) | Rostos de figuras públicas | Análise de Sentimentos (Tweets) | South Park | Passagens Aéreas
