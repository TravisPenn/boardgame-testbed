

class mission_manager(map, pieces, mission):
    def __init__(self):
        self.map = map
        self.pieces = pieces
        self.mission = mission
        self.exhaustedlist = []
        self.depletedlist = []
        self.defeatedlist = []
        self.inplaylist = []
        self.threatcount = 0
        self.roundcount = 0


    def load_mission(self):
        ## unpack misson > set threat_count
        pass


    def load_inplay(self):
        ## unpack pieces, map, mission 
        pass
        

    def round_count(self):
        return self.roundcount


    def threat_count(self):
        return self.threatcount