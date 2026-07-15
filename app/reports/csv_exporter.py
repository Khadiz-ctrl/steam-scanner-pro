import csv
from datetime import datetime
from pathlib import Path


class CSVExporter:

    @staticmethod
    def export(analyses):

        reports_dir = Path("reports")
        reports_dir.mkdir(exist_ok=True)

        filename = datetime.now().strftime(
            "analysis_%Y-%m-%d_%H-%M-%S.csv"
        )

        filepath = reports_dir / filename

        with open(
            filepath,
            mode="w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                "Skin",
                "Current Price",
                "Average Price",
                "Moving Average",
                "Difference %",
                "Volume",
                "Trend",
                "Volatility",
                "Score",
                "Recommendation"
            ])

            for analysis in analyses:

               writer.writerow([
                 analysis.skin,
                 analysis.current_price,
                 analysis.average_price,
                 analysis.moving_average,
                 analysis.difference_percent,
                 analysis.volume,
                 analysis.trend,
                 analysis.volatility,
                 analysis.score,
                 analysis.recommendation,

])

        print(f"\n📄 Report exported: {filepath}")