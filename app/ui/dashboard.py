class Dashboard:

    @staticmethod
    def show(analyses):

        buy = 0
        watch = 0
        skip = 0

        for analysis in analyses:

            recommendation = analysis["recommendation"]

            if recommendation == "BUY":
                buy += 1

            elif recommendation == "WATCH":
                watch += 1

            else:
                skip += 1

        best = analyses[0]

        print("=" * 60)
        print(" STEAM SCANNER PRO ")
        print("=" * 60)

        print("\nRESUMEN DEL MERCADO\n")

        print(f"Skins analizadas : {len(analyses)}")
        print(f"BUY              : {buy}")
        print(f"WATCH            : {watch}")
        print(f"SKIP             : {skip}")

        print("\nMejor oportunidad:")

        print(f"  {best['skin']}")
        print(f"  Score: {best['score']}")