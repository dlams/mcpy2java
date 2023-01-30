from multipledispatch import dispatch
import copy

from mcpy2java.org.bukkit.utils.Vector import Vector


class BlockVector(Vector):
    """A vector with a hash function that floors the X, Y, Z components, a la BlockVector in WorldEdit.
    BlockVectors can be used in hash sets and hash maps.
    Be aware that BlockVectors are mutable, but it is important that BlockVectors are never changed once put into a hash set or hash map."""

    @dispatch()
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0

    @dispatch(int, int, int)
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @dispatch(float, float, float)
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @dispatch(Vector)
    def __init__(self, vec):
        self.x = vec.x
        self.y = vec.y
        self.z = vec.z

    def clone(self):
        """Get a new block vector."""
        return copy.deepcopy(self)

    # def deserialize(Map<String,Object> args):
    #     """"""
    #     pass
    #
    # def equals(Object obj):
    #     """Checks if another object is equivalent."""
    #     pass
    #
    # def hashCode():
    #     """Returns a hash code for this vector."""
    #     pass
