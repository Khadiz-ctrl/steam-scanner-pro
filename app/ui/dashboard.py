from rich.panel import Panel
from rich.table import Table

from app.ui.theme import console


class Dashboard:

    @staticmethod
    def show(analyses):

        buy = sum(
            1
            for analysis in analyses
            if analysis.recommendation == "BUY"
        )

        watch = sum(
            1
            for analysis in analyses
            if analysis.recommendation == "WATCH"
        )

        skip = sum(
            1
            for analysis in analyses
            if analysis.recommendation == "SKIP"
        )

        best = analyses[0]

        console.print()

        console.print(
            Panel.fit(
                (
                    f"[bold cyan]Steam Scanner Pro[/bold cyan]\n\n"
                    f"🟢 BUY      : {buy}\n"
                    f"🟡 WATCH    : {watch}\n"
                    f"🔴 SKIP     : {skip}\n\n"
                    f"🏆 Mejor oportunidad\n"
                    f"{best.skin}\n"
                    f"⭐ Score: {best.score}"
                ),
                title="Dashboard",
            )
        )

        table = Table(title="Top Opportunities")

        table.add_column("#", justify="center", width=4)
        table.add_column("Skin")
        table.add_column("Score", justify="right")
        table.add_column("Action", justify="center")

        medals = ["🥇", "🥈", "🥉"]

        for index, analysis in enumerate(analyses[:5]):

            medal = medals[index] if index < 3 else "⭐"

            if analysis.recommendation == "BUY":
                action = "🟢 BUY"

            elif analysis.recommendation == "WATCH":
                action = "🟡 WATCH"

            else:
                action = "🔴 SKIP"

            table.add_row(
                medal,
                analysis.skin,
                f"⭐ {analysis.score}",
                action,
            )

        console.print(table)