class Document:
    def __init__(self):
        self.cursor = 0
        self.left = 0
        self.right = 0
        self.text = ""
        self.history = []
        self.redoStack = []
        self.undoStack = []
        self.copied = ""
    
    def append(self, txt):
        if len(txt) > 0:
            self.undoStack.append((self.text, self.left, self.right, self.cursor))
            self.redoStack = []
            if self.right == 0 and self.left == 0:
                self.text = self.text[:self.cursor] + txt + self.text[self.cursor:]
                self.cursor += len(txt)
            else:
                self.text = self.text[:self.left] + txt + self.text[self.right:]
                self.cursor = self.left + len(txt)
                self.left = 0
                self.right = 0
        self.history.append(self.text)
        return self.text
    
    def backspace(self):
        self.undoStack.append((self.text, self.left, self.right, self.cursor))
        self.redoStack = []
        if self.cursor > 0 and self.left == 0 and self.right == 0:
            self.text = self.text[:self.cursor-1] + self.text[self.cursor:]
            self.cursor -= 1
            self.history.append(self.text)
        else:
            self.text = self.text[:self.left] + self.text[self.right:]
            self.cursor = self.left
            self.left = 0
            self.right = 0
            self.history.append(self.text)
        return self.text

    def move(self, pos):
        if pos < 0:
            self.cursor = 0
        else:
            self.cursor = min(pos, len(self.text))
        self.left = 0
        self.right = 0
    
    def select(self, left, right):
        self.left = max(0, left)
        self.right = min(right, len(self.text))
    
    def copy(self):
        if self.left != self.right:
            self.copied = self.text[self.left:self.right]

    def paste(self):
        if len(self.copied) > 0:
            self.undoStack.append((self.text, self.left, self.right, self.cursor))
            self.redoStack = []
            self.append(self.copied)
    
    def undo(self):
        if len(self.undoStack) > 0:
            self.redoStack.append((self.text, self.left, self.right, self.cursor))
            self.text, self.left, self.right, self.cursor = self.undoStack.pop()
            self.history.append(self.text)

    def redo(self):
        if len(self.redoStack) > 0:
            self.undoStack.append((self.text, self.left, self.right, self.cursor))
            self.text, self.left, self.right, self.cursor = self.redoStack.pop()
            self.history.append((self.text, self.left, self.right, self.cursor))
    

