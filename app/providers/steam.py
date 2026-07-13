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

        return datos