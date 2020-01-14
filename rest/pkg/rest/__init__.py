from fastapi import FastAPI
from pkg.config import CONFIG
from pkg.constants.error_codes import ERROR_UNHANDLED_EXCEPTION, ERROR_CUSTOM_EXCEPTION
from pkg.rest.routers.root import router as root_router
from pkg.rest.routers.v1 import router as v1_router
from pkg.utils.errors import CustomException, response_error
from pkg.utils.logger import DEFAULT_LOGGER, REST_LOGGER
from starlette.exceptions import HTTPException
from starlette.requests import Request

app = FastAPI()
app.include_router(root_router)
app.include_router(v1_router, prefix='/v1')


@app.on_event("startup")
async def startup_event():
    DEFAULT_LOGGER.info(f'REST server started on {CONFIG["rest"]["listen_host"]}:{CONFIG["rest"]["listen_port"]}\n')


@app.exception_handler(Exception)
async def unhandled_exceptions_handler(request: Request, exc: Exception):
    return response_error(ERROR_UNHANDLED_EXCEPTION, str(exc), log_error=False)


@app.exception_handler(HTTPException)
async def http_exceptions_handler(request: Request, exc: HTTPException):
    return response_error(exc.status_code, str(exc.detail), exc.status_code, log_stacktrace=False)


@app.exception_handler(CustomException)
async def http_exceptions_handler(request: Request, exc: CustomException):
    return response_error(ERROR_CUSTOM_EXCEPTION, str(exc.detail), log_error=False)
