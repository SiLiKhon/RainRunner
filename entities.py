from geometry import Vector

class Entity:
    def __init__(self, location : Vector):
        self.location = location

    def line_collide(self, loc_first : Vector, loc_last : Vector) -> bool:
        raise NotImplementedError

class Ball(Entity):
    def __init__(self, location : Vector, R : float):
        super().__init__(location)
        self.R = R

    def line_collide(self, loc_first : Vector, loc_last : Vector) -> bool:
        vec_to_first = loc_first - self.location

        if loc_first == loc_last:
            return vec_to_first.norm() <= self.R

        if (loc_first - self.location).norm() <= self.R:
            return True
        if (loc_last - self.location).norm() <= self.R:
            return True

        segment_dir = loc_last - loc_first
        segment_norm = segment_dir.norm()
        segment_dir /= segment_norm

        delta_to_closest = -segment_dir * (vec_to_first.dot(segment_dir))
        loc_closest = loc_first + delta_to_closest

        if (loc_closest - self.location).norm() <= self.R:
            if delta_to_closest.dot(segment_dir) >= 0:
                if delta_to_closest.norm() <= segment_norm:
                    return True

        return False
