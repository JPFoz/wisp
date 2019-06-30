import asyncio
import datetime
from datetime import timedelta
import websockets
from utils.db_accessor import DbAccessor

accessor = DbAccessor()


async def serve_client(websocket, path):
    print(path)
    while True:
        if 'wind' in path:
            latest = accessor.get_wind_speed_data(datetime.datetime.now(),datetime.datetime.now() - timedelta(seconds=5))
            print(latest)
            await websocket.send(str(latest))
            await asyncio.sleep(5)

start_server = websockets.serve(serve_client, '192.168.3.7', 5000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
