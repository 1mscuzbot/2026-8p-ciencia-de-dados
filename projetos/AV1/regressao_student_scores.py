"""
Prova Prática 1 / AV1 — Regressão Linear Simples
Base: student_scores.csv (Hours = independente, Scores = dependente)
Disciplina: Ciência de Dados — Prof. MSc. Sergio Luiz Marques Filho
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR.parent.parent / "material" / "provas" / "AV1" / "student_scores.csv"
FIG_DIR = BASE_DIR / "figuras"
OUT_TXT = BASE_DIR / "saida.txt"

RANDOM_STATE = 42
TEST_SIZE = 0.2


def main() -> None:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    lines: list[str] = []

    def log(msg: str = "") -> None:
        try:
            print(msg)
        except UnicodeEncodeError:
            print(msg.encode("ascii", "replace").decode("ascii"))
        lines.append(msg)

    df = pd.read_csv(CSV_PATH)
    log("=== Base student_scores.csv ===")
    log(f"Amostras: {len(df)}")
    log(f"Colunas: {list(df.columns)}")
    log()
    log("Estatísticas descritivas:")
    log(df.describe().to_string())
    log()
    log("Primeiras linhas:")
    log(df.head().to_string(index=False))
    log()

    X = df[["Hours"]]
    y = df["Scores"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE
    )

    modelo = LinearRegression()
    modelo.fit(X_train, y_train)

    beta0 = float(modelo.intercept_)
    beta1 = float(modelo.coef_[0])

    y_pred_test = modelo.predict(X_test)
    y_pred_all = modelo.predict(X)

    mse = mean_squared_error(y_test, y_pred_test)
    rmse = float(np.sqrt(mse))
    mae = mean_absolute_error(y_test, y_pred_test)
    r2 = r2_score(y_test, y_pred_test)
    r2_all = r2_score(y, y_pred_all)

    # --- A. Grafico + reta ---
    x_linha = pd.DataFrame(
        {"Hours": np.linspace(df["Hours"].min() - 0.2, df["Hours"].max() + 0.2, 100)}
    )
    y_linha = modelo.predict(x_linha)

    fig, ax = plt.subplots(figsize=(7, 5))
    ax.scatter(df["Hours"], df["Scores"], c="#2980b9", s=70, edgecolors="black", linewidths=0.4, label="Dados")
    ax.plot(
        x_linha["Hours"],
        y_linha,
        color="#c0392b",
        linewidth=2,
        label=f"Reta: y = {beta0:.2f} + {beta1:.2f}*x",
    )
    ax.set_xlabel("Hours (horas de estudo) - variavel independente")
    ax.set_ylabel("Scores - variavel dependente")
    ax.set_title("A. Regressao linear: Hours x Scores")
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "A_regressao_reta.png", dpi=150)
    plt.close(fig)
    log("Grafico A salvo em figuras/A_regressao_reta.png")

    # --- C. Coeficientes e métricas ---
    log("=== C. Coeficientes e metricas ===")
    log("Modelo: y_hat = beta0 + beta1 * x")
    log(f"beta0 (intercepto): {beta0:.6f}")
    log(f"beta1 (inclinacao): {beta1:.6f}")
    log(f"Interpretacao: a cada +1 hora de estudo, o score previsto sobe cerca de {beta1:.2f} pontos.")
    log()
    log(f"Treino: {len(X_train)} | Teste: {len(X_test)} | test_size={TEST_SIZE}")
    log("--- No conjunto de teste ---")
    log(f"R2 (coef. de determinacao): {r2:.4f}")
    log(f"MSE (erro quadratico medio): {mse:.4f}")
    log(f"RMSE: {rmse:.4f}")
    log(f"MAE (erro absoluto medio): {mae:.4f}")
    log()
    log(f"R2 no conjunto completo (referencia): {r2_all:.4f}")
    log()
    log("Comparacao no teste (Hours | Score real | Score previsto | erro):")
    for h, real, pred in zip(X_test["Hours"].values, y_test.values, y_pred_test):
        log(f"  {h:4.1f} h | {real:5.1f} | {pred:6.2f} | erro={pred - real:+6.2f}")

    # --- D. Previsoes novas ---
    novos = pd.DataFrame({"Hours": [1.0, 4.0, 6.5, 9.5, 10.0]})
    scores_novos = modelo.predict(novos)
    novos["Score_previsto"] = np.round(scores_novos, 2)

    log()
    log("=== D. Previsoes para horas fora / diferentes da base ===")
    log(novos.to_string(index=False))
    log()

    fig, ax = plt.subplots(figsize=(7, 5))
    ax.scatter(df["Hours"], df["Scores"], c="#2980b9", s=60, alpha=0.75, edgecolors="black", linewidths=0.3, label="Dados")
    ax.plot(x_linha["Hours"], y_linha, color="#c0392b", linewidth=2, label="Reta ajustada")
    ax.scatter(
        novos["Hours"],
        novos["Score_previsto"],
        c="#27ae60",
        marker="X",
        s=140,
        edgecolors="black",
        linewidths=0.8,
        label="Novas previsoes",
        zorder=5,
    )
    for _, row in novos.iterrows():
        ax.annotate(
            f"{row['Score_previsto']:.1f}",
            (row["Hours"], row["Score_previsto"]),
            textcoords="offset points",
            xytext=(6, 6),
            fontsize=8,
        )
    ax.set_xlabel("Hours (horas de estudo)")
    ax.set_ylabel("Scores")
    ax.set_title("D. Previsoes para novos valores de Hours")
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "D_previsoes_novas.png", dpi=150)
    plt.close(fig)
    log("Grafico D salvo em figuras/D_previsoes_novas.png")
    log("Concluido.")

    OUT_TXT.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
