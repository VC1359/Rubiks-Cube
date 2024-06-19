class edge_p:
    def __init__(self, id, orientation, colors, faces):
        self.name = id # "1"
        self.ort = orientation # [F] (defines normal for whites and yellow)
        self.colors = colors # (red, blue)
        self.faces = faces # [F, R]
    
class corner_p:
    def __init__(self, id, orientation, colors, faces):
        self.name = id 
        self.ort = orientation 
        self.colors = colors # (red, blue, yellow)
        self.faces = faces # [F, R, U]
        
class center_p:
    def __init__(self, id, orientation, color, face):
        self.name = id 
        self.ort = orientation
        self.colors = color # (red)
        self.faces = face # [F]

# White Cross (ID: 25 23 21 19)
def white_cross():
    pass


def solve(state):
    #expect recursive
    pass