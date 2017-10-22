import cv2
from aiohttp import web
from narerundar import  narerundar

async def handle_poll(request):
    return web.Response(text="OK")

async def handle_beep(request):
    print("play beep!")
    print("\007")
    return web.Response(text="OK")

async def handle_setvolume(request):
    volume = int(request.match_info['vol'])
    if volume >= 0 and volume <= 10:

        print("set volume= " + str(volume))
    else:
        print("out of range: " + str(volume))
    return web.Response(text="OK")

async def handle_runopencv(request):
    print("run opencv")
    narerundar().runNarerundar()
    return web.Response(text="OK")

app = web.Application()
app.router.add_get('/playBeep', handle_beep)
app.router.add_get('/runOpenCV', handle_runopencv)
app.router.add_get('/poll', handle_poll)
app.router.add_get('/setVolume/{vol}', handle_setvolume)
web.run_app(app, host='127.0.0.1', port=12345)

