from fastapi.responses import FileResponse
from fastapi.responses import HTMLResponse
from fastapi import FastAPI

app=FastAPI()




@app.get("/", response_class=HTMLResponse)
def home():
    return open("index.html").read()
@app.get("/report")
def get_report():
    return FileResponse("report.docx")