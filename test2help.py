import cv2
from aiohttp import web
from narerundar import  narerundar

async def handle_poll(request):
    return web.Response(text="OK")

async def handle_runopencv(request):
    print("run opencv")
    narerundar().runNarerundar()
    return web.Response(text="OK")

app = web.Application()
app.router.add_get('/poll', handle_poll)
app.router.add_get('/runOpenCV', handle_runopencv)
web.run_app(app, host='127.0.0.1', port=12345)

