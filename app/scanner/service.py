import json

from app.analysis.analyzer import Analyzer
from app.analysis.filter import AnalysisFilter
from app.reports.csv_exporter import CSVExporter
from app.scanner.engine import ScannerEngine
from app.ui.rich_console import ConsoleUI
from app.ui.dashboard import Dashboard


class ScannerService:

    def __init__(self):

        self.engine = ScannerEngine()
        self.analyzer = Analyzer()

    # ---------------------------------------------------------
    # Watchlist
    # ---------------------------------------------------------

    def load_watchlist(self):

        with open(
            "data/watchlist.json",
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    # ---------------------------------------------------------
    # Analysis
    # ---------------------------------------------------------

    def analyze(self):

        watchlist = self.load_watchlist()

        self.engine.scan(watchlist)

        analyses = self.analyzer.analyze_watchlist(
            watchlist
        )

        analyses.sort(
          key=lambda analysis: analysis.score,
          reverse=True
)

        return analyses

    # ---------------------------------------------------------
    # UI
    # ---------------------------------------------------------

    def show_results(self, analyses):

        Dashboard.show(analyses)

        opportunities = AnalysisFilter.opportunities(
            analyses
        )
        if not opportunities:

            print("\nNo hay oportunidades.\n")
            return

        medals = ["🥇", "🥈", "🥉"]

        print("\n" + "=" * 60)
        print(" DETALLE ")
        print("=" * 60)

        for analysis in opportunities[:3]:
            ConsoleUI.show_analysis(analysis)

    # ---------------------------------------------------------
    # Reports
    # ---------------------------------------------------------

    def export_reports(self, analyses):

        CSVExporter.export(analyses)

    # ---------------------------------------------------------
    # Entry Point
    # ---------------------------------------------------------

    def run(self):

        analyses = self.analyze()

        self.show_results(analyses)

        self.export_reports(analyses)