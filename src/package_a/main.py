from typing import Union

import pandas as pd
import uvicorn
from fastapi import FastAPI

import package_a as pa
import package_b as pb

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {
        "item_id": item_id,
        "pa_version": pa.__version__,
        "pb_version": pb.__version__,
        "pd_versiob": pd.__version__,
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)  # nosec B104
