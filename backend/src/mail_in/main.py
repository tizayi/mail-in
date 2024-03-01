from typing import List

from fastapi import FastAPI
from .dependencies import StorageTempOptions, SaxMailIn, ColumnOptions

app = FastAPI()

@app.get("/")
def read_root():
    return {"hello": "world"}

@app.get("/hplc_column")
def get_current_hplc_columns() -> List[str]:
    return [member.value for member in ColumnOptions]

@app.get("/storage_temp")
def get_storage_temps() -> List[str]:
    return [member.value for member in StorageTempOptions]

@app.post("/mail_in/submit")
def post_mail_in(input: SaxMailIn) -> SaxMailIn:
    return input