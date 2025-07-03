import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(12, 8))
ax.set_xlim(0, 12)
ax.set_ylim(0, 10)
ax.axis('off')

# Function to draw box with text
def draw_box(x, y, w, h, label, color="#e0f7fa"):
    rect = patches.FancyBboxPatch((x, y), w, h,
                                  boxstyle="round,pad=0.03",
                                  linewidth=1.5, edgecolor='black',
                                  facecolor=color)
    ax.add_patch(rect)
    ax.text(x + w / 2, y + h / 2, label, ha="center", va="center", fontsize=9)

# Frontend
draw_box(1, 7.5, 3, 1, "User Interface\n(Web / Mobile UI)", "#ffe0b2")

# Input
draw_box(1, 6, 3, 1, "User Input\n(Chat / Voice)", "#fff9c4")

# Agent Builder Layer
draw_box(4.5, 7.5, 3, 1, "Vertex AI Agent Builder", "#dcedc8")

# Financial Data Source
draw_box(8, 8, 3, 1, "Fi MCP\n(Financial Data)", "#f8bbd0")

# AI Engine
draw_box(4.5, 6, 3, 1, "Gemini\n(Intelligence Layer)", "#c5cae9")

# Database
draw_box(4.5, 4.5, 3, 1, "Firebase Firestore\n(Data Storage)", "#b2ebf2")

# Google Wallet
draw_box(8, 6, 3, 1, "Google Wallet API\n(Pass Creation)", "#d1c4e9")

# Output
draw_box(1, 3, 3, 1, "Insight Delivery\n(Dashboard + Wallet)", "#c8e6c9")

# Arrows
def arrow(x1, y1, x2, y2):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="->", lw=2))

arrow(2.5, 7.5, 6, 7.5)  # UI to Agent Builder
arrow(2.5, 6, 6, 6.5)    # Input to Gemini
arrow(6, 7.5, 6, 6.5)    # Agent Builder to Gemini
arrow(9.5, 8, 6.8, 6.9)  # Fi MCP to Gemini
arrow(6, 6, 6, 5)        # Gemini to Firestore
arrow(6, 6, 9.5, 6.5)    # Gemini to Wallet
arrow(6, 4.5, 2.5, 3.5)  # Firestore to Output
arrow(9.5, 6, 2.5, 3.5)  # Wallet to Output

# Title
plt.title("NeoVerse – Architecture Diagram of the Proposed Solution", fontsize=14, weight='bold')

plt.tight_layout()
plt.show()

