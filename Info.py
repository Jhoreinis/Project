class Info:
    def __init__(self, data: str):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return str(self.data)
