from matplotlib import pyplot as plt
import numpy as np
import my_colors
from scipy.special import comb


def prob(h, t, r):
    return comb(h+t,h)*r**h*(1-r)**t


def g(r):
    return 1


def pdf(h, t, r):
    p_array = np.linspace(0,1,100)
    dp = np.mean(np.diff(p_array))
    denom = 0
    for p in p_array:
        denom += prob(h, t, p)*g(p)*dp
    numer = prob(h, t, r)*g(r)

    return numer/denom

n = 725
h = int(0.636*725)
t = n-h

r_array = np.linspace(0,1,500)

pdf_ = []
for r in r_array:
    pdf_.append(pdf(h,t,r))

# BLOCK: Import modules for plot
plt.rcParams["font.family"] ="Times New Roman"
plt.rcParams["axes.unicode_minus"] = False

# Create a figure object
fig, ax = plt.subplots(1, 1, figsize=(8, 6), tight_layout=True)

# Plot the data
ax.plot(r_array, pdf_,
        linestyle="-", linewidth=2, color=my_colors.color[0],
        marker="none", markersize=8, markerfacecolor="white", markevery=10,
        label="n=725, win=461, lose=264")

# Set legend and axis
# plt.legend() # Show the legends
plt.xticks(fontname="Times New Roman", fontsize=12)  # Rotate the xticks by 15 degree
plt.yticks(fontname="Times New Roman", fontsize=12) # Set the yticks
ax.grid(True) # Show grids

# Add texts
plt.title("Posterior probability density function",  fontdict={"fontsize":16, "fontweight": "normal"})
plt.xlabel("r", fontsize=16, color="black", fontname="Times New Roman")
plt.ylabel("pdf", fontsize=16, color="black", fontname="Times New Roman")

# Save figure and show
plt.tight_layout() # Tight layout
plt.savefig(f"pdf.png", dpi=300)
plt.show()
