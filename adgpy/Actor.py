class Actor(object):
    """ An object representing an actor.
    
    Attributes:
        
    """
    
    def __init__(self, canonical_name=None, all_names=None, sectors=None):
        
        if canonical_name is None:
            self.canonical_name = ""
        else:
            self.canonical_name = canonical_name
        
        if all_names is None:
            self.names = []
        else:
            self.names = all_names
        
        if sectors is None:
            self.sectors = []
        else:
            self.sectors = sectors
        
    def __repr__(self):
        print(str(self.canonical_name) + "\n" + ", ".join([str(a) for a in self.names]) + "\n" + ", ".join([str(a) + " " + str(b) + " " + str(c) for a, b, c in self.sectors]))
        
    def set_canonical_name(self, name):
        self.canonical_name = name
    
    def set_names(self, names):
        self.names = names
    
    def set_sectors(self, sectors):
        sectors.sort(key=lambda tup: tup[2], reverse=True) 
        self.sectors = sectors
        
    def get_canonical_name(self):
        return self.canonical_name
    
    def get_names(self):
        return self.names
    
    def get_sectors(self):
        return self.sectors
    
    def get_latest_sector(self):
        return self.sectors[0]