RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'DELETE']
SERVER_NAME = None
MONGO_HOST = 'mongo'
MONGO_PORT = 27017
#BACKENDS = ['aleph', 'beth']
BACKENDS = ['localhost:55555', 'localhost:55554']
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
