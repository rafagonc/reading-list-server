from models.note import Note

def note_from_id(note_id):
	return Note.query.filter(Note.id == note_id).first()