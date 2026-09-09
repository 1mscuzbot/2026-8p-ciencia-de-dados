# Aula 3 — Regressão Linear

**Disciplina:** Ciência de Dados (Prof. MSc. Sergio Luiz Marques Filho)  
**Slide:** `material/slides/MachineLearning_Introducao Aula 3.pdf`

---

## Modelo

```
y(x) = β₀ + β₁·x
```

- `β₀`: intercepto  
- `β₁`: inclinação (quanto `y` muda quando `x` aumenta 1)  

Exemplo do slide (lucro × orçamento): `β₀ ≈ 30,68`, `β₁ ≈ 0,54`.

## Erro

Erro de um ponto: valor predito − valor observado.

**Erro quadrático médio (MSE):**

```
MSE = (1/n) · Σ (ŷᵢ − yᵢ)²
```

Quanto menor o MSE, melhor o ajuste (no conjunto considerado).

## Aplicação

**Petrol Consumption:** prever consumo de combustível (milhões de galões) em 48 estados dos EUA a partir de imposto, renda per capita, milhas pavimentadas e proporção com carteira.

Também citada no README: Boston House Prices.

---

- Anterior → [Aula 2 — KNN](estudo-aula02-knn.md) · Próxima → [Aula 4 — Regressão logística](estudo-aula04-regressao-logistica.md)
