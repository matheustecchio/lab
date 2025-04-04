class Set:
    def __init__(self, set_id, title, pieces, rrp, stock):
        self.set_id = set_id
        self.title = title
        self.pieces = pieces
        self.rrp = rrp
        self.stock = stock

    def __str__(self):
        return f"Set ID: {self.set_id}, Title: {self.title}, Pieces: {self.pieces}, RRP: {self.rrp}, Stock: {self.stock}"