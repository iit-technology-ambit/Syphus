## Purpose

This folder contains scripts that can be used to add items in the backend in a simpler manner.

### Present Scripts

#### Upload Newsletter

The process to upload newsletter is simple.

- Go to sendgrid control panel -> templates -> dynamic -> choose to edit latest template -> go to build -> click on advanced -> export to HTML.
- Download the html file and put it in the same folder as the `upload_newsletter.py` replacing current `newsletter.html` file.
- Set environment variables for logging into the API and activate pipenv.
- Run the script and carefully file all the details.

Voila! The newsletter is added :D