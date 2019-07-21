import asyncio
import datetime
from datetime import timedelta
import websockets
import json
from utils.db_accessor import DbAccessor
import os

accessor = DbAccessor()


async def serve_client(websocket, path):
    while True:
        latest = accessor.get_wind_speed_measurements(datetime.datetime.now() - timedelta(minutes=3), datetime.datetime.now())
        results = json.dumps([{"wind_speed": item["wind_speed"], "date_created": str(item["date_created"])} for item in latest])
        await websocket.send(results)
        await asyncio.sleep(5)

if __name__ == '__main__':
    start_server = websockets.serve(serve_client, os.environ["WISP_WEBSOCKET_IP"], int(os.environ["WISP_WEBSOCKET_PORT"]))
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
