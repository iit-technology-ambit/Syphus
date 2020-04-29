### Adding an issue to the Database using swagger
(*Before uploading files in the CDN see the naming convetion please already uploaded files, it looks like `apr20` for april 2020*)

**NOTE**: If you are following the process correctly, but it gave some error like internal server error or failed to add. Just try to execute the request again
1. Add the image(Cover pic of the magazine) in `ambitcdn/cover` folder in Digital Ocean
2. Add the pdf in ambitcdn/issue folder
3. Go to https://api.iit-techambit.in/. Swagger will be appeared
4. Login with Super user credentials
5. Go to endpoint `POST /image/addLink`
6. Add the CDN image link of the issue through this endpoint through swagger.
7. An ID will be returned. Copy it to the clipboard as an integer(exclude the quote marks while copying)
8. In swagger only, go to the endpoint `POST /issues/add`
 The post request associated data is in the format
 ```
{
  "coverId": 0,
  "month": "string",
  "year": "string",
  "link": "string",
  "description": "string"
}
```
9. Use the ID copied in the step 7 as coverId value
10. month value is 3 letter of that month like January will be `jan`, february will be `feb`, December will be `dec`
11. year is the full year 2020, 2021 etc
12. Link the CDN link of the PDF
13. Add a suitable description. Preferably in this format `IIT Tech Ambit MONTH YEAR ISSUE`
14. You should get back the message `Issue added Successfully` after the POST request is executed

**NOTE**:If you make a mistake anywhere like adding a wrong thing in Database, please contact Mukul Mehta or Shivam Kumar Jha.
