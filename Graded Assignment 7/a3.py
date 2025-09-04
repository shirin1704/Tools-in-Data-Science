# app.py
# Marimo interactive notebook
# Author: 23f2003577@ds.study.iitm.ac.in

import marimo # pyright: ignore[reportMissingImports]

app = marimo.App()


# Cell 1: Import libraries and create dataset
# -------------------------------------------
# This cell prepares the synthetic dataset that will be used in later cells.
@app.cell
def __():
    import numpy as np
    import pandas as pd

    # Generate synthetic dataset
    np.random.seed(42)
    x = np.linspace(0, 10, 100)
    y = 2 * x + np.random.normal(0, 2, size=100)  # Linear relationship with noise

    df = pd.DataFrame({"x": x, "y": y})
    df.head()
    return df, x, y
    


# Cell 2: Interactive slider
# ---------------------------
# This slider controls the slope (m) of the regression line that we will plot later.
@app.cell
def __():
    import marimo as mo # pyright: ignore[reportMissingImports]

    slope_slider = mo.ui.slider(start=0, stop=5, step=0.1, value=2, label="Adjust slope (m)")
    slope_slider
    return slope_slider
    


# Cell 3: Variable dependency on slider
# -------------------------------------
# This cell uses the slope value from the slider to compute predictions.
@app.cell
def __(slope_slider, x):
    m = slope_slider.value
    y_pred = m * x  # No intercept for simplicity
    (m, y_pred[:5])  # Show slope and first 5 predictions
    return m, y_pred
    


# Cell 4: Visualization
# ---------------------
# This cell depends on the dataset (df), slope (m), and predictions (y_pred).
# It demonstrates how changes in the slider dynamically update the plot.
@app.cell
def __(df, x, y, y_pred):
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()
    ax.scatter(x, y, alpha=0.6, label="Observed Data")
    ax.plot(x, y_pred, color="red", label="Fitted Line")
    ax.set_title("Interactive Linear Fit")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()
    fig
    return fig
    


# Cell 5: Dynamic Markdown
# ------------------------
# This cell creates dynamic Markdown text that updates when the slider moves.
@app.cell
def __(m):
    import marimo as mo # pyright: ignore[reportMissingImports]

    mo.md(f"### 📊 Current slope (m) = **{m:.2f}**  The fitted line updates dynamically with your adjustment.")
    


if __name__ == "__main__":
    app.run()