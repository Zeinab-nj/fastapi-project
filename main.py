from fastapi import FastAPI
import logging
import logging.config


logging.config.fileConfig("logging.conf", disable_existing_loggers=False)


app = FastAPI()


@app.get("/")
async def read_root():
    try:
        raise Exception("simulated debug error ocurred!")
    except Exception as e:
        logging.debug(f"An exception occuresd: {e}")
        logging.debug("Exception traceback:", exc_info=True)
    return {"message": "Hello, world"}
