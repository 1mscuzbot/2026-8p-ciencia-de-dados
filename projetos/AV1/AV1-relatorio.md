# Prova Prática 1 / AV1 — Regressão Linear Simples

**Disciplina:** Ciência de Dados  
**Professor:** MSc. Sergio Luiz Marques Filho  
**Curso:** Bacharelado em Ciência da Computação — UTP  
**Tipo:** Prova prática individual (Tipo 1)  
**Aluno:** Lucas Müller Scuzziato  

**Enunciado:** `material/provas/AV1/2026-2_CienciaDeDados_ProvaPratica1.pdf`  
**Base:** `material/provas/AV1/student_scores.csv`  
**Código-fonte:** `projetos/AV1/regressao_student_scores.py`  
**Saída do programa:** `projetos/AV1/saida.txt`

---

## Objetivo

Aplicar **regressão linear simples** na base de horas de estudo × pontuação e entregar:

| Item | O que foi feito |
|------|-----------------|
| **A** | Gráfico Hours × Scores **com a reta** da regressão |
| **B** | Código-fonte Python (`regressao_student_scores.py`) |
| **C** | Métricas de acerto do modelo + coeficientes β₀ e β₁ |
| **D** | Previsões para horas diferentes das da base |

---

## Base de dados

- **25 amostras**
- Variável independente: `Hours` (horas de estudo)  
- Variável dependente: `Scores` (nota/pontuação a prever)

| Estatística | Hours | Scores |
|-------------|------:|-------:|
| Média | 5,01 | 51,48 |
| Mínimo | 1,1 | 17 |
| Máximo | 9,2 | 95 |

Há relação crescente clara: mais horas → scores maiores.

---

## A. Gráfico + reta de regressão

Arquivo: `figuras/A_regressao_reta.png`

Os pontos formam uma nuvem alongada diagonal. A reta ajustada pelo modelo passa pelo meio dessa nuvem:

\[
\hat{y} = 2{,}83 + 9{,}68 \cdot x
\]

---

## B. Código-fonte (resumo da solução)

Bibliotecas: `pandas`, `numpy`, `matplotlib`, `scikit-learn`.

1. Ler o CSV  
2. Separar treino/teste (`test_size=0.2`, `random_state=42`)  
3. Ajustar `LinearRegression`  
4. Plotar dados + reta (item A)  
5. Reportar β₀, β₁, R², MSE, RMSE, MAE (item C)  
6. Prever scores para horas novas (item D)

Trecho central:

```python
X = df[["Hours"]]
y = df["Scores"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
modelo = LinearRegression()
modelo.fit(X_train, y_train)
beta0 = modelo.intercept_
beta1 = modelo.coef_[0]
```

---

## C. Coeficientes e métricas

### Coeficientes

| Coeficiente | Valor | Significado |
|-------------|------:|-------------|
| **β₀** (intercepto) | **2,8269** | Score previsto quando Hours = 0 |
| **β₁** (inclinação) | **9,6821** | Cada +1 hora eleva o score previsto em ≈ **9,68** pontos |

Modelo:

\[
\hat{y} = 2{,}8269 + 9{,}6821 \cdot \text{Hours}
\]

### Métricas no conjunto de teste (5 amostras)

| Métrica | Valor |
|---------|------:|
| **R²** | **0,9678** |
| MSE | 18,9432 |
| RMSE | 4,3524 |
| MAE | 3,9208 |

R² no conjunto completo (referência): **0,9528**.

### Comparação no teste

| Hours | Score real | Score previsto | Erro |
|------:|-----------:|---------------:|-----:|
| 8,3 | 81 | 83,19 | +2,19 |
| 2,5 | 30 | 27,03 | −2,97 |
| 2,5 | 21 | 27,03 | +6,03 |
| 6,9 | 76 | 69,63 | −6,37 |
| 5,9 | 62 | 59,95 | −2,05 |

### Análise

- R² ≈ 0,97 no teste indica que a reta explica bem a variação dos scores.  
- RMSE ≈ 4,4 pontos: o erro típico fica na casa de poucos pontos na escala 0–100.  
- O maior erro no teste (+6,03) ocorre em 2,5 h com score 21 (há outra amostra com 2,5 h e score 30): a mesma hora pode gerar notas diferentes, e a reta devolve um valor médio.  
- β₁ positivo confirma a relação direta horas → desempenho.

---

## D. Previsões para novos valores de Hours

Valores **diferentes** dos usados só para checagem (inclui extrapolação acima do máximo 9,2 h):

| Hours | Score previsto |
|------:|---------------:|
| 1,0 | 12,51 |
| 4,0 | 41,56 |
| 6,5 | 65,76 |
| 9,5 | 94,81 |
| 10,0 | 99,65 |

Arquivo: `figuras/D_previsoes_novas.png`.

Os pontos novos caem sobre a mesma reta. Em 10 h o modelo prevê ≈ 100 pontos — coerente com a inclinação, mas já é extrapolação fora do intervalo original (1,1–9,2).

---

## Como reproduzir

```bash
cd projetos/AV1
python regressao_student_scores.py
```

Dependências: `pandas`, `numpy`, `scikit-learn`, `matplotlib`.

---

## Checklist de entrega (Teams)

1. Respostas / relatório (este arquivo)  
2. Código-fonte: `regressao_student_scores.py`  
3. Saída do programa: `saida.txt` (ou print da tela)  
4. Figuras em `figuras/`
