import re
from .Actor import Actor

class PhoenixDictionary(object):
    """An object representing a Phoenix Dictionary.
    
    Attributes:
        
    """

    def __init__(self):
        """Return a new instance of PhenixDictionary.
        """
        
        self.phoenix_text = []
        self.country_list = []
        self.actor_list = []
    
    def load_actor_dictionary(self, path):
        with open(path) as f:
            self.phoenix_text = f.read().splitlines()
            
    def get_phoenix_text(self):
        return self.phoenix_text
        
    def get_country_list(self):
        return self.country_list
    
    def get_actor_list(self):
        return self.actor_list
        
    def make_country_list(self):
        # Make a list of country terms
        if len(self.phoenix_text) == 0:
            raise Exception("You must have a phoenix_text object before calling `make_country_list`. Load a python_text object by calling `load_actor_dictionary`.")
        
        saving = False
        for line in self.phoenix_text:
            toplevel = False
            if re.search("^\+",line) is None:
                saving = False
            if re.search("^[A-Z].+[A-Z]\]$",line) is not None:
                ccode = re.search("(?<=\[)[A-Z]+",line)
                country = re.search(".+(?=\[)",line).group(0)
                country = re.sub("#.+$","",country)
                country = re.sub("_*\s.*$","",country)
                saving = True
                toplevel = True
                self.country_list.append([[ccode.group(0)],[country]])
            if saving is True and toplevel is False:
                try:
                    altname = re.sub("#.+$","",line)
                    altname = re.sub("[\s_]*$","",altname)
                    altname = re.sub("[^A-Za-z0-9_]","",altname)
                    altname = re.sub("^\+","",altname)
                    self.country_list[len(self.country_list)-1][1].append(altname)
                except:
                    pass

    def make_actor_list(self):
        # Make a list of actor terms
        if len(self.phoenix_text) == 0:
            raise Exception("You must have a phoenix_text object before calling `make_country_list`. Load a python_text object by calling `load_actor_dictionary`.")
        
        saving = False
        for line in self.phoenix_text:
            toplevel = False
            if re.search("^\+",line) is None and re.search("^\s+\[",line) is None:
                saving = False
            if re.search("^[A-Z].+;",line) is not None:
                actor = re.search("^.+(?=;)",line)
                actor = re.sub("[\s_]+$","",actor.group(0))
                self.actor_list.append([[],[actor]])
                saving = True
                toplevel = True
            if saving is True and toplevel is False:
                if re.search("^\+",line) is not None:
                    altname = re.sub("#.+$","",line)
                    altname = re.sub("[\s_]+$","",altname)
                    altname = re.sub("^\+","",altname)
                    self.actor_list[len(self.actor_list)-1][1].append(altname)
                    # actor_list[len(actor_list)].append(altname)
                if re.search("\[[A-Z]",line) is not None:
                    sector = re.search("(?<=\[)[A-Z]+",line)
                    sector = sector.group(0)
                    try:
                        dates = re.search("[0-9]+[-]*[0-9]*", line).group(0).split("-")
                        if len(dates) == 1:
                            dates = dates + ("Present",)
                    except:
                        dates = ("Present","Present")
                    self.actor_list[len(self.actor_list)-1][0].append((sector, dates[0], dates[1]))
                    
        self.actor_list = [Actor(a[1][0], a[1], a[0]) for a in self.actor_list]
                    
        