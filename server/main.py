from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from middlewares.exception_handlers import catch_exception_middleware
from routes.upload_pdfs import router as upload_router
from routes.ask_que import router as ask_router


app = FastAPI(
    title="MY TUTOR API",
    description="API for AI tutor for class notes chatbot"
)


#Cors setup
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = ["*"],
    allow_methods = ["*"],
    allow_headers = ["*"]
)

#middleware expection handler
app.middleware("http")(catch_exception_middleware)
#router

#1. upload pdf
app.include_router(upload_router)
#2. asking query
app.include_router(ask_router)
