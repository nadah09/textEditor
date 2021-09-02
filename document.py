class Document:
    def __init__(self):
        self.cursor = 0
        self.left = 0
        self.right = 0
        self.text = ""
        self.history = []
        self.redoStack = []
        self.undoStack = []
    
    def append(self, txt):
        self.text = self.text[:self.cursor] + txt + self.text[self.cursor:]
        self.cursor += len(txt)
        self.history.append(self.text)
        return self.text
    
    def backspace(self):
        if self.cursor > 0:
            self.text = self.text[:self.cursor-1] + self.text[self.cursor:]
            self.cursor -= 1
            self.history.append(self.text)
        return self.text

    def move(self, pos):
        if pos < 0:
            self.cursor = 0
        else:
            self.cursor = min(pos, len(self.text))
