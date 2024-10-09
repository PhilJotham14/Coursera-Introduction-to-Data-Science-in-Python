import matplotlib.pyplot as plt
import matplotlib.patches as patches


def draw_flowchart():
    fig, ax = plt.subplots(figsize=(15, 10))
    ax.axis("off")

    # Main components
    ax.text(
        0.5,
        0.95,
        "main.c",
        ha="center",
        va="center",
        fontsize=12,
        bbox=dict(facecolor="lightblue", edgecolor="black"),
    )
    ax.text(
        0.5,
        0.8,
        "Vehicle Type Calculation",
        ha="center",
        va="center",
        fontsize=12,
        bbox=dict(facecolor="lightgreen", edgecolor="black"),
    )
    ax.text(
        0.25,
        0.6,
        "calculateAmbulanceTaxes",
        ha="center",
        va="center",
        fontsize=12,
        bbox=dict(facecolor="lightyellow", edgecolor="black"),
    )
    ax.text(
        0.5,
        0.6,
        "calculateEstateTaxes",
        ha="center",
        va="center",
        fontsize=12,
        bbox=dict(facecolor="lightyellow", edgecolor="black"),
    )
    ax.text(
        0.75,
        0.6,
        "calculateSuvTaxes",
        ha="center",
        va="center",
        fontsize=12,
        bbox=dict(facecolor="lightyellow", edgecolor="black"),
    )
    ax.text(
        0.5,
        0.4,
        "calculateTrailerTaxes",
        ha="center",
        va="center",
        fontsize=12,
        bbox=dict(facecolor="lightyellow", edgecolor="black"),
    )
    ax.text(
        0.5,
        0.2,
        "calculateTransportMode",
        ha="center",
        va="center",
        fontsize=12,
        bbox=dict(facecolor="lightcoral", edgecolor="black"),
    )
    ax.text(
        0.5,
        0.1,
        "calculateParkingFees",
        ha="center",
        va="center",
        fontsize=12,
        bbox=dict(facecolor="lightcoral", edgecolor="black"),
    )

    # Arrows
    ax.annotate(
        "", xy=(0.5, 0.93), xytext=(0.5, 0.85), arrowprops=dict(arrowstyle="->", lw=1.5)
    )
    ax.annotate(
        "",
        xy=(0.25, 0.58),
        xytext=(0.5, 0.78),
        arrowprops=dict(arrowstyle="->", lw=1.5),
    )
    ax.annotate(
        "", xy=(0.5, 0.58), xytext=(0.5, 0.78), arrowprops=dict(arrowstyle="->", lw=1.5)
    )
    ax.annotate(
        "",
        xy=(0.75, 0.58),
        xytext=(0.5, 0.78),
        arrowprops=dict(arrowstyle="->", lw=1.5),
    )
    ax.annotate(
        "", xy=(0.5, 0.38), xytext=(0.5, 0.78), arrowprops=dict(arrowstyle="->", lw=1.5)
    )
    ax.annotate(
        "", xy=(0.5, 0.18), xytext=(0.5, 0.38), arrowprops=dict(arrowstyle="->", lw=1.5)
    )
    ax.annotate(
        "", xy=(0.5, 0.08), xytext=(0.5, 0.18), arrowprops=dict(arrowstyle="->", lw=1.5)
    )

    plt.show()


def draw_er_diagram():
    fig, ax = plt.subplots(figsize=(15, 10))
    ax.axis("off")

    # Entity-relationship diagram
    ax.text(
        0.2,
        0.9,
        "Vehicle",
        ha="center",
        va="center",
        fontsize=12,
        bbox=dict(facecolor="lightblue", edgecolor="black"),
    )
    ax.text(
        0.2,
        0.7,
        "Ambulance",
        ha="center",
        va="center",
        fontsize=12,
        bbox=dict(facecolor="lightgreen", edgecolor="black"),
    )
    ax.text(
        0.2,
        0.5,
        "Estate",
        ha="center",
        va="center",
        fontsize=12,
        bbox=dict(facecolor="lightgreen", edgecolor="black"),
    )
    ax.text(
        0.2,
        0.3,
        "SUV",
        ha="center",
        va="center",
        fontsize=12,
        bbox=dict(facecolor="lightgreen", edgecolor="black"),
    )
    ax.text(
        0.2,
        0.1,
        "Trailer",
        ha="center",
        va="center",
        fontsize=12,
        bbox=dict(facecolor="lightgreen", edgecolor="black"),
    )

    ax.text(
        0.6,
        0.9,
        "Tax",
        ha="center",
        va="center",
        fontsize=12,
        bbox=dict(facecolor="lightblue", edgecolor="black"),
    )
    ax.text(
        0.6,
        0.7,
        "Import Duty",
        ha="center",
        va="center",
        fontsize=12,
        bbox=dict(facecolor="lightgreen", edgecolor="black"),
    )
    ax.text(
        0.6,
        0.5,
        "VAT",
        ha="center",
        va="center",
        fontsize=12,
        bbox=dict(facecolor="lightgreen", edgecolor="black"),
    )
    ax.text(
        0.6,
        0.3,
        "Withholding Tax",
        ha="center",
        va="center",
        fontsize=12,
        bbox=dict(facecolor="lightgreen", edgecolor="black"),
    )
    ax.text(
        0.6,
        0.1,
        "Excise Duty",
        ha="center",
        va="center",
        fontsize=12,
        bbox=dict(facecolor="lightgreen", edgecolor="black"),
    )

    ax.text(
        0.9,
        0.7,
        "Other Fees",
        ha="center",
        va="center",
        fontsize=12,
        bbox=dict(facecolor="lightblue", edgecolor="black"),
    )
    ax.text(
        0.9,
        0.5,
        "Road Tolls",
        ha="center",
        va="center",
        fontsize=12,
        bbox=dict(facecolor="lightgreen", edgecolor="black"),
    )
    ax.text(
        0.9,
        0.3,
        "Border Fees",
        ha="center",
        va="center",
        fontsize=12,
        bbox=dict(facecolor="lightgreen", edgecolor="black"),
    )
    ax.text(
        0.9,
        0.1,
        "Parking Fees",
        ha="center",
        va="center",
        fontsize=12,
        bbox=dict(facecolor="lightgreen", edgecolor="black"),
    )

    # Relationships
    ax.plot([0.2, 0.6], [0.85, 0.85], "k-")
    ax.plot([0.2, 0.6], [0.65, 0.65], "k-")
    ax.plot([0.2, 0.6], [0.45, 0.45], "k-")
    ax.plot([0.2, 0.6], [0.25, 0.25], "k-")

    ax.plot([0.6, 0.9], [0.65, 0.65], "k-")
    ax.plot([0.6, 0.9], [0.45, 0.45], "k-")
    ax.plot([0.6, 0.9], [0.25, 0.25], "k-")

    plt.show()


draw_flowchart()
draw_er_diagram()
