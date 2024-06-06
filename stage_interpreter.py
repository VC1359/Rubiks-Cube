class edge_p:
    def __init__(self, pos, rot, colors):
    self.pos = pos # [x, y, z]
    self.rot = rot # [x, y, z]
    self.colors = colors # (a, b, c)
    
class corner_p:
    def __init__(self, pos, rot, colors):
    self.pos = pos # [x, y, z]
    self.rot = rot # [x, y, z]
    self.colors = colors # (a, b)
    
class center_p:
    def __init__(self, pos, color):
    self.pos = pos # [x, y, z]
    self.color = colors # (a)