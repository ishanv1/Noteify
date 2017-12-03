import evernote.edam.type.ttypes as Types
from evernote.api.client import EvernoteClient
developer_token = "S=s1:U=9438f:E=1677195eabf:C=16019e4bc48:P=1cd:A=en-devtoken:V=2:H=0c8e2805d803b18abd7da5dcc23d9c1a"

# Set up the NoteStore client
client = EvernoteClient(token=developer_token)
noteStore = client.get_note_store()
note = Types.Note()
note.title = "I'm a test note!"
cont = "Default Text"
note.content = '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">'
note.content += '<en-note>' + cont + '</en-note>'
note = noteStore.createNote(note)

# Make API calls
notebooks = noteStore.listNotebooks()
#for notebook in notebooks:
#    print ("Notebook: ", notebook.name)
