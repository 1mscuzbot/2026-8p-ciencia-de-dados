# Aula 6 — SVM e Processamento de Linguagem Natural (PLN)

**Disciplina:** Ciência de Dados (Prof. MSc. Sergio Luiz Marques Filho)  
**Slide:** `material/slides/MachineLearning_Introducao Aula 6.pdf`

---

## Support Vector Machine (SVM)

Busca um **hiperplano** que separa classes com a maior margem possível:

```
f(x) = w·x + b = 0
```

- Vetores de suporte = pontos que “definem” a margem.  
- Com kernel, separa casos não linearmente separáveis no espaço original.

### Aplicações citadas

- **Labeled Faces in the Wild** (rostos)  
- **Breast Cancer Wisconsin**

---

## PLN (visão do slide)

| Conceito | Ideia |
|----------|--------|
| **Tokenização** | quebrar texto em unidades (palavras/tokens) |
| **Stemming** | reduzir à raiz |
| **Bag of Words** | documento = “saco” de contagens; ignora ordem |
| **CountVectorizer** | matriz documento–termo (frequências) |
| **Cosine similarity** | similaridade pelo cosseno entre vetores |
| **TF-IDF** | pesa termos frequentes no doc e raros no corpus |

Exemplos: análise de sentimentos em **tweets**; diálogos **South Park**.

---

- Anterior → [Aula 5](estudo-aula05-metricas-classificacao.md) · Próxima → [Aula 7 — Não-supervisionado](estudo-aula07-nao-supervisionado-kmeans.md)
