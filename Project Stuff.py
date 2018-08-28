
def maintain_levels():
    
Class Tank(object):
    
    def __init__(self, level):
        self.fluid_level = level
        
    def set_level(self, level):
        self.fluid_level = level
        
    def get_level(self):
        return self.fluid_level
    
    def maintain(self, get_level):
        if get_level >= 1000:
            print( WARNING OVERFLOW!)
            
            
        
        