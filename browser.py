import os
import asyncio
from aiohttp import web

async def handle(request):
    name = request.match_info.get('name', "/")
    if name[0] != "/":
        name = "/" + name

    cmd = "ls -l " + name

    p = await asyncio.create_subprocess_shell(cmd,
                                              stdout=asyncio.subprocess.PIPE,
                                              stderr=asyncio.subprocess.PIPE)
    returncode = await p.wait()
    out = (await p.stdout.read()).decode("utf-8")
    print(out)

    return web.Response(text=out)

app = web.Application()
app.router.add_get('/', handle)
app.router.add_get(r'/{name:.+}', handle)


port = os.getenv('VCAP_APP_PORT', '5000')
if __name__ == "__main__":
    web.run_app(app, port=int(port))
