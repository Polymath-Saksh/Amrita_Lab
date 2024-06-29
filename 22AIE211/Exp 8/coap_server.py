import asyncio
from aiocoap import *
class CoAPServer(resource.Resource):
	async def render_get(self, request):
		return Message(payload=b"Hello CoAP!")

async def main():
	root = resource.Site()
	root.add_resource(['test'], CoAPServer())
	await Context.create_server_context(root)
	await asyncio.get_running_loop().create_future()

asyncio.run(main())
