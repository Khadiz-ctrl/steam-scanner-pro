class ConsoleUI:

    @staticmethod
    def show_analysis(analysis):

        print("=" * 50)
        print(" Steam Scanner Pro ")
        print("=" * 50)

        print(f"\nSkin:\n  {analysis['skin']}")

        print("\nRecomendación:")

        recommendation = analysis["recommendation"]

        if recommendation == "BUY":
            emoji = "🟢"

        elif recommendation == "WATCH":
            emoji = "🟡"

        else:
            emoji = "🔴"

        print(f"  {emoji} {recommendation}")

        print("\nPrecio actual:")
        print(f"  ${analysis['current_price']}")

        print("\nPrecio promedio:")
        print(f"  ${analysis['average_price']}")

        print("\nPrecio objetivo:")
        print(f"  ${analysis.get('target_price', '-')}")

        print("\nDiferencia:")
        emoji = "🟢" if analysis["difference_percent"] < 0 else "🔴"
        print(f"  {emoji} {analysis['difference_percent']} %")

        print("\nVolumen:")
        print(f"  {analysis['volume']}")

        print("\nTendencia:")
        trend = analysis["trend"]

        if trend == "UP":
            emoji = "📈"
        elif trend == "DOWN":
            emoji = "📉"
        else:
            emoji = "➖"

        print(f"  {emoji} {trend}")

        print("\nVolatilidad:")
        print(f"  {analysis['volatility']}")

        print("\nRegistros históricos:")
        print(f"  {len(analysis['history'])}")

        print("\nPrioridad:")
        print(f"  {analysis.get('priority', '-')}")

        print("\nOpportunity Score:")
        print(f"  ⭐ {analysis['score']}/100")

        print("\nRazones:")

        for reason in analysis["reasons"]:
            print(f"  ✔ {reason}")

        print("=" * 50)