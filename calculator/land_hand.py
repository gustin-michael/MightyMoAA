class land_hand:
    def __init__(self,inf=0,art=0,tan=0,fig=0,bom=0,ant=0):
        self.infantry = inf
        self.artillery = art
        self.tank = tan
        self.fighter = fig
        self.bomber = bom
        self.anti_aircraft = ant

    def toString(self):
        return("Infantry: " + str(self.infantry) + 
               " - Artilery: " + str(self.artillery) + 
               " - Tank: " + str(self.tank) + 
               " - Fighter: " + str(self.fighter) + 
               " - Bomber: " + str(self.bomber) + 
               " - Anti-Aircraft: " + str(self.anti_aircraft))