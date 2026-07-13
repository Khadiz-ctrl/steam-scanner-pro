import requests


class SteamProvider:

    BASE_URL = "https://steamcommunity.com/market/priceoverview/"

    def obtener_precio(self, skin):

        parametros = {
            "appid": 730,
            "currency": 1,
            "market_hash_name": skin
        }

        respuesta = requests.get(
            self.BASE_URL,
            params=parametros,
            timeout=10,
            headers={
                "User-Agent": "SteamScanner/1.0"
            }
        )

        if respuesta.status_code != 200:
            return {
                "success": False,
                "error": f"HTTP {respuesta.status_code}"
            }

        datos = respuesta.json()

        if not datos.get("success"):
            return datos

        # Limpiar precio
        precio = datos.get("lowest_price", "")
        precio = precio.replace("$", "").replace(",", "")

        try:
            precio = float(precio)
        except ValueError:
            precio = None

        # Limpiar volumen
        volumen = datos.get("volume", "0")
        volumen = volumen.replace(",", "")

        try:
            volumen = int(volumen)
        except ValueError:
            volumen = 0

        return {
            "success": True,
            "price": precio,
            "volume": volumen,
            "median_price": datos.get("median_price")
        }