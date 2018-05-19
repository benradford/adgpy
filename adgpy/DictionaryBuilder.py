from .PhoenixDictionary import PhoenixDictionary
from gensim.models import Word2Vec

class SupervisedDictionaryBuilder(object):
    
    def __init__(self):
        self.phoenix_dict = PhoenixDictionary()
        self.w2v_model = None
        self.actor_vectors = []
        self.location_vectors = []
        
        
    ######################################################
    ## Initialization methods for dictionary and W2V model
    def load_phoenix_dictionary(self, path):
        self.phoenix_dict.load_actor_dictionary(path)
        self.phoenix_dict.make_actor_list()
        self.phoenix_dict.make_country_list()
    
    def load_w2v_model(self, path):
        try:
            self.w2v_model = Word2Vec.load(path)
        except:
            self.w2v_model = Word2Vec.load_word2vec_format(path, binary=True)
        if self.w2v_model is None:
            raise Exception("Please supply a valid Word2Vec model.")
    ## End initialization methods for dictionary and W2V model
    ##########################################################
    
    
    ###################################
    ## Get methods for class attributes
    def get_phoenix_dict(self):
        return self.phoenix_dict
    
    def get_w2v_model(self):
        return self.w2v_model
    
    def get_actor_vectors(self):
        return self.actor_vectors
    
    def get_location_vectors(self):
        return self.location_vectors
    ## End get methods for class attributes
    #######################################
    
    
    def make_actor_vectors(self):
        
        actor_list = self.phoenix_dict.get_actor_list()

        ## Note that this differs from Cylicon text
        ## actor[0][1].title only
        for actor in actor_list:
            for pseudonym in actor[1]:
                for case in {pseudonym, pseudonym.title(), pseudonym.upper(), pseudonym.lower()}:
                    try:
                        actor_vector = self.w2v_model[case]
                        actor_desc = actor[0]
                        actor_ccode = [c[0:3] for c in actor[0]]
                        actor_sector = [s[3:6] for s in actor[0]]
                        actor_tuple = {"name":case, "vector":actor_vector, "cameo":actor_desc, "ccode":actor_ccode, "scode":actor_sector}
                        self.actor_vectors.append(actor_tuple)
                    except:
                        pass

    def make_location_vectors(self):
        
        country_list = self.phoenix_dict.get_country_list()
        
        ## Note that this differs from Cylicon text
        ## location.title() only
        for country in country_list:
            ccode = country[0][0]
            all_countries = country[1]
            for location in all_countries:
                for case in {location, location.title(), location.upper(), location.lower()}:
                    try:
                        location_vector = self.w2v_model[case]
                        location_tuple = {"name":case, "vector":location_vector, "ccode":ccode}
                        self.location_vectors.append(location_tuple)
                    except:
                        pass
