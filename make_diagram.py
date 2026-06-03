"""Generate the Adventure Works business-process data-flow diagram."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from matplotlib.lines import Line2D

fig, ax = plt.subplots(figsize=(12, 7.2))
ax.set_xlim(0, 12)
ax.set_ylim(0, 7.2)
ax.axis("off")

# Colour palette
C_PROC = "#2E5E8C"     # process boxes (operational)
C_PROC_TXT = "white"
C_STORE = "#C8A04B"    # data store
C_BI = "#4A7C3F"       # BI / dashboard
C_ARROW = "#555555"

def box(x, y, w, h, title, sub, fc, tc="white", fs=10, subfs=8):
    p = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.12",
                       linewidth=1.2, edgecolor="#222222", facecolor=fc, zorder=2)
    ax.add_patch(p)
    cx, cy = x + w / 2, y + h / 2
    ax.text(cx, cy + (0.12 if sub else 0), title, ha="center", va="center",
            fontsize=fs, fontweight="bold", color=tc, zorder=3)
    if sub:
        ax.text(cx, cy - 0.2, sub, ha="center", va="center",
                fontsize=subfs, color=tc, zorder=3, style="italic")
    return (cx, cy, x, y, w, h)

def arrow(p1, p2, color=C_ARROW, style="-|>", lw=1.6, rad=0.0, ls="-"):
    a = FancyArrowPatch(p1, p2, arrowstyle=style, mutation_scale=14,
                        linewidth=lw, color=color, zorder=1,
                        connectionstyle=f"arc3,rad={rad}", linestyle=ls)
    ax.add_patch(a)

# Title
ax.text(6, 6.95, "Adventure Works Cycles - Business Process & Data Flow",
        ha="center", va="center", fontsize=14, fontweight="bold", color="#1a1a1a")
ax.text(6, 6.6, "Operational source processes feed the data warehouse, which serves the Power BI dashboard",
        ha="center", va="center", fontsize=9, color="#555555", style="italic")

# Row 1 - operational processes (top)
b1 = box(0.4, 5.0, 2.5, 1.0, "Customer\nAcquisition", "Customer Lookup", C_PROC)
b2 = box(3.3, 5.0, 2.5, 1.0, "Order\nManagement", "Sales Data", C_PROC)
b3 = box(6.2, 5.0, 2.5, 1.0, "Sales /\nDistribution", "Sales Data", C_PROC)
b4 = box(9.1, 5.0, 2.5, 1.0, "Inventory &\nFulfilment", "Product Lookup", C_PROC)

# Row 2 - operational processes (lower)
b5 = box(3.3, 3.4, 2.5, 1.0, "Returns\nManagement", "Returns Data", C_PROC)
b6 = box(6.2, 3.4, 2.5, 1.0, "Customer\nExperience", "Customer Lookup", C_PROC)

# Flow between operational processes
arrow((b1[0]+1.25, b1[1]), (b2[0]-1.25, b2[1]))
arrow((b2[0]+1.25, b2[1]), (b3[0]-1.25, b3[1]))
arrow((b3[0]+1.25, b3[1]), (b4[0]-1.25, b4[1]))
arrow((b3[0], 5.0), (b5[0]+0.6, 4.4), rad=-0.2)   # sales -> returns
arrow((b3[0], 5.0), (b6[0], 4.4), rad=0.0)        # sales -> CX

# Central data warehouse
dw = box(3.0, 1.7, 6.0, 1.0, "ETL / Power Query  ->  Data Warehouse (Star Schema)",
         "Fact: Sales, Returns   |   Dim: Customer, Product, Territory, Calendar",
         C_STORE, tc="#1a1a1a", fs=10.5, subfs=8)

# Arrows from processes into the warehouse
for src in [b1, b2, b3, b4]:
    arrow((src[0], src[1]-0.5), (src[0], 2.7), color="#888888", lw=1.3, rad=0.0, ls=(0,(4,2)))
for src in [b5, b6]:
    arrow((src[0], 3.4), (src[0], 2.7), color="#888888", lw=1.3, ls=(0,(4,2)))

# BI layer
bi = box(3.0, 0.25, 6.0, 1.0, "Power BI Dashboard",
         "Executive | Regional | Product | Customer Insights",
         C_BI, fs=11, subfs=8)
arrow((dw[0], 1.7), (bi[0], 1.25), color=C_BI, lw=2.0)

# Legend
legend_items = [
    ("Operational business process", C_PROC),
    ("Data warehouse / staging", C_STORE),
    ("BI presentation layer", C_BI),
]
handles = [Line2D([0],[0], marker="s", markersize=11, linestyle="",
                  markerfacecolor=c, markeredgecolor="#222") for _, c in legend_items]
ax.legend(handles, [t for t, _ in legend_items], loc="lower left",
          bbox_to_anchor=(0.0, -0.02), fontsize=8, frameon=False, ncol=3)

plt.tight_layout()
fig.savefig("diagram_process_flow.png", dpi=200, bbox_inches="tight", facecolor="white")
print("saved diagram_process_flow.png")
