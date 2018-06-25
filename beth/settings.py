RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'DELETE']
SERVER_NAME = None
MONGO_HOST = 'mongo'
MONGO_PORT = 27017
DOMAIN = {
    'device': {
        'schema': {
            'name': {
                'type': 'string',
                'unique': True,
                'required': True,
            },
            'uid': {
                'type': 'integer',
                'required': True,
            },
            'type': {
                'type': 'string',
                'required': True,
            },
	    'price': {
		 'type': 'float',
		 'required': True,
             },

        }
    }
}
