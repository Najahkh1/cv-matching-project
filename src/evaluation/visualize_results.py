import pandas as pd
import matplotlib.pyplot as plt


def plot_average_scores(results_df):
    """
    Plot gemiddelde similarity score per model.
    """
    avg_scores = results_df.groupby("model")["score"].mean()

    plt.figure(figsize=(6, 4))
    avg_scores.plot(kind="bar")
    plt.title("Gemiddelde similarity score per model")
    plt.xlabel("Model")
    plt.ylabel("Gemiddelde score")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig("results/average_scores_per_model.png")
    plt.close()


def plot_scores_per_resume(results_df):
    """
    Plot score per resume index voor beide modellen.
    """
    pivot_df = results_df.pivot(
        index="resume_index",
        columns="model",
        values="score"
    )

    plt.figure(figsize=(8, 5))
    pivot_df.plot(marker="o")
    plt.title("Similarity score per CV")
    plt.xlabel("Resume index")
    plt.ylabel("Similarity score")
    plt.tight_layout()
    plt.savefig("results/scores_per_resume.png")
    plt.close()


def plot_top_roles(results_df):
    """
    Plot hoe vaak rollen als top match voorkomen.
    """
    role_counts = results_df["role"].value_counts().head(10)

    plt.figure(figsize=(10, 5))
    role_counts.plot(kind="bar")
    plt.title("Meest voorkomende top-match rollen")
    plt.xlabel("Role")
    plt.ylabel("Aantal keer top match")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("results/top_roles.png")
    plt.close()


def main():
    results_df = pd.read_csv("results/model_evaluation.csv")

    plot_average_scores(results_df)
    plot_scores_per_resume(results_df)
    plot_top_roles(results_df)

    print("Visualisaties opgeslagen in results/:")
    print("- average_scores_per_model.png")
    print("- scores_per_resume.png")
    print("- top_roles.png")


if __name__ == "__main__":
    main()