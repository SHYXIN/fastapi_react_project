from fastapi import FastAPI, Cookie
from typing import Optional

app = FastAPI()

@app.get('/cookies')
async def read_cookies(
    foo: Optional[str] = Cookie(None),
    # user_id: Optional[str] = Cookie(None)
):
    return {
        "foo": foo,
        # "user_id": user_id
    }
