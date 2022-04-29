from __future__ import annotations
import numpy as np

class Vector:
    def __init__(self, data : np.ndarray):
        self.data = data

    def __neg__(self) -> Vector:
        return Vector(-self.data)

    def __add__(self, other : Vector) -> Vector:
        return Vector(self.data + other.data)

    def __sub__(self, other : Vector) -> Vector:
        return Vector(self.data - other.data)

    def __mul__(self, num : float) -> Vector:
        return Vector(self.data * num)

    def __rmul__(self, num : float) -> Vector:
        return Vector(self.data * num)

    def __truediv__(self, num : float) -> Vector:
        return Vector(self.data / num)

    def norm(self) -> float:
        return np.linalg.norm(self.data)

    def dot(self, other : Vector) -> float:
        return np.dot(self.data, other.data)

    def __eq__(self, other : object) -> bool:
        if not isinstance(other, Vector):
            return NotImplemented

        return np.allclose(self.data, other.data)
