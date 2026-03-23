@app.post("/api/scrub")
async def scrub_image(file: UploadFile = File(...)):
