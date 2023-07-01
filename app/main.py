# from typing import Union

from fastapi import FastAPI
import os

app = FastAPI()


@app.get("/")
def read_root():
    # return {"Hello": "k8s World"}
    return {"Hello": f"From: {os.environ.get('HOSTNAME', 'DEFAULT_ENV')}"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
