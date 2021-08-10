class node:
    def __init__(self):
        self.unit = "-"
        self.occupied = False
        self.topRight = None
        self.top = None
        self.topLeft = None
        self.left = None
        self.right = None
        self.bottomLeft = None
        self.bottom = None
        self.bottomRight = None

    def default(self):
      self.unit = "-"
      self.occupied = False