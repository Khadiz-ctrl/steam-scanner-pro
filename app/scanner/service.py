import json

from app.analysis.analyzer import Analyzer
from app.analysis.filter import AnalysisFilter
from app.scanner.engine import ScannerEngine
from app.ui.console import ConsoleUI
from app.ui.dashboard import Dashboard


class ScannerService:

    def __init__(self):

        self.engine = ScannerEngine()
        self.analyzer = Analyzer()

    def load_watchlist(self):

        with open(
            "data/watchlist.json",
            "r",
            encoding="utf-8",
        ) as file:

            return json.load(file)

    def analyze(self):

        watchlist = self.load_watchlist()

        self.engine.scan(watchlist)

        analyses = self.analyzer.analyze_watchlist(
            watchlist
        )

        analyses.sort(
            key=lambda analysis: analysis.score,
            reverse=True,
        )

        return analyses

    def show_results(self, analyses):

        Dashboard.show(analyses)

        opportunities = AnalysisFilter.opportunities(
            analyses
        )

        if not opportunities:

            print("\nNo hay oportunidades.\n")
            return

        for analysis in opportunities[:3]:
            ConsoleUI.show_analysis(analysis)

    def run(self):

        analyses = self.analyze()

        self.show_results(analyses)