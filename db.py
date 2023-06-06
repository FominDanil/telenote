class Db:
    def __init__(self):
        self.q = {}

    def add(self, uid, text):
        if not (self.q.get(uid)):
            self.q[uid] = [text]
        else:
            self.q[uid].append(text)
