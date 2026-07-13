import json

from app.analysis.analyzer import Analyzer
from app.ui.console import ConsoleUI


def main():

    analyzer = Analyzer()

    with open("data/watchlist.json", "r", encoding="utf-8") as file:
        skins = json.load(file)

    analyses = analyzer.analyze_watchlist(skins)

    analyses.sort(
        key=lambda analysis: analysis["score"],
        reverse=True
    )

    print("=" * 60)
    print(" STEAM SCANNER PRO ")
    print("=" * 60)

    print("\nTOP OPORTUNIDADES\n")

    medals = ["🥇", "🥈", "🥉"]

    for index, analysis in enumerate(analyses):

        medal = medals[index] if index < 3 else "⭐"

        print(
            f"{medal} "
            f"{analysis['skin']} "
            f"- Score: {analysis['score']}/100"
        )

    print("\n" + "=" * 60)
    print(" DETALLE ")
    print("=" * 60)

    for analysis in analyses[:3]:
        ConsoleUI.show_analysis(analysis)


if __name__ == "__main__":
    main()