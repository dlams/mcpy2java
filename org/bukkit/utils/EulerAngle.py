class EulerAngle:
    """EulerAngle is used to represent 3 angles, one for each axis (x, y, z). The angles are in radians"""
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    # def add(self, x: float, y: float, z: float):
    #     """Creates a new EulerAngle which is the result of adding the x, y, z components to this EulerAngle"""
    #     pass

    # def equals(self, Object o):
    #     """"""
    #     pass

    def getX(self):
        """Returns the angle on the x axis in radians"""
        return self.x

    def getY(self):
        """Returns the angle on the y axis in radians"""
        return self.y

    def getZ(self):
        """Returns the angle on the z axis in radians"""
        return self.z

    # def hashCode(self):
    #     """"""
    #     pass

    def setX(self, x: float):
        """Return a EulerAngle which is the result of changingthe x axis to the passed angle"""
        self.x = x

    def setY(self, y: float):
        """Return a EulerAngle which is the result of changingthe y axis to the passed angle"""
        self.y = y

    def setZ(self, z: float):
        """Return a EulerAngle which is the result of changingthe z axis to the passed angle"""
        self.z = z

    # def subtract(self, x: float, y: float, z: float):
    #     """Creates a new EulerAngle which is the result of subtractingthe x, y, z components to this EulerAngle"""
    #     pass