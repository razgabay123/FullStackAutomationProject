def attach_playwright_listeners(page):
    page.on("request", lambda request: print(f"[REQ] {request.method} {request.url}"))
    page.on("response", lambda response: print(f"[RES] {response.status} {response.url}"))
    page.on("console", lambda msg: print(f"[CONSOLE] {msg.type}: {msg.text}"))
    page.on("pageerror", lambda error: print(f"[ERROR] {error}"))
