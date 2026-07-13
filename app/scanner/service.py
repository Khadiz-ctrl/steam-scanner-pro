import json

from app.analysis.analyzer import Analyzer
from app.ui.console import ConsoleUI


class ScannerService:

    def __init__(self):
        self.analyzer = Analyzer()

    def load_watchlist(self):

        with open("data/watchlist.json", "r", encoding="utf-8") as file:
            return json.load(file)

    def analyze(self):

        watchlist = self.load_watchlist()

        analyses = self.analyzer.analyze_watchlist(watchlist)

        analyses.sort(
            key=lambda analysis: analysis["score"],
            reverse=True
        )

        return analyses

    def show_results(self, analyses):

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
                f"- {analysis['recommendation']} "
                f"- Score: {analysis['score']}/100"
            )

        print("\n" + "=" * 60)
        print(" DETALLE ")
        print("=" * 60)

        for analysis in analyses[:3]:
            ConsoleUI.show_analysis(analysis)

    def run(self):

        analyses = self.analyze()

        self.show_results(analyses)