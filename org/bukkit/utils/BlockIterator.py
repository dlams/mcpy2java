# from multipledispatch import dispatcher
#
#
# class BlockIterator:
#     """This class performs ray tracing and iterates along blocks on a line"""
#     @dispatcher(LivingEntity)
#     def __init__(self, entity):
#         self.entity = entity
#
#     @dispatcher(LivingEntity, int)
#     def __init__(self, entity, maxDistance):
#         self.entity = entity
#         self.maxDistance = maxDistance
#
#     BlockIterator(Location
#     loc)
#     Constructs
#     the
#     BlockIterator.
#     BlockIterator(Location
#     loc, double
#     yOffset)
#     Constructs
#     the
#     BlockIterator.
#     BlockIterator(Location
#     loc, double
#     yOffset, int
#     maxDistance)
#     Constructs
#     the
#     BlockIterator.
#     BlockIterator(World
#     world, Vector
#     start, Vector
#     direction, double
#     yOffset, int
#     maxDistance)
#
#     def hasNext():
#         """Returns true if the iteration has more elements"""
#         pass
#
#     def next():
#         """Returns the next Block in the trace"""
#         pass
#
#     def remove():
#         """"""
#         pass
