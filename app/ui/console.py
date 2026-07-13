class ConsoleUI:

    @staticmethod
    def show_analysis(analysis):

        print("=" * 50)
        print(" Steam Scanner Pro ")
        print("=" * 50)

        print(f"\nSkin:")
        print(f"  {analysis['skin']}")

        print("\nPrecio actual:")
        print(f"  ${analysis['current_price']}")

        print("\nPrecio promedio:")
        print(f"  ${analysis['average_price']}")

        print("\nDiferencia:")

        emoji = "🟢" if analysis["difference_percent"] < 0 else "🔴"

        print(f"  {emoji} {analysis['difference_percent']} %")

        print("\nVolumen:")
        print(f"  {analysis['volume']}")

        print("\nRegistros históricos:")
        print(f"  {len(analysis['history'])}")

        print("\nOpportunity Score:")
        print(f"  ⭐ {analysis['score']}/100")

        print("=" * 50)