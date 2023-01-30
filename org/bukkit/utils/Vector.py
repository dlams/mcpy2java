# from multipledispatch import dispatcher
import copy


class Vector:
    """Represents a mutable vector.
    Because the components of Vectors are mutable, storing Vectors long term may be dangerous if passing code modifies the Vector later.
    If you want to keep around a Vector, it may be wise to call clone() in order to get a copy."""

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def add(self, vec):
        """Adds a vector to this one"""
        self.x += vec.x
        self.y += vec.y
        self.z += vec.z

    # def angle(self, other):  # 나중에 최적화 식 찾아서 넣기
    #     """Gets the angle between this vector and another in radians."""
    #     pass

    # def checkFinite(self) -> None:
    #     """Check if each component of this Vector is finite."""
    #     pass

    def clone(self):
        """Get a new vector."""
        return copy.deepcopy(self)

    def copy(self, vec):  # 무슨 녀석인지 확인 필요
        """Copies another vector"""
        return copy.deepcopy(vec)

    def crossProduct(self, o):
        """Calculates the cross product of this vector with another."""
        pass

    # def deserialize(Map<String,Object> args):
    #     """"""
    #     pass
    #
    # def distance(Vector o):
    #     """Get the distance between this vector and another."""
    #     pass
    #
    # def distanceSquared(Vector o):
    #     """Get the squared distance between this vector and another."""
    #     pass
    #
    # def divide(Vector vec):
    #     """Divides the vector by another."""
    #     pass
    #
    # def dot(Vector other):
    #     """Calculates the dot product of this vector with another."""
    #     pass
    #
    # def equals(Object obj):
    #     """Checks to see if two objects are equal."""
    #     pass
    #
    # def getBlockX(self):
    #     """Gets the floored value of the X component, indicating the block thatthis vector is contained with."""
    #     pass
    #
    # def getBlockY(self):
    #     """Gets the floored value of the Y component, indicating the block thatthis vector is contained with."""
    #     pass
    #
    # def getBlockZ(self):
    #     """Gets the floored value of the Z component, indicating the block thatthis vector is contained with."""
    #     pass
    #
    # def getCrossProduct(Vector o):
    #     """Calculates the cross product of this vector with another without mutatingthe original."""
    #     pass
    #
    # def getEpsilon(self):
    #     """Get the threshold used for equals(self)."""
    #     pass
    #
    # def getMaximum(Vector v1,Vector v2):
    #     """Gets the maximum components of two vectors."""
    #     pass
    #
    # def getMidpoint(Vector other):
    #     """Gets a new midpoint vector between this vector and another."""
    #     pass
    #
    # def getMinimum(Vector v1,Vector v2):
    #     """Gets the minimum components of two vectors."""
    #     pass
    #
    # def getRandom(self):
    #     """Gets a random vector with components having a random value between 0and 1."""
    #     pass

    def getX(self):
        """Gets the X component."""
        return self.x

    def getY(self):
        """Gets the Y component."""
        return self.y

    def getZ(self):
        """Gets the Z component."""
        return self.z

    # def hashCode(self):
    #     """Returns a hash code for this vector"""
    #     pass
    #
    # def isInAABB(Vector min,Vector max):
    #     """Returns whether this vector is in an axis-aligned bounding box."""
    #     pass
    #
    # def isInSphere(Vector origin,double radius):
    #     """Returns whether this vector is within a sphere."""
    #     pass
    #
    # def isNormalized(self) -> bool:
    #     """Returns if a vector is normalized"""
    #     pass
    #
    # def length(self):
    #     """Gets the magnitude of the vector, defined as sqrt(x^2+y^2+z^2)."""
    #     pass
    #
    # def lengthSquared(self):
    #     """Gets the magnitude of the vector squared."""
    #     pass
    #
    # def midpoint(Vector other):
    #     """Sets this vector to the midpoint between this vector and another."""
    #     pass
    #
    # def multiply(double m):
    #     """Performs scalar multiplication, multiplying all components with a scalar."""
    #     pass
    #
    # def multiply(float m):
    #     """Performs scalar multiplication, multiplying all components with a scalar."""
    #     pass
    #
    # def multiply(int m):
    #     """Performs scalar multiplication, multiplying all components with a scalar."""
    #     pass
    #
    # def multiply(Vector vec):
    #     """Multiplies the vector by another."""
    #     pass
    #
    # def normalize(self):
    #     """Converts this vector to a unit vector (a vector with length of 1)."""
    #     pass
    #
    # def rotateAroundAxis(Vector axis,double angle):
    #     """Rotates the vector around a given arbitrary axis in 3 dimensional space."""
    #     pass
    #
    # def rotateAroundNonUnitAxis(Vector axis,double angle):
    #     """Rotates the vector around a given arbitrary axis in 3 dimensional space."""
    #     pass
    #
    # def rotateAroundX(double angle):
    #     """Rotates the vector around the x axis."""
    #     pass
    #
    # def rotateAroundY(double angle):
    #     """Rotates the vector around the y axis."""
    #     pass
    #
    # def rotateAroundZ(double angle):
    #     """Rotates the vector around the z axis"""
    #     pass
    #
    # def serialize(self):
    #     """Creates a Map representation of this class."""
    #     pass
    #
    def setX(self, x):
        """Set the X component."""
        self.x = x

    def setY(self, y):
        """Set the Y component."""
        self.y = y

    def setZ(self, z):
        """Set the Z component."""
        self.z = z

    def subtract(self, vec):
        """Subtracts a vector from this one."""
        self.x -= vec.x
        self.y -= vec.y
        self.z -= vec.z

    # def toBlockVector(self):
    #     """Get the block vector of this vector."""
    #     pass
    #
    # def toLocation(world: World, yaw: float, pitch: float):
    #     """Gets a Location version of this vector."""
    #     pass
    #     # return Location(x, y, z)
    #
    # def toString(self):
    #     """Returns this vector's components as x,y,z."""
    #     pass
    #
    def zero(self):
        """Zero this vector's components."""
        self.x = 0.;
        self.y = 0.;
        self.z = 0.
