import asyncio
from aiocoap import *

async def main():
	protocol = await Context.create_client_context()
	request = Message(code=GET, uri='coap://localhost/test')
	response = await protocol.request(request).response
	print('Result: %s\n%r' % (response.code, response.payload))

asyncio.run(main())