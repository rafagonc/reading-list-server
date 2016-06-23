from exc.invalid_note import InvalidNoteException

def validate(note_dict):
	text = note_dict['text']
	if len(text) == 0:
		raise InvalidNoteException