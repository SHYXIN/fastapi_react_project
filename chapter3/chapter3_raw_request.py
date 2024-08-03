from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/cars")
async def raw_request(request: Request):

    # 使用一个字典来存储属性值
    request_info = {
        "app": request.app,
        # "auth": request.auth,  # AssertionError: AuthenticationMiddleware must be installed to access request.auth
        "base_url": request.base_url,
        "body": await request.body(),
        "client": request.client,
        "cookies": request.cookies,
        # "form": await request.form(), # AssertionError: The `python-multipart` library must be installed to use form parsing.
        "headers": request.headers.items(),
        "is_disconnected": await request.is_disconnected(),
        # "json": await request.json(),  # JSONDecodeError("Expecting value", s, err.value) from None
        "method": request.method,
        "path_params": request.path_params,
        "query_params": request.query_params.items(),
        "receive": request.receive,
        "scope": request.scope,
        "send_push_promise": request.send_push_promise,
        # "session": request.session, # AssertionError: SessionMiddleware must be installed to access request.session
        "state": request.state._state,
        "stream": request.stream,
        "url": request.url,
        "url_for": request.url_for,
        # "user": request.user, # AssertionError: AuthenticationMiddleware must be installed to access request.user
        "values": request.values()
    }

    # 打印每个属性和值
    for key, value in request_info.items():
        print(f"{key}: {value}")

    return {
        "message": request.base_url,
        "all": dir(request),
    }
