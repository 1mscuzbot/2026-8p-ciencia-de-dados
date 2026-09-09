# Aula 4 — Regressão Logística

**Disciplina:** Ciência de Dados (Prof. MSc. Sergio Luiz Marques Filho)  
**Slide:** `material/slides/MachineLearning_Introducao Aula 4.pdf`

---

## Ideia

Usa a forma linear por dentro, mas passa pela **sigmoide** para obter probabilidade ∈ (0, 1) — classificação.

```
σ(z) = 1 / (1 + e^(-z))
z = β₀ + β₁·x + …
```

Limiar típico: se `σ(z) > 0,5` → uma classe; senão → outra (o slide ilustra com “sobreviveu / não”).

> Nome “regressão”, mas a tarefa é **classificação**.

## Aplicações

| Dataset | Objetivo |
|---------|----------|
| **Marks** | 2 notas de exame → admitido (1) ou não (0) |
| **MNIST** | dígitos 0–9 manuscritos, imagens 28×28 (`sklearn.datasets`) |

---

- Anterior → [Aula 3](estudo-aula03-regressao-linear.md) · Próxima → [Aula 5 — Métricas](estudo-aula05-metricas-classificacao.md)
