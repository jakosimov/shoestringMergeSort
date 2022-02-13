from static.assets.python.interfaces import ScaleInterface


class Scale(ScaleInterface):
    def __init__(self) -> None:
        pass

    def measure(self) -> float:
        raise NotImplementedError

