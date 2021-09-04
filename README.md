# textEditor
Command line text editor. Run main.py and use the following commands to edit your text.

COMMANDS:

APPEND <text>: Adds text wherever the cursor or selected text is.
  
MOVE <cursor position>: Moves the cursor to the position right after the index provided.
  
BACKSPACE: Deletes the character directly before the cursor, or deletes the selected text.
  
SELECT <left> <right>: Selects the text between the left and right positions provided.
  
COPY: Copies selected text if any.
  
PASTE: Pastes copied text in cursor position or in place of selected text, if copied text exists.
  
UNDO: Reverts to state before previous command.
  
REDO: Reverts an undo command if it was performed immediately before the REDO is given.
  
CREATE <file name>: Creates a new file.
  
SWITCH <file name>: Switches to a previously created file and loads its contents, if the file exists.
  
QUIT: Exit text editor.
