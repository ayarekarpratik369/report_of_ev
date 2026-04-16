from fastapi.responses import FileResponse
from fastapi.responses import HTMLResponse
from fastapi import FastAPI

app=FastAPI()




@app.get("/", response_class=HTMLResponse)
def home():
    return open("main.html").read()
@app.get("/report")
def get_report():
    return FileResponse("EV_Fault_Detection_Final_Report.pdf")