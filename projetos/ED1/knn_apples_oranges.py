"""
Trabalho 1 / ED1 — K-Nearest Neighbors
Base: apples_and_oranges.csv (Weight, Size, Class)
Disciplina: Ciência de Dados — Prof. MSc. Sergio Luiz Marques Filho
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR.parent.parent / "material" / "provas" / "ED1" / "apples_and_oranges.csv"
FIG_DIR = BASE_DIR / "figuras"
OUT_TXT = BASE_DIR / "saida.txt"

K = 5
RANDOM_STATE = 42
TEST_SIZE = 0.3


def main() -> None:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    lines: list[str] = []

    def log(msg: str = "") -> None:
        print(msg)
        lines.append(msg)

    df = pd.read_csv(CSV_PATH)
    log("=== Base apples_and_oranges.csv ===")
    log(f"Amostras: {len(df)}")
    log(f"Colunas: {list(df.columns)}")
    log(f"Contagem por classe:\n{df['Class'].value_counts().to_string()}")
    log()
    log("Primeiras linhas:")
    log(df.head().to_string(index=False))
    log()

    # --- A. Gráfico das variáveis por classe ---
    fig, ax = plt.subplots(figsize=(7, 5))
    cores = {"apple": "#c0392b", "orange": "#e67e22"}
    for classe, grupo in df.groupby("Class"):
        ax.scatter(
            grupo["Weight"],
            grupo["Size"],
            c=cores.get(classe, "gray"),
            label=classe,
            s=70,
            edgecolors="black",
            linewidths=0.4,
        )
    ax.set_xlabel("Weight (peso)")
    ax.set_ylabel("Size (tamanho)")
    ax.set_title("A. Distribuição Weight × Size por classe")
    ax.legend(title="Class")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "A_scatter_classes.png", dpi=150)
    plt.close(fig)
    log("Gráfico A salvo em figuras/A_scatter_classes.png")

    X = df[["Weight", "Size"]]
    y = df["Class"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE, stratify=y
    )

    modelo = KNeighborsClassifier(n_neighbors=K, metric="euclidean")
    modelo.fit(X_train, y_train)
    y_pred = modelo.predict(X_test)

    # --- C. Métricas e matriz de confusão ---
    acc = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred, labels=["apple", "orange"])
    report = classification_report(y_test, y_pred, digits=3)

    log("=== C. Desempenho no conjunto de teste ===")
    log(f"K = {K} | distância = euclidiana | test_size = {TEST_SIZE}")
    log(f"Treino: {len(X_train)} | Teste: {len(X_test)}")
    log(f"Acurácia: {acc:.4f} ({acc * 100:.2f}%)")
    log()
    log("Matriz de confusão (linhas = real, colunas = predito)")
    log("          pred_apple  pred_orange")
    log(f"apple     {cm[0, 0]:10d}  {cm[0, 1]:11d}")
    log(f"orange    {cm[1, 0]:10d}  {cm[1, 1]:11d}")
    log()
    log("Relatório de classificação:")
    log(report)

    fig, ax = plt.subplots(figsize=(5, 4))
    im = ax.imshow(cm, cmap="Oranges")
    ax.set_xticks([0, 1], ["apple", "orange"])
    ax.set_yticks([0, 1], ["apple", "orange"])
    ax.set_xlabel("Predito")
    ax.set_ylabel("Real")
    ax.set_title("C. Matriz de confusão (teste)")
    for i in range(2):
        for j in range(2):
            ax.text(j, i, str(cm[i, j]), ha="center", va="center", fontsize=14, fontweight="bold")
    fig.colorbar(im, ax=ax, fraction=0.046)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "C_matriz_confusao.png", dpi=150)
    plt.close(fig)
    log("Gráfico C salvo em figuras/C_matriz_confusao.png")

    # --- D. Previsões fora da base ---
    novos = pd.DataFrame(
        {
            "Weight": [66, 71, 68, 74, 72],
            "Size": [4.20, 5.40, 4.90, 5.60, 4.50],
        }
    )
    pred_novos = modelo.predict(novos)
    novos_out = novos.copy()
    novos_out["Class_prevista"] = pred_novos

    log("=== D. Previsões para novos valores (fora do CSV) ===")
    log(novos_out.to_string(index=False))
    log()

    fig, ax = plt.subplots(figsize=(7, 5))
    for classe, grupo in df.groupby("Class"):
        ax.scatter(
            grupo["Weight"],
            grupo["Size"],
            c=cores.get(classe, "gray"),
            label=f"treino/base: {classe}",
            s=55,
            alpha=0.7,
            edgecolors="black",
            linewidths=0.3,
        )
    for classe in ["apple", "orange"]:
        sub = novos_out[novos_out["Class_prevista"] == classe]
        if len(sub) == 0:
            continue
        ax.scatter(
            sub["Weight"],
            sub["Size"],
            c=cores[classe],
            marker="X",
            s=140,
            label=f"novo→{classe}",
            edgecolors="black",
            linewidths=0.8,
        )
    ax.set_xlabel("Weight (peso)")
    ax.set_ylabel("Size (tamanho)")
    ax.set_title("D. Novos pontos classificados pelo KNN")
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "D_previsoes_novas.png", dpi=150)
    plt.close(fig)
    log("Gráfico D salvo em figuras/D_previsoes_novas.png")
    log("Concluído.")

    OUT_TXT.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
