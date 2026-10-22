class CajaFuerte:
    def __init__(self, clave_secreta: str):
        if len(clave_secreta) != 4 or not clave_secreta.isdigit():
            raise ValueError("La clave debe ser un número de 4 dígitos.")
        self._clave_secreta = clave_secreta
        self._abierta = False
        self._intentos_fallidos = 0
        self._bloqueada = False

    @property
    def estado(self) -> str:
        if self._bloqueada:
            return "BLOQUEADA"
        return "ABIERTA" if self._abierta else "CERRADA"

    @property
    def intentos_fallidos(self) -> int:
        return self._intentos_fallidos

    @property
    def bloqueada(self) -> bool:
        return self._bloqueada

    def desbloquear(self, clave: str) -> str:
        if self._bloqueada:
            return "Sistema bloqueado. No se permiten más intentos."

        if clave == self._clave_secreta:
            self._abierta = True
            self._intentos_fallidos = 0  # resetea al acertar
            return "Caja abierta correctamente."
        else:
            self._intentos_fallidos += 1
            if self._intentos_fallidos >= 3:
                self.bloquear()
                return "Tres intentos fallidos. Sistema bloqueado."
            return f"Clave incorrecta. Intento {self._intentos_fallidos}/3."

    def bloquear(self):
        self._bloqueada = True
        self._abierta = False

    def __repr__(self):
        return (f"CajaFuerte(estado={self.estado}, "
                f"intentos_fallidos={self._intentos_fallidos})")


# ── Demo / prueba ──────────────────────────────────────────────
if __name__ == "__main__":
    caja = CajaFuerte("1234")
    print(caja)                        # CERRADA

    print(caja.desbloquear("0000"))    # Intento 1/3
    print(caja.desbloquear("5555"))    # Intento 2/3
    print(caja.desbloquear("9999"))    # Bloqueada
    print(caja)                        # BLOQUEADA

    print(caja.desbloquear("1234"))    # No se puede, está bloqueada