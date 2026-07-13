class Dashboard:

    WIDTH = 60

    @staticmethod
    def line():
        print("═" * Dashboard.WIDTH)

    @staticmethod
    def title(text):

        Dashboard.line()
        print(text.center(Dashboard.WIDTH))
        Dashboard.line()

    @staticmethod
    def show(analyses):

        buy = sum(
            1
            for analysis in analyses
            if analysis["recommendation"] == "BUY"
        )

        watch = sum(
            1
            for analysis in analyses
            if analysis["recommendation"] == "WATCH"
        )

        skip = sum(
            1
            for analysis in analyses
            if analysis["recommendation"] == "SKIP"
        )

        best = analyses[0]

        Dashboard.title("STEAM SCANNER PRO")

        print()

        print("📊 RESUMEN")
        print("-" * Dashboard.WIDTH)

        print(f"Skins analizadas : {len(analyses)}")
        print(f"BUY              : {buy}")
        print(f"WATCH            : {watch}")
        print(f"SKIP             : {skip}")

        print()

        print("🏆 MEJOR OPORTUNIDAD")
        print("-" * Dashboard.WIDTH)

        print(best["skin"])
        print(f"Score          : ⭐ {best['score']}")
        print(f"Recomendación  : {best['recommendation']}")