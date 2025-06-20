class Runtime:
    """Placeholder runtime providing minimal services."""

    def __init__(self) -> None:
        self.ffi = None

    def set_ffi(self, ffi) -> None:
        self.ffi = ffi
