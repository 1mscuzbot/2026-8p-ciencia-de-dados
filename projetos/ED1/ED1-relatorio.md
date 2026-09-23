# Estudo Dirigido / Trabalho 1 — K-Nearest Neighbors

**Disciplina:** Ciência de Dados  
**Professor:** MSc. Sergio Luiz Marques Filho  
**Curso:** Bacharelado em Ciência da Computação — UTP  
**Prazo:** 24/09/2026  
**Aluno:** Lucas Müller Scuzziato  

**Enunciado:** `material/provas/ED1/2026-2_CienciaDeDados_Trabalho1_CC.pdf`  
**Base:** `material/provas/ED1/apples_and_oranges.csv`  
**Código-fonte:** `projetos/ED1/knn_apples_oranges.py`  
**Saída do programa:** `projetos/ED1/saida.txt`

---

## Objetivo

Aplicar o classificador **KNN** na base de maçãs e laranjas (`Weight`, `Size`, `Class`) e entregar:

| Item | O que foi feito |
|------|-----------------|
| **A** | Gráfico Weight × Size evidenciando as classes |
| **B** | Código-fonte Python (`knn_apples_oranges.py`) |
| **C** | Acurácia + matriz de confusão + análise |
| **D** | Previsões para valores **fora** da base |

---

## Base de dados

- **40 amostras** (20 `apple` + 20 `orange`)
- Features: `Weight` (peso) e `Size` (tamanho)
- Target: `Class` ∈ {apple, orange}

As classes formam dois grupos bem separados: laranjas concentram peso menor e tamanho menor; maçãs, peso e tamanho maiores. Isso favorece o KNN.

---

## A. Gráfico das classes

Arquivo: `figuras/A_scatter_classes.png`

No plano Weight × Size, as laranjas ficam no canto inferior-esquerdo e as maçãs no superior-direito, com pouca sobreposição. Visualmente já dá para ver que um classificador por vizinhos próximos deve acertar bem.

---

## B. Código-fonte (resumo da solução)

Bibliotecas: `pandas`, `matplotlib`, `scikit-learn`.

1. Ler o CSV  
2. Plotar as classes (item A)  
3. Separar treino/teste com `train_test_split` (30% teste, `stratify`, `random_state=42`)  
4. Treinar `KNeighborsClassifier(n_neighbors=5, metric="euclidean")`  
5. Avaliar acurácia e matriz de confusão (item C)  
6. Classificar 5 pontos novos (item D)

Trecho central:

```python
X = df[["Weight", "Size"]]
y = df["Class"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)
modelo = KNeighborsClassifier(n_neighbors=5, metric="euclidean")
modelo.fit(X_train, y_train)
y_pred = modelo.predict(X_test)
```

---

## C. Métricas e matriz de confusão

| Configuração | Valor |
|--------------|-------|
| K | 5 |
| Distância | Euclidiana |
| Treino / teste | 28 / 12 |
| **Acurácia** | **100% (1,0000)** |

### Matriz de confusão (conjunto de teste)

| Real \ Predito | apple | orange |
|----------------|------:|-------:|
| **apple** | 6 | 0 |
| **orange** | 0 | 6 |

Arquivo: `figuras/C_matriz_confusao.png`

**Precision / Recall / F1** = 1,000 para as duas classes.

### Análise

- Com as classes bem separadas no gráfico A, o KNN com K=5 acertou todas as 12 amostras de teste.  
- Não houve FP nem FN: a matriz é diagonal.  
- Acurácia 100% neste split é coerente com a separação visual; em bases mais misturadas o resultado seria menor e K precisaria ser ajustado.  
- Limitação: a base é pequena (40 linhas). O resultado é bom para a tarefa, mas não garante o mesmo desempenho em dados reais maiores ou com sobreposição.

---

## D. Previsões para valores novos

Pontos **não presentes** no CSV, classificados pelo modelo treinado:

| Weight | Size | Classe prevista |
|-------:|-----:|-----------------|
| 66 | 4,2 | orange |
| 71 | 5,4 | apple |
| 68 | 4,9 | orange |
| 74 | 5,6 | apple |
| 72 | 4,5 | apple |

Arquivo: `figuras/D_previsoes_novas.png` (novos pontos marcados com **X**).

Os resultados seguem o padrão visto no gráfico A: peso/tamanho baixos → laranja; altos → maçã. O ponto `(72, 4.5)` fica numa região intermediária de tamanho, mas o peso alto puxa a votação dos vizinhos para `apple`.

---

## Como reproduzir

```bash
cd projetos/ED1
python knn_apples_oranges.py
```

Dependências: `pandas`, `scikit-learn`, `matplotlib`.

---

## Checklist de entrega (Teams)

1. Código-fonte: `knn_apples_oranges.py`  
2. Relatório (este arquivo) com gráficos, métricas, previsões e análise  
3. Saída do programa: `saida.txt`  
4. Figuras em `figuras/`
