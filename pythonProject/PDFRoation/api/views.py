from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from PyPDF2 import PdfFileReader,PdfFileWriter

@api_view(["POST"])
def api_home(request , *args ,**kwargs):
    data = request.data
    file_path = data["file_path"]
    angle_rotation = data["angle_of_rotation"]
    page_number = data["page_number"]
    '''
    {
    "file_path" : "C:/Users/hacke/Downloads/crypto 1.pdf",
    "angle_of_rotation":90,
    "page_number":2
    }
    '''
    output_filePath =  helper(file_path,angle_rotation,page_number-1)
    return Response(
        {
            "msg": "succes",
            "file_Path":output_filePath
        }
    )


def helper(file_path,ang,page_num):
    target_file = file_path
    output_filePath = file_path[0:file_path.rfind('/')+1]+'output_rotated.pdf'
    output_file = open(output_filePath, 'wb')
    print(output_file)
    pdf = PdfFileReader(target_file)
    writer = PdfFileWriter()

    num_page = pdf.getNumPages()
    # print(num_page,"slkjslkj",page_num)
    angle = ang
    rotated_page = page_num

    for i in range(num_page):
        page = pdf.getPage(i)
        if rotated_page == i:
            page.rotateClockwise(angle)
        writer.addPage(page)

    writer.write(output_file)

    output_file.close()
    return output_filePath
