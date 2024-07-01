from fastapi.security import HTTPBearer
from fastapi import Request, HTTPException
from utils.jwt_manager import validate_token

#class JWTBearer(HTTPBearer):
#    async def __call__(self, request: Request):
#        auth = await super().__call__(request)
#        data = validate_token(auth.credentials)
#        if data['email'] != "elianmaineri@gmail.com":
#            raise HTTPException(status_code=403, detail="Credenciales son invalidas")
class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        if request.url.path in ["/login"]:
            return
        if request.url.path in ["/Usuarios"] and request.method == "POST":
            return
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
