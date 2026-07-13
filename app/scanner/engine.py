from app.database.database import Database
from app.providers.mock import MockProvider
from app.utils.logger import Logger


class ScannerEngine:

    def __init__(self):

        self.provider = MockProvider()
        self.database = Database()

    def scan(self, watchlist):

        Logger.info("Iniciando escaneo")

        print("\nEscaneando mercado...\n")

        for item in watchlist:

            skin = item["skin"]

            print(f"Consultando {skin}")

            data = self.provider.obtener_precio(skin)

            if data["success"]:

                self.database.guardar_precio(
                    skin,
                    data
                )

                Logger.info(f"{skin} escaneada correctamente")

                print("   ✔ OK")

            else:

                Logger.info(f"Error al consultar {skin}")

                print("   ❌ Error")

        Logger.info("Escaneo finalizado")