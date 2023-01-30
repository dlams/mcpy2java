class World: # interface
    """Represents a world, which may contain entities, chunks and blocks"""
    def __init__(self):
        pass
    
    # def addPluginChunkTicket(int x,int z,Plugin plugin):
    #     """Adds a plugin ticket for the specified chunk, loading the chunk if it isnot already loaded."""
    #     pass
    #
    # def canGenerateStructures():
    #     """Gets whether or not structures are being generated."""
    #     pass
    #
    # def createExplosion(double x,double y,double z,float power):
    #     """Creates explosion at given coordinates with given power"""
    #     pass
    #
    # def createExplosion(double x,double y,double z,float power,boolean setFire):
    #     """Creates explosion at given coordinates with given power and optionallysetting blocks on fire."""
    #     pass
    #
    # def createExplosion(double x,double y,double z,float power,boolean setFire,boolean breakBlocks):
    #     """Creates explosion at given coordinates with given power and optionallysetting blocks on fire or breaking blocks."""
    #     pass
    #
    # def createExplosion(double x,double y,double z,float power,boolean setFire,boolean breakBlocks,Entity source):
    #     """Creates explosion at given coordinates with given power and optionallysetting blocks on fire or breaking blocks."""
    #     pass
    #
    # def createExplosion(Location loc,float power):
    #     """Creates explosion at given coordinates with given power"""
    #     pass
    #
    # def createExplosion(Location loc,float power,boolean setFire):
    #     """Creates explosion at given coordinates with given power and optionallysetting blocks on fire."""
    #     pass
    #
    # def createExplosion(Location loc,float power,boolean setFire,boolean breakBlocks):
    #     """Creates explosion at given coordinates with given power and optionallysetting blocks on fire or breaking blocks."""
    #     pass
    #
    # def createExplosion(Location loc,float power,boolean setFire,boolean breakBlocks,Entity source):
    #     """Creates explosion at given coordinates with given power and optionallysetting blocks on fire or breaking blocks."""
    #     pass
    #
    # def dropItem(Location location,ItemStack item):
    #     """Drops an item at the specified Location"""
    #     pass
    #
    # def dropItem(Location location,ItemStack item,Consumer<Item> function):
    #     """Drops an item at the specified LocationNote that functions will run before the entity is spawned"""
    #     pass
    #
    # def dropItemNaturally(Location location,ItemStack item):
    #     """Drops an item at the specified Location with a random offset"""
    #     pass
    #
    # def dropItemNaturally(Location location,ItemStack item,Consumer<Item> function):
    #     """Drops an item at the specified Location with a random offsetNote that functions will run before the entity is spawned"""
    #     pass
    #
    # def generateTree(Location location,TreeType type):
    #     """Creates a tree at the given Location"""
    #     pass
    #
    # def generateTree(Location loc,TreeType type,BlockChangeDelegate delegate):
    #     """Deprecated.this method does not handle tile entities (bee nests)"""
    #     pass
    #
    # def getAllowAnimals():
    #     """Gets whether animals can spawn in this world."""
    #     pass
    #
    # def getAllowMonsters():
    #     """Gets whether monsters can spawn in this world."""
    #     pass
    #
    # def getAmbientSpawnLimit():
    #     """Deprecated.Deprecated in favor of getSpawnLimit(SpawnCategory)"""
    #     pass
    #
    # def getAnimalSpawnLimit():
    #     """Deprecated.Deprecated in favor of getSpawnLimit(SpawnCategory)"""
    #     pass
    #
    # def getBiome(int x,int z):
    #     """Deprecated.biomes are now 3-dimensional"""
    #     pass
    #
    # def getBiomeProvider():
    #     """Gets the biome provider for this world"""
    #     pass
    #
    # def getBlockAt(int x,int y,int z):
    #     """Gets the Block at the given coordinates"""
    #     pass
    #
    # def getBlockAt(Location location):
    #     """Gets the Block at the given Location"""
    #     pass
    #
    # def getChunkAt(int x,int z):
    #     """Gets the Chunk at the given coordinates"""
    #     pass
    #
    # def getChunkAt(Block block):
    #     """Gets the Chunk that contains the given Block"""
    #     pass
    #
    # def getChunkAt(Location location):
    #     """Gets the Chunk at the given Location"""
    #     pass
    #
    # def getClearWeatherDuration():
    #     """Get the clear weather duration."""
    #     pass
    #
    # def getDifficulty():
    #     """Gets the Difficulty of the world."""
    #     pass
    #
    # def getEmptyChunkSnapshot(int x,int z,boolean includeBiome,boolean includeBiomeTemp):
    #     """Get empty chunk snapshot (equivalent to all air blocks), optionallyincluding valid biome data."""
    #     pass
    #
    # def getEnderDragonBattle():
    #     """Get the DragonBattle associated with this world."""
    #     pass
    #
    # def getEntities():
    #     """Get a list of all entities in this World"""
    #     pass
    #
    # def getEntitiesByClass(Class<T> cls):
    #     """Get a collection of all entities in this World matching the givenclass/interface"""
    #     pass
    #
    # def getEntitiesByClass(Class<T>... classes):
    #     """Deprecated."""
    #     pass
    #
    # def getEntitiesByClasses(Class<?>... classes):
    #     """Get a collection of all entities in this World matching any of thegiven classes/interfaces"""
    #     pass
    #
    # def getForceLoadedChunks():
    #     """Returns all force loaded chunks in this world."""
    #     pass
    #
    # def getFullTime():
    #     """Gets the full in-game time on this world"""
    #     pass
    #
    # def getGameRuleDefault(GameRule<T> rule):
    #     """Get the default value for a given GameRule."""
    #     pass
    #
    # def getGameRules():
    #     """Get an array containing the names of all the GameRules."""
    #     pass
    #
    # def getGameRuleValue(String rule):
    #     """Deprecated.use getGameRuleValue(GameRule) instead"""
    #     pass
    #
    # def getGameRuleValue(GameRule<T> rule):
    #     """Get the current value for a given GameRule."""
    #     pass
    #
    # def getGameTime():
    #     """Gets the full in-game time on this world since the world generation"""
    #     pass
    #
    # def getGenerator():
    #     """Gets the chunk generator for this world"""
    #     pass
    #
    # def getHighestBlockAt(int x,int z):
    #     """Gets the highest non-empty (impassable) block at the given coordinates."""
    #     pass
    #
    # def getHighestBlockAt(int x,int z,HeightMap heightMap):
    #     """Gets the highest block corresponding to the HeightMap at thegiven coordinates."""
    #     pass
    #
    # def getHighestBlockAt(Location location):
    #     """Gets the highest non-empty (impassable) block at the given coordinates."""
    #     pass
    #
    # def getHighestBlockAt(Location location,HeightMap heightMap):
    #     """Gets the highest block corresponding to the HeightMap at thegiven coordinates."""
    #     pass
    #
    # def getHighestBlockYAt(int x,int z):
    #     """Gets the highest non-empty (impassable) coordinate at the givencoordinates."""
    #     pass
    #
    # def getHighestBlockYAt(int x,int z,HeightMap heightMap):
    #     """Gets the highest coordinate corresponding to the HeightMap at thegiven coordinates."""
    #     pass
    #
    # def getHighestBlockYAt(Location location):
    #     """Gets the highest non-empty (impassable) coordinate at the givenLocation."""
    #     pass
    #
    # def getHighestBlockYAt(Location location,HeightMap heightMap):
    #     """Gets the highest coordinate corresponding to the HeightMap at thegiven Location."""
    #     pass
    #
    # def getHumidity(int x,int z):
    #     """Deprecated.biomes are now 3-dimensional"""
    #     pass
    #
    # def getHumidity(int x,int y,int z):
    #     """Gets the humidity for the given block coordinates."""
    #     pass
    #
    # def getKeepSpawnInMemory():
    #     """Gets whether the world's spawn area should be kept loaded into memoryor not."""
    #     pass
    #
    # def getLivingEntities():
    #     """Get a list of all living entities in this World"""
    #     pass
    #
    # def getLoadedChunks():
    #     """Gets an array of all loaded Chunks"""
    #     pass
    #
    # def getLogicalHeight():
    #     """Gets the maximum height to which chorus fruits and nether portals canbring players within this dimension."""
    #     pass
    #
    # def getMonsterSpawnLimit():
    #     """Deprecated.Deprecated in favor of getSpawnLimit(SpawnCategory)"""
    #     pass
    #
    # def getNearbyEntities(Location location,double x,double y,double z):
    #     """Returns a list of entities within a bounding box centered around aLocation."""
    #     pass
    #
    # def getNearbyEntities(Location location,double x,double y,double z,Predicate<Entity> filter):
    #     """Returns a list of entities within a bounding box centered around aLocation."""
    #     pass
    #
    # def getNearbyEntities(BoundingBox boundingBox):
    #     """Returns a list of entities within the given bounding box."""
    #     pass
    #
    # def getNearbyEntities(BoundingBox boundingBox,Predicate<Entity> filter):
    #     """Returns a list of entities within the given bounding box."""
    #     pass
    #
    # def getPlayers():
    #     """Get a list of all players in this World"""
    #     pass
    #
    # def getPluginChunkTickets():
    #     """Returns a map of which plugins have tickets for what chunks."""
    #     pass
    #
    # def getPluginChunkTickets(int x,int z):
    #     """Retrieves a collection specifying which plugins have tickets for thespecified chunk."""
    #     pass
    #
    # def getPopulators():
    #     """Gets a list of all applied BlockPopulators for this World"""
    #     pass
    #
    # def getPVP():
    #     """Gets the current PVP setting for this world."""
    #     pass
    #
    # def getRaids():
    #     """Gets all raids that are going on over this world."""
    #     pass
    #
    # def getSeaLevel():
    #     """Gets the sea level for this world."""
    #     pass
    #
    # def getSimulationDistance():
    #     """Returns the simulation distance used for this world."""
    #     pass
    #
    # def getSpawnLimit(SpawnCategory spawnCategory):
    #     """Gets the limit for number of SpawnCategory entities that can spawn in a chunk inthis world"""
    #     pass
    #
    # def getSpawnLocation():
    #     """Gets the default spawn Location of this world"""
    #     pass
    #
    # def getTemperature(int x,int z):
    #     """Deprecated.biomes are now 3-dimensional"""
    #     pass
    #
    # def getTemperature(int x,int y,int z):
    #     """Gets the temperature for the given block coordinates."""
    #     pass
    #
    # def getThunderDuration():
    #     """Get the thundering duration."""
    #     pass
    #
    # def getTicksPerAmbientSpawns():
    #     """Deprecated.Deprecated in favor of getTicksPerSpawns(SpawnCategory)"""
    #     pass
    #
    # def getTicksPerAnimalSpawns():
    #     """Deprecated.Deprecated in favor of getTicksPerSpawns(SpawnCategory)"""
    #     pass
    #
    # def getTicksPerMonsterSpawns():
    #     """Deprecated.Deprecated in favor of getTicksPerSpawns(SpawnCategory)"""
    #     pass
    #
    # def getTicksPerSpawns(SpawnCategory spawnCategory):
    #     """Gets the world's ticks per SpawnCategory mob spawns value"""
    #     pass
    #
    # def getTicksPerWaterAmbientSpawns():
    #     """Deprecated.Deprecated in favor of getTicksPerSpawns(SpawnCategory)"""
    #     pass
    #
    # def getTicksPerWaterSpawns():
    #     """Deprecated.Deprecated in favor of getTicksPerSpawns(SpawnCategory)"""
    #     pass
    #
    # def getTicksPerWaterUndergroundCreatureSpawns():
    #     """Deprecated.Deprecated in favor of getTicksPerSpawns(SpawnCategory)"""
    #     pass
    #
    # def getTime():
    #     """Gets the relative in-game time of this world."""
    #     pass
    #
    # def getViewDistance():
    #     """Returns the view distance used for this world."""
    #     pass
    #
    # def getWaterAmbientSpawnLimit():
    #     """Deprecated.Deprecated in favor of getSpawnLimit(SpawnCategory)"""
    #     pass
    #
    # def getWaterAnimalSpawnLimit():
    #     """Deprecated.Deprecated in favor of getSpawnLimit(SpawnCategory)"""
    #     pass
    #
    # def getWaterUndergroundCreatureSpawnLimit():
    #     """Deprecated.Deprecated in favor of getSpawnLimit(SpawnCategory)"""
    #     pass
    #
    # def getWeatherDuration():
    #     """Get the remaining time in ticks of the current conditions."""
    #     pass
    #
    # def getWorldBorder():
    #     """Gets the world border for this world."""
    #     pass
    #
    # def getWorldFolder():
    #     """Gets the folder of this world on disk."""
    #     pass
    #
    # def getWorldType():
    #     """Deprecated.world type is only used to select the default word generationsettings and is not stored in Vanilla worlds, making it impossible forthis method to always return the correct value."""
    #     pass
    #
    # def hasCeiling():
    #     """Gets if this world has a ceiling."""
    #     pass
    #
    # def hasRaids():
    #     """Gets if players with the bad omen effect in this world will trigger araid."""
    #     pass
    #
    # def hasSkyLight():
    #     """Gets if this world has skylight access."""
    #     pass
    #
    # def hasStorm():
    #     """Returns whether the world has an ongoing storm."""
    #     pass
    #
    # def isAutoSave():
    #     """Gets whether or not the world will automatically save"""
    #     pass
    #
    # def isBedWorks():
    #     """Gets if beds work in this world."""
    #     pass
    #
    # def isChunkForceLoaded(int x,int z):
    #     """Gets whether the chunk at the specified chunk coordinates is forceloaded."""
    #     pass
    #
    # def isChunkGenerated(int x,int z):
    #     """Checks if the Chunk at the specified coordinates is generated"""
    #     pass
    #
    # def isChunkInUse(int x,int z):
    #     """Deprecated.This method was added to facilitate chunk garbage collection."""
    #     pass
    #
    # def isChunkLoaded(int x,int z):
    #     """Checks if the Chunk at the specified coordinates is loaded"""
    #     pass
    #
    # def isChunkLoaded(Chunk chunk):
    #     """Checks if the specified Chunk is loaded"""
    #     pass
    #
    # def isClearWeather():
    #     """Returns whether the world has clear weather."""
    #     pass
    #
    # def isGameRule(String rule):
    #     """Checks if string is a valid game rule"""
    #     pass
    #
    # def isHardcore():
    #     """Gets whether the world is hardcore or not."""
    #     pass
    #
    # def isNatural():
    #     """Gets if this world is natural."""
    #     pass
    #
    # def isPiglinSafe():
    #     """Gets if this world allow to piglins to survive without shaking andtransforming to zombified piglins."""
    #     pass
    #
    # def isRespawnAnchorWorks():
    #     """Gets if this world allows players to charge and use respawn anchors."""
    #     pass
    #
    # def isThundering():
    #     """Returns whether there is thunder."""
    #     pass
    #
    # def isUltraWarm():
    #     """Gets if various water/lava mechanics will be triggered in this world, eg:Water is evaporatedSponges dryLava spreads faster and further"""
    #     pass
    #
    # def loadChunk(int x,int z):
    #     """Loads the Chunk at the specified coordinates."""
    #     pass
    #
    # def loadChunk(int x,int z,boolean generate):
    #     """Loads the Chunk at the specified coordinates."""
    #     pass
    #
    # def loadChunk(Chunk chunk):
    #     """Loads the specified Chunk."""
    #     pass
    #
    # def locateNearestRaid(Location location,int radius):
    #     """Finds the nearest raid close to the given location."""
    #     pass
    #
    # def locateNearestStructure(Location origin,Structure structure,int radius,boolean findUnexplored):
    #     """Find the closest nearby structure of a given Structure."""
    #     pass
    #
    # def locateNearestStructure(Location origin,StructureType structureType,int radius,boolean findUnexplored):
    #     """Find the closest nearby structure of a given StructureType."""
    #     pass
    #
    # def locateNearestStructure(Location origin,StructureType structureType,int radius,boolean findUnexplored):
    #     """Deprecated.UselocateNearestStructure(Location, Structure, int, boolean) orlocateNearestStructure(Location, StructureType, int, boolean)instead."""
    #     pass
    #
    # def playEffect(Location location,Effect effect,int data):
    #     """Plays an effect to all players within a default radius around a givenlocation."""
    #     pass
    #
    # def playEffect(Location location,Effect effect,int data,int radius):
    #     """Plays an effect to all players within a given radius around a location."""
    #     pass
    #
    # def playEffect(Location location,Effect effect,T data):
    #     """Plays an effect to all players within a default radius around a givenlocation."""
    #     pass
    #
    # def playEffect(Location location,Effect effect,T data,int radius):
    #     """Plays an effect to all players within a given radius around a location."""
    #     pass
    #
    # def playSound(Entity entity,String sound,float volume,float pitch):
    #     """Play a Sound at the location of the provided entity in the World."""
    #     pass
    #
    # def playSound(Entity entity,String sound,SoundCategory category,float volume,float pitch):
    #     """Play a Sound at the location of the provided entity in the World."""
    #     pass
    #
    # def playSound(Entity entity,Sound sound,float volume,float pitch):
    #     """Play a Sound at the location of the provided entity in the World."""
    #     pass
    #
    # def playSound(Entity entity,Sound sound,SoundCategory category,float volume,float pitch):
    #     """Play a Sound at the location of the provided entity in the World."""
    #     pass
    #
    # def playSound(Location location,String sound,float volume,float pitch):
    #     """Play a Sound at the provided Location in the World."""
    #     pass
    #
    # def playSound(Location location,String sound,SoundCategory category,float volume,float pitch):
    #     """Play a Sound at the provided Location in the World."""
    #     pass
    #
    # def playSound(Location location,Sound sound,float volume,float pitch):
    #     """Play a Sound at the provided Location in the World."""
    #     pass
    #
    # def playSound(Location location,Sound sound,SoundCategory category,float volume,float pitch):
    #     """Play a Sound at the provided Location in the World."""
    #     pass
    #
    # def rayTrace(Location start,Vector direction,double maxDistance,FluidCollisionMode fluidCollisionMode,boolean ignorePassableBlocks,double raySize,Predicate<Entity> filter):
    #     """Performs a ray trace that checks for both block and entity collisions."""
    #     pass
    #
    # def rayTraceBlocks(Location start,Vector direction,double maxDistance):
    #     """Performs a ray trace that checks for block collisions using the blocks'precise collision shapes."""
    #     pass
    #
    # def rayTraceBlocks(Location start,Vector direction,double maxDistance,FluidCollisionMode fluidCollisionMode):
    #     """Performs a ray trace that checks for block collisions using the blocks'precise collision shapes."""
    #     pass
    #
    # def rayTraceBlocks(Location start,Vector direction,double maxDistance,FluidCollisionMode fluidCollisionMode,boolean ignorePassableBlocks):
    #     """Performs a ray trace that checks for block collisions using the blocks'precise collision shapes."""
    #     pass
    #
    # def rayTraceEntities(Location start,Vector direction,double maxDistance):
    #     """Performs a ray trace that checks for entity collisions."""
    #     pass
    #
    # def rayTraceEntities(Location start,Vector direction,double maxDistance,double raySize):
    #     """Performs a ray trace that checks for entity collisions."""
    #     pass
    #
    # def rayTraceEntities(Location start,Vector direction,double maxDistance,double raySize,Predicate<Entity> filter):
    #     """Performs a ray trace that checks for entity collisions."""
    #     pass
    #
    # def rayTraceEntities(Location start,Vector direction,double maxDistance,Predicate<Entity> filter):
    #     """Performs a ray trace that checks for entity collisions."""
    #     pass
    #
    # def refreshChunk(int x,int z):
    #     """Deprecated.This method is not guaranteed to work suitably across all client implementations."""
    #     pass
    #
    # def regenerateChunk(int x,int z):
    #     """Deprecated.regenerating a single chunk is not likely to produce the samechunk as before as terrain decoration may be spread across chunks."""
    #     pass
    #
    # def removePluginChunkTicket(int x,int z,Plugin plugin):
    #     """Removes the specified plugin's ticket for the specified chunk"""
    #     pass
    #
    # def removePluginChunkTickets(Plugin plugin):
    #     """Removes all plugin tickets for the specified plugin"""
    #     pass
    #
    # def save():
    #     """Saves world to disk"""
    #     pass
    #
    # def setAmbientSpawnLimit(int limit):
    #     """Deprecated.Deprecated in favor of setSpawnLimit(SpawnCategory, int)"""
    #     pass
    #
    # def setAnimalSpawnLimit(int limit):
    #     """Deprecated.Deprecated in favor of getSpawnLimit(SpawnCategory)"""
    #     pass
    #
    # def setAutoSave(boolean value):
    #     """Sets whether or not the world will automatically save"""
    #     pass
    #
    # def setBiome(int x,int z,Biome bio):
    #     """Deprecated.biomes are now 3-dimensional"""
    #     pass
    #
    # def setChunkForceLoaded(int x,int z,boolean forced):
    #     """Sets whether the chunk at the specified chunk coordinates is forceloaded."""
    #     pass
    #
    # def setClearWeatherDuration(int duration):
    #     """Set the clear weather duration."""
    #     pass
    #
    # def setDifficulty(Difficulty difficulty):
    #     """Sets the Difficulty of the world."""
    #     pass
    #
    # def setFullTime(long time):
    #     """Sets the in-game time on the server"""
    #     pass
    #
    # def setGameRule(GameRule<T> rule,T newValue):
    #     """Set the given GameRule's new value."""
    #     pass
    #
    # def setGameRuleValue(String rule,String value):
    #     """Deprecated.use setGameRule(GameRule, Object) instead."""
    #     pass
    #
    # def setHardcore(boolean hardcore):
    #     """Sets whether the world is hardcore or not."""
    #     pass
    #
    # def setKeepSpawnInMemory(boolean keepLoaded):
    #     """Sets whether the world's spawn area should be kept loaded into memoryor not."""
    #     pass
    #
    # def setMonsterSpawnLimit(int limit):
    #     """Deprecated.Deprecated in favor of setSpawnLimit(SpawnCategory, int)"""
    #     pass
    #
    # def setPVP(boolean pvp):
    #     """Sets the PVP setting for this world."""
    #     pass
    #
    # def setSpawnFlags(boolean allowMonsters,boolean allowAnimals):
    #     """Sets the spawn flags for this."""
    #     pass
    #
    # def setSpawnLimit(SpawnCategory spawnCategory,int limit):
    #     """Sets the limit for number of SpawnCategory entities that can spawn in a chunk inthis world"""
    #     pass
    #
    # def setSpawnLocation(int x,int y,int z):
    #     """Sets the spawn location of the world"""
    #     pass
    #
    # def setSpawnLocation(int x,int y,int z,float angle):
    #     """Sets the spawn location of the world"""
    #     pass
    #
    # def setSpawnLocation(Location location):
    #     """Sets the spawn location of the world."""
    #     pass
    #
    # def setStorm(boolean hasStorm):
    #     """Set whether there is a storm."""
    #     pass
    #
    # def setThunderDuration(int duration):
    #     """Set the thundering duration."""
    #     pass
    #
    # def setThundering(boolean thundering):
    #     """Set whether it is thundering."""
    #     pass
    #
    # def setTicksPerAmbientSpawns(int ticksPerAmbientSpawns):
    #     """Deprecated.Deprecated in favor of setTicksPerSpawns(SpawnCategory, int)"""
    #     pass
    #
    # def setTicksPerAnimalSpawns(int ticksPerAnimalSpawns):
    #     """Deprecated.Deprecated in favor of setTicksPerSpawns(SpawnCategory, int)"""
    #     pass
    #
    # def setTicksPerMonsterSpawns(int ticksPerMonsterSpawns):
    #     """Deprecated.Deprecated in favor of setTicksPerSpawns(SpawnCategory, int)"""
    #     pass
    #
    # def setTicksPerSpawns(SpawnCategory spawnCategory,int ticksPerCategorySpawn):
    #     """Sets the world's ticks per SpawnCategory mob spawns value"""
    #     pass
    #
    # def setTicksPerWaterAmbientSpawns(int ticksPerAmbientSpawns):
    #     """Deprecated.Deprecated in favor of setTicksPerSpawns(SpawnCategory, int)"""
    #     pass
    #
    # def setTicksPerWaterSpawns(int ticksPerWaterSpawns):
    #     """Deprecated.Deprecated in favor of setTicksPerSpawns(SpawnCategory, int)"""
    #     pass
    #
    # def setTicksPerWaterUndergroundCreatureSpawns(int ticksPerWaterUndergroundCreatureSpawns):
    #     """Deprecated.Deprecated in favor of setTicksPerSpawns(SpawnCategory, int)"""
    #     pass
    #
    # def setTime(long time):
    #     """Sets the relative in-game time on the server."""
    #     pass
    #
    # def setWaterAmbientSpawnLimit(int limit):
    #     """Deprecated.Deprecated in favor of setSpawnLimit(SpawnCategory, int)"""
    #     pass
    #
    # def setWaterAnimalSpawnLimit(int limit):
    #     """Deprecated.Deprecated in favor of setSpawnLimit(SpawnCategory, int)"""
    #     pass
    #
    # def setWaterUndergroundCreatureSpawnLimit(int limit):
    #     """Deprecated.Deprecated in favor of setSpawnLimit(SpawnCategory, int)"""
    #     pass
    #
    # def setWeatherDuration(int duration):
    #     """Set the remaining time in ticks of the current conditions."""
    #     pass
    #
    # def spawnArrow(Location location,Vector direction,float speed,float spread):
    #     """Creates an Arrow entity at the given Location"""
    #     pass
    #
    # def spawnArrow(Location location,Vector direction,float speed,float spread,Class<T> clazz):
    #     """Creates an arrow entity of the given class at the given Location"""
    #     pass
    #
    # def spawnFallingBlock(Location location,BlockData data):
    #     """Spawn a FallingBlock entity at the given Location ofthe specified Material."""
    #     pass
    #
    # def spawnFallingBlock(Location location,MaterialData data):
    #     """Spawn a FallingBlock entity at the given Location ofthe specified Material."""
    #     pass
    #
    # def spawnFallingBlock(Location location,Material material,byte data):
    #     """Deprecated.Magic value"""
    #     pass
    #
    # def spawnParticle(Particle particle,double x,double y,double z,int count):
    #     """Spawns the particle (the number of times specified by count)at the target location."""
    #     pass
    #
    # def spawnParticle(Particle particle,double x,double y,double z,int count,double offsetX,double offsetY,double offsetZ):
    #     """Spawns the particle (the number of times specified by count)at the target location."""
    #     pass
    #
    # def spawnParticle(Particle particle,double x,double y,double z,int count,double offsetX,double offsetY,double offsetZ,double extra):
    #     """Spawns the particle (the number of times specified by count)at the target location."""
    #     pass
    #
    # def spawnParticle(Particle particle,double x,double y,double z,int count,double offsetX,double offsetY,double offsetZ,double extra,T data):
    #     """Spawns the particle (the number of times specified by count)at the target location."""
    #     pass
    #
    # def spawnParticle(Particle particle,double x,double y,double z,int count,double offsetX,double offsetY,double offsetZ,double extra,T data,boolean force):
    #     """Spawns the particle (the number of times specified by count)at the target location."""
    #     pass
    #
    # def spawnParticle(Particle particle,double x,double y,double z,int count,double offsetX,double offsetY,double offsetZ,T data):
    #     """Spawns the particle (the number of times specified by count)at the target location."""
    #     pass
    #
    # def spawnParticle(Particle particle,double x,double y,double z,int count,T data):
    #     """Spawns the particle (the number of times specified by count)at the target location."""
    #     pass
    #
    # def spawnParticle(Particle particle,Location location,int count):
    #     """Spawns the particle (the number of times specified by count)at the target location."""
    #     pass
    #
    # def spawnParticle(Particle particle,Location location,int count,double offsetX,double offsetY,double offsetZ):
    #     """Spawns the particle (the number of times specified by count)at the target location."""
    #     pass
    #
    # def spawnParticle(Particle particle,Location location,int count,double offsetX,double offsetY,double offsetZ,double extra):
    #     """Spawns the particle (the number of times specified by count)at the target location."""
    #     pass
    #
    # def spawnParticle(Particle particle,Location location,int count,double offsetX,double offsetY,double offsetZ,double extra,T data):
    #     """Spawns the particle (the number of times specified by count)at the target location."""
    #     pass
    #
    # def spawnParticle(Particle particle,Location location,int count,double offsetX,double offsetY,double offsetZ,double extra,T data,boolean force):
    #     """Spawns the particle (the number of times specified by count)at the target location."""
    #     pass
    #
    # def spawnParticle(Particle particle,Location location,int count,double offsetX,double offsetY,double offsetZ,T data):
    #     """Spawns the particle (the number of times specified by count)at the target location."""
    #     pass
    #
    # def spawnParticle(Particle particle,Location location,int count,T data):
    #     """Spawns the particle (the number of times specified by count)at the target location."""
    #     pass
    #
    # def spigot():
    #     """"""
    #     pass
    #
    # def strikeLightning(Location loc):
    #     """Strikes lightning at the given Location"""
    #     pass
    #
    # def strikeLightningEffect(Location loc):
    #     """Strikes lightning at the given Location without doing damage"""
    #     pass
    #
    # def unloadChunk(int x,int z):
    #     """Safely unloads and saves the Chunk at the specified coordinates"""
    #     pass
    #
    # def unloadChunk(int x,int z,boolean save):
    #     """Safely unloads and optionally saves the Chunk at the specifiedcoordinates."""
    #     pass
    #
    # def unloadChunk(Chunk chunk):
    #     """Safely unloads and saves the Chunk at the specified coordinates"""
    #     pass
    #
    # def unloadChunkRequest(int x,int z):
    #     """Safely queues the Chunk at the specified coordinates forunloading."""
    #     pass
