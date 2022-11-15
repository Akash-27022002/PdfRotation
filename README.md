# PdfRotation
This is python django project which have an on rest api 

Install the project and enter the directory which contains manage.py file

**install required files such as django , djangorestframework , PyPDF2... **

Run command *python manage.py runserver*

Then hit the localhost url /api

#Then give the input as

{
 "file_path" : "C:/Users/hacke/Downloads/Crypto Ass1.pdf",
    "angle_of_rotation":90,
    "page_number":2
}


then post the request after that output_rotated.pdf will be downloaded in same directory from where the input is given.
