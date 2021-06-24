class Element:

    def setPosition(obj, Position_x, Position_y):
        obj.posx = Position_x
        obj.posy = Position_y

    def setDimension(obj, width, height):
        obj.width = width
        obj.height = height

    def getPosition(obj):
        return obj.posx, obj.posy

    def getDimension(obj):
        return obj.width, obj.height
