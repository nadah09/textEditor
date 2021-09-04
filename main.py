import document as d

def edit_document(doc, txt):
    command = txt.split(" ")[0]
    print(command)
    if command == "APPEND":
        toAppend = txt.split(" ")[1]
        doc.append(toAppend)
    elif command == "BACKSPACE":
        doc.backspace()
    elif command == "MOVE":
        pos = int(txt.split(" ")[1])
        doc.move(pos)
    elif command == "SELECT":
        left, right = int(txt.split(" ")[1]), int(txt.split(" ")[2])
        doc.select(left, right)
    elif command == "COPY":
        doc.copy()
    elif command == "PASTE":
        doc.paste()
    elif command == "UNDO":
        doc.undo()
    elif command == "REDO":
        doc.redo()

    return doc.text

def setup_document(name):
    doc = d.Document()
    return doc


    



if __name__=="__main__":
    doc = setup_document("doc1")
    docs = {}
    docs["doc1"] = doc
    print("Welcome to Text Editor! To quit, type 'QUIT'.")
    while True:
        txt = input("Enter a new command: ")
        if txt == "QUIT":
            break
        if txt.split(" ")[0] == "CREATE":
            name = txt.split(" ")[1]
            if name not in docs:
                doc = setup_document(name)
                docs[name] = doc   
        if txt.split(" ")[0] == "SWITCH":
            name = txt.split(" ")[1]
            if name in docs:
                doc = docs[name]
                print(doc.text)
        else:
            edit = edit_document(doc, txt)
            print(edit)