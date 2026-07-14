from abc import ABC, abstractmethod


class PriceProvider(ABC):
    """
    Contrato para cualquier proveedor de precios.
    """

    @abstractmethod
    def obtener_precio(self, skin):
        """
        Debe devolver:

        {
            "success": bool,
            "price": float,
            "volume": int,
            "median_price": float
        }
        """
        pass