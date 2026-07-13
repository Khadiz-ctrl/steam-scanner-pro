import json

from app.providers.steam import SteamProvider
from app.database.database import Database


def cargar_watchlist():
    with open("data/watchlist.json", "r", encoding="utf-8") as archivo:
        return json.load(archivo)


def main():

    watchlist = cargar_watchlist()

    steam = SteamProvider()

    db = Database()
    db.crear_tablas()

    print("=" * 50)
    print(" Steam Scanner ")
    print("=" * 50)

    for skin in watchlist:

        print(f"\nBuscando: {skin}")

        datos = steam.obtener_precio(skin)

        if not datos.get("success"):
            print("❌ Error:", datos.get("error"))
            continue

        db.guardar_precio(skin, datos)

        print("💲 Precio:", datos.get("lowest_price"))
        print("📊 Volumen:", datos.get("volume"))
        print("📈 Mediana:", datos.get("median_price"))

    db.cerrar()


if __name__ == "__main__":
    main()