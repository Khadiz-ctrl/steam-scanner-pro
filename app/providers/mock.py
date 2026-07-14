import random

from app.providers.base import PriceProvider


class MockProvider(PriceProvider):

    def obtener_precio(self, skin):

        precios = {
            "AK-47 | Redline (Field-Tested)": (41.30, 73),
            "AWP | Asiimov (Battle-Scarred)": (103.24, 19),
            "USP-S | Printstream (Field-Tested)": (55.00, 80),
        }

        precio, volumen = precios.get(
            skin,
            (
                round(random.uniform(10, 200), 2),
                random.randint(10, 300)
            )
        )

        variacion = random.uniform(-2, 2)

        precio = round(precio * (1 + variacion / 100), 2)

        return {
            "success": True,
            "price": precio,
            "volume": volumen,
            "median_price": precio
        }