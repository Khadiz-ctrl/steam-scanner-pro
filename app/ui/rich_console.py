from app.ui.components import Components


class ConsoleUI:

    @staticmethod
    def show_analysis(analysis):

        Components.title("Steam Scanner Pro")

        Components.field("Skin", analysis.skin)

        Components.field(
            "Recommendation",
            analysis.recommendation
        )

        Components.field(
            "Current Price",
            f"${analysis.current_price}"
        )

        Components.field(
            "Average Price",
            f"${analysis.average_price}"
        )

        Components.field(
            "Moving Average",
            f"${analysis.moving_average}"
        )

        Components.field(
            "Target Price",
            analysis.target_price if analysis.target_price is not None else "-"
        )

        Components.field(
            "Difference %",
            f"{analysis.difference_percent} %"
        )

        Components.field(
            "Volume",
            analysis.volume
        )

        Components.field(
            "Trend",
            analysis.trend
        )

        Components.field(
            "Volatility",
            analysis.volatility
        )

        Components.field(
            "History",
            len(analysis.history)
        )

        Components.field(
            "Priority",
            analysis.priority if analysis.priority is not None else "-"
        )

        Components.field(
            "Score",
            f"{analysis.score}/100"
        )

        Components.section("Reasons")

        for reason in analysis.reasons:
            Components.field("✓", reason)

        Components.section("Debug")

        for key, value in analysis.debug.items():
            Components.field(key, value)