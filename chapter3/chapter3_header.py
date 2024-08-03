from fastapi import FastAPI, Header

app = FastAPI()

@app.get("/headers")
async def read_headers(
    user_agent: str | None = Header(None),
    accept: str | None = Header(None),
    content_type: str | None = Header(None),
    accept_language: str | None = Header(None)
    ):

    return {
        "User-Agent": user_agent,
        'Accept': accept,
        'Content-Type': content_type,
        'Accept-Language': accept_language
        }
