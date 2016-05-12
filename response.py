import json

class Response(object):
	def __init__(self, success, message, data):
		super(Response, self).__init__()
		self.success = success
		self.message = message
		self.data = data

	def output(self):
		return {'success' : self.success, 'message' : self.message, 'data' : json.loads(self.data) if self.data is not None else self.data}
