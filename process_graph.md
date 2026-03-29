If I were to build a pipeline or graph for the Photo
  Scrubber project, it would indeed start with the
  Frontend, but it wouldn't simply "end" at the
  database. Instead, it would look like a closed loop
  for the user experience, with a persistent branch into
  the database for metadata and auditing.


  Based on my investigation of your code (main.py,
  scrub.py, and scrub_post.py), here is what that
  pipeline looks like:


  1. The Trigger: Frontend (User Input)
   * Action: The user drops a photo into the dropZone in
     index.html.
   * Technology: Vanilla JS sends a POST request with
     the file to /api/scrub.


  2. The Gateway: Nginx Proxy
   * Action: The Nginx container (gateway) receives the
     request on port 8080 and proxies it to the FastAPI
     service on port 8000.


  3. The Intake: Backend (FastAPI)
   * Action: api/scrub_post.py receives the UploadFile
     object.
   * Logic: It prepares the environment and hands the
     file off to the processing logic.


  4. The Core: Processing (ExifTool)
   * Action: processing/scrub.py saves the raw file to
     the uploads/ directory, then runs the external
     ExifTool command.
   * Transformation: All metadata (EXIF, GPS,
     MakerNotes) is stripped, and a "clean" version is
     created. The raw file is then deleted from the
     disk.


  5. The Audit: Database (PostgreSQL)
   * Action: Once processing is successful, the backend
     calls the stats_record stored procedure in the
     database.
   * Persistence: This is where the "journey" ends for
     the metadata—the database increments the total
     number of photos cleaned and the sum of bytes
     removed.
   * End-point: This is the final resting place for the
     record of the activity.


  6. The Delivery: Backend Response
   * Action: The FastAPI service sends a FileResponse
     containing the cleaned photo blob back to the
     frontend.


  7. The Result: Frontend (User Feedback)
   * Action: The JS in the browser receives the blob,
     creates a download link, and triggers a
     fetchStats() call.
   * Closing the Loop: The frontend pulls the updated
     totals back from the database (via /api/stats) and
     updates the UI to show the new "Photos scrubbed"
     count.

  ---


  Summary Graph
  So, to answer your question: It starts at the
  Frontend, goes through the Disk/Processing, branches
  into the Database for a permanent record, and finally
  returns to the Frontend for the user's download.


  Simplified Flow:
  Frontend (Start) ➔ Backend ➔ Processing (ExifTool) ➔
  Local Disk ➔ Database (Audit) ➔ Backend ➔ Frontend
  (End/Download)


