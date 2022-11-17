from typing import Union

import pandas as pd
import uvicorn
from fastapi import FastAPI
import awswrangler as wr

import package_a as pa
import package_b as pb
from typing import Dict, Any

app = FastAPI()


@app.get("/")
def read_root() -> Dict[str, str]:
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None) -> Dict[str, Any]:
    return {
        "item_id": item_id,
        "pa_version": pa.__version__,
        "pb_version": pb.__version__,
        "pd_version": pd.__version__,
        "awswrangler_version": wr.__version__,
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=9000, reload=True)  # nosec B104
