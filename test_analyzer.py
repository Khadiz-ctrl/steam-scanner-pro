import json

from app.analysis.analyzer import Analyzer
from app.ui.console import ConsoleUI

analyzer = Analyzer()

with open("data/watchlist.json", "r", encoding="utf-8") as file:
    skins = json.load(file)

analyses = analyzer.analyze_watchlist(skins)

analyses.sort(
    key=lambda analysis: analysis["score"],
    reverse=True
)

print("=" * 50)
print(" TOP OPORTUNIDADES ")
print("=" * 50)
print()

medallas = ["🥇", "🥈", "🥉"]

for i, analysis in enumerate(analyses):

    if i < 3:
        icono = medallas[i]
    else:
        icono = "⭐"

    print(
        f"{icono} "
        f"{analysis['skin']} "
        f"({analysis['score']}/100)"
    )