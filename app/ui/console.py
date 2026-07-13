class ConsoleUI:

    @staticmethod
    def show_analysis(analysis):

        ConsoleUI.show_header(analysis)
        ConsoleUI.show_recommendation(analysis)
        ConsoleUI.show_market(analysis)
        ConsoleUI.show_activity(analysis)
        ConsoleUI.show_score(analysis)
        ConsoleUI.show_debug(analysis)

        print("=" * 50)

    @staticmethod
    def show_header(analysis):

        print("=" * 50)
        print(" Steam Scanner Pro ")
        print("=" * 50)

        print(f"\nSkin:\n  {analysis['skin']}")

    @staticmethod
    def show_recommendation(analysis):

        recommendation = analysis["recommendation"]

        if recommendation == "BUY":
            emoji = "🟢"
        elif recommendation == "WATCH":
            emoji = "🟡"
        else:
            emoji = "🔴"

        print("\nRecomendación:")
        print(f"  {emoji} {recommendation}")

    @staticmethod
    def show_market(analysis):

        print("\nPrecio actual:")
        print(f"  ${analysis['current_price']}")

        print("\nPrecio promedio:")
        print(f"  ${analysis['average_price']}")

        print("\nMedia móvil (5):")
        print(f"  ${analysis['moving_average']}")

        print("\nPrecio objetivo:")
        print(f"  ${analysis.get('target_price', '-')}")

        emoji = "🟢" if analysis["difference_percent"] < 0 else "🔴"

        print("\nDiferencia:")
        print(f"  {emoji} {analysis['difference_percent']} %")

    @staticmethod
    def show_activity(analysis):

        print("\nVolumen:")
        print(f"  {analysis['volume']}")

        trend = analysis["trend"]

        if trend == "UP":
            emoji = "📈"
        elif trend == "DOWN":
            emoji = "📉"
        else:
            emoji = "➖"

        print("\nTendencia:")
        print(f"  {emoji} {trend}")

        print("\nVolatilidad:")
        print(f"  {analysis['volatility']}")

        print("\nRegistros históricos:")
        print(f"  {len(analysis['history'])}")

        print("\nPrioridad:")
        print(f"  {analysis.get('priority', '-')}")

    @staticmethod
    def show_score(analysis):

        print("\nOpportunity Score:")
        print(f"  ⭐ {analysis['score']}/100")

        print("\nRazones:")

        for reason in analysis["reasons"]:
            print(f"  ✔ {reason}")

    @staticmethod
    def show_debug(analysis):

        print("\nScore Debug:")

        for key, value in analysis["debug"].items():
            print(f"  {key:<15} +{value}")