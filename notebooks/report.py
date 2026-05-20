import marimo

__generated_with = "0.10.0"
app = marimo.App()

@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import matplotlib.pyplot as plt
    return mo, pd, plt

@app.cell
def _(pd):
    df = pd.read_csv("data/features/events.csv")
    df.head()
    return (df,)

@app.cell
def _(df, plt, mo):
    fig, ax = plt.subplots()
    ax.hist(df["duration_minutes"], bins=20, edgecolor="black")
    ax.set_xlabel("Duration (minutes)")
    ax.set_ylabel("Count")
    ax.set_title("Distribution of Event Durations")
    mo.pyplot(fig)
    return fig, ax