from multipledispatch import dispatch
import copy


class BoundingBox:
    """A mutable axis aligned bounding box (AABB).
    This basically represents a rectangular box (specified by minimum and maximum corners) that can for example be used to describe the position and extents of an object (such as an entity, block, or rectangular region) in 3D space. Its edges and faces are parallel to the axes of the cartesian coordinate system.

    The bounding box may be degenerate (one or more sides having the length 0).

    Because bounding boxes are mutable, storing them long term may be dangerous if they get modified later. If you want to keep around a bounding box, it may be wise to call clone(self) in order to get a copy."""

    @dispatch(float, float, float, float, float, float)
    def __init__(self):
        self.x1 = 0
        self.y1 = 0
        self.z1 = 0
        self.x2 = 0
        self.y2 = 0
        self.z2 = 0

    @dispatch(float, float, float, float, float, float)
    def __init__(self, x1, y1, z1, x2, y2, z2):
        self.x1 = x1
        self.y1 = y1
        self.z1 = z1
        self.x2 = x2
        self.y2 = y2
        self.z2 = z2

    def clone(self):
        """Creates a copy of this bounding box."""
        return copy.deepcopy(self)
#
#     @dispatch(float, float, float)
#     def contains(self, x, y, z):
#         """Checks if this bounding box contains the specified position."""
#         pass
#
#     @dispatch(BoundingBox)
#     def contains(self, other):
#         """Checks if this bounding box fully contains the given bounding box."""
#         pass
#
#     @dispatch(Vector)
#     def contains(self, position):
#         """Checks if this bounding box contains the specified position."""
#         pass
#
#     @dispatch(Vector, Vector)
#     def contains(min, max):
#         """Checks if this bounding box fully contains the bounding box that isdefined by the given corners."""
#         pass
#
#
#     def copy(BoundingBox other):
#         """Copies another bounding box."""
#         pass
#
#     def deserialize(Map<String,Object> args):
#         """"""
#         pass
#
#     def equals(Object obj):
#         """"""
#         pass
#
#     @dispatch(float)
#     def expand(self, expansion):
#         """Expands this bounding box uniformly by the given value in all directions."""
#         pass
#
#     @dispatch(float, float, float)
#     def expand(self, x, y, z):
#         """Expands this bounding box uniformly by the given values in both positiveand negative directions."""
#         pass
#
#     @dispatch(float, float, float, float)
#     def expand(self, dirX, dirY, dirZ, expansion):
#         """Expands this bounding box in the specified direction."""
#         pass
#
#     @dispatch(float, float, float, float, float, float)
#     def expand(self, negativeX, negativeY, negativeZ, positiveX, positiveY, positiveZ):
#         """Expands this bounding box by the given values in the correspondingdirections."""
#         pass
#
#     @dispatch(BlockFace, float)
#     def expand(self, blockFace, expansion):
#         """Expands this bounding box in the direction specified by the given blockface."""
#         pass
#
#     @dispatch(Vector)
#     def expand(self, expansion):
#         """Expands this bounding box uniformly by the given values in both positiveand negative directions."""
#         pass
#
#     @dispatch(Vector, float)
#     def expand(self, direction, expansion):
#         """Expands this bounding box in the specified direction."""
#         pass
#
#     @dispatch(float, float, float)
#     def expandDirectional(self, dirX, dirY, dirZ):
#         """Expands this bounding box in the specified direction."""
#         pass
#
#     @dispatch(Vector)
#     def expandDirectional(self, direction):
#         """Expands this bounding box in the specified direction."""
#         pass
#
#     def getCenter(self):
#         """Gets the center of the bounding box."""
#         pass
#
#     def getCenterX(self):
#         """Gets the x coordinate of the center of the bounding box."""
#         pass
#
#     def getCenterY(self):
#         """Gets the y coordinate of the center of the bounding box."""
#         pass
#
#     def getCenterZ(self):
#         """Gets the z coordinate of the center of the bounding box."""
#         pass
#
#     def getHeight(self):
#         """Gets the height of the bounding box."""
#         pass
#
#     def getMax(self):
#         """Gets the maximum corner as vector."""
#         pass
#
#     def getMaxX(self):
#         """Gets the maximum x value."""
#         pass
#
#     def getMaxY(self):
#         """Gets the maximum y value."""
#         pass
#
#     def getMaxZ(self):
#         """Gets the maximum z value."""
#         pass
#
#     def getMin(self):
#         """Gets the minimum corner as vector."""
#         pass
#
#     def getMinX(self):
#         """Gets the minimum x value."""
#         pass
#
#     def getMinY(self):
#         """Gets the minimum y value."""
#         pass
#
#     def getMinZ(self):
#         """Gets the minimum z value."""
#         pass
#
#     def getVolume(self):
#         """Gets the volume of the bounding box."""
#         pass
#
#     def getWidthX(self):
#         """Gets the width of the bounding box in the x direction."""
#         pass
#
#     def getWidthZ(self):
#         """Gets the width of the bounding box in the z direction."""
#         pass
#
#     def hashCode(self):
#         """"""
#         pass
#
#     def intersection(BoundingBox other):
#         """Resizes this bounding box to represent the intersection of this and thegiven bounding box."""
#         pass
#
#     def of(Block block):
#         """Creates a new 1x1x1 sized bounding box containing the given block."""
#         pass
#
#     def of(Block corner1,Block corner2):
#         """Creates a new bounding box using the coordinates of the given blocks ascorners."""
#         pass
#
#     def of(Location center,double x,double y,double z):
#         """Creates a new bounding box using the given center and extents."""
#         pass
#
#     def of(Location corner1,Location corner2):
#         """Creates a new bounding box using the coordinates of the given locationsas corners."""
#         pass
#
#     def of(Vector center,double x,double y,double z):
#         """Creates a new bounding box using the given center and extents."""
#         pass
#
#     def of(Vector corner1,Vector corner2):
#         """Creates a new bounding box using the coordinates of the given vectors ascorners."""
#         pass
#
#     def overlaps(BoundingBox other):
#         """Checks if this bounding box overlaps with the given bounding box."""
#         pass
#
#     def overlaps(Vector min,Vector max):
#         """Checks if this bounding box overlaps with the bounding box that isdefined by the given corners."""
#         pass
#
#     def rayTrace(Vector start,Vector direction,double maxDistance):
#         """Calculates the intersection of this bounding box with the specified linesegment."""
#         pass
#
#     def resize(double x1,double y1,double z1,double x2,double y2,double z2):
#         """Resizes this bounding box."""
#         pass
#
#     def serialize(self):
#         """Creates a Map representation of this class."""
#         pass
#
#     def shift(double shiftX,double shiftY,double shiftZ):
#         """Shifts this bounding box by the given amounts."""
#         pass
#
#     def shift(Location shift):
#         """Shifts this bounding box by the given amounts."""
#         pass
#
#     def shift(Vector shift):
#         """Shifts this bounding box by the given amounts."""
#         pass
#
#     def toString(self):
#         """"""
#         pass
#
#     def union(double posX,double posY,double posZ):
#         """Expands this bounding box to contain (or border) the specified position."""
#         pass
#
#     def union(Location position):
#         """Expands this bounding box to contain (or border) the specified position."""
#         pass
#
#     def union(BoundingBox other):
#         """Expands this bounding box to contain both this and the given boundingbox."""
#         pass
#
#     def union(Vector position):
#         """Expands this bounding box to contain (or border) the specified position."""
#         pass