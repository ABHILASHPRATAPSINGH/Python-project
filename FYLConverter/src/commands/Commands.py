import pathlib
from typing import List

import PyPDF2 as pdf
from PyPDF2.utils import PdfReadError
from pdf2image import pdf2image


def protectPdf(pdfFilePath:str,password:str):
    fileBaseName = pdfFilePath.replace(".pdf", "")
    try:
        pdfReader = pdf.PdfFileReader(pdfFilePath)
        pdfPagesCount = pdfReader.getNumPages()
        pdfWriter = pdf.PdfFileWriter()
        page_suffix = "protected"

        for i in range(pdfPagesCount):
            pageI = pdfReader.getPage(i)
            pdfWriter.addPage(pageI)
        pdfWriter.encrypt(password)
        oFilePath="{}_{}.pdf".format(fileBaseName, page_suffix)
        with open(oFilePath, "wb") as f:  # 1 is added as python starts indexing from 0
            pdfWriter.write(f)
    except PdfReadError as e:
        raise PdfReadError("File :'{}'\n pdf is not readable may be currupted or protected".format(pdfFilePath))
    return oFilePath

def extractPagesAsSinglePdf(pdfFilePath:str,requiredPages:List[int]):
    # pdfFilePath = r"C:\Users\DELL\Desktop\BasicComputerCourse\Python\PythonProjects\so_survey_2020.pdf"
    fileBaseName = pdfFilePath.replace(".pdf", "")
    pdfReader = pdf.PdfFileReader(pdfFilePath)
    # pdfPages = pdfReader.getNumPages()
    pdfWriter = pdf.PdfFileWriter()
    numberOfRequiredPages = requiredPages
    page_suffix = "".join([str(i) for i in numberOfRequiredPages])
    for i in numberOfRequiredPages:
        pageI = pdfReader.getPage(i - 1)
        pdfWriter.addPage(pageI)
    oFilePath="{}_{}.pdf".format(fileBaseName, page_suffix)
    with open(oFilePath, "wb") as f:  # 1 is added as python starts indexing from 0
        pdfWriter.write(f)
    return oFilePath

def pdf2Pngs(pdfFileName:str,requiredPages:List[int])->List[str]:
    oPngs=[]
    imgs=pdf2image.convert_from_path(pdfFileName)
    iPath=pathlib.Path(pdfFileName)
    oName=iPath.name[:iPath.name.find(iPath.suffix)]
    for i in requiredPages:
        ofName="{}_{}.png".format(oName,i)
        ofName=iPath.with_name(ofName)
        imgs[i-1].save(ofName)
        oPngs.append(str(ofName))
    return oPngs


def extractPagesAsIndPdf(pdfFilePath,requiredPages):
    resultedPdfFiles=[]
    for page in requiredPages:
        page2List=[page]
        oPdfFile=extractPagesAsSinglePdf(pdfFilePath,page2List)
        resultedPdfFiles.append(oPdfFile)
    return resultedPdfFiles

def getPdfTotalPages(pdfFilePath:str)->int:
    pdfReader = pdf.PdfFileReader(pdfFilePath)
    try:
        pdfPagesCount = pdfReader.getNumPages()
    except BaseException as e:
        raise ValueError("Pdf File is not readable, may be currupted or password protected.")
    return pdfPagesCount

def getPageList(pageString):
    # pages="1-5;5;6;17-19"
    pages=pageString
    requiredPageList=[]
    pages=pages.split(";")
    try:
        for p in pages:
            if p.find("-")>=0:
                start=int(p[:p.find("-")])
                end=int(p[p.find("-")+1:])+1
                l=list(range(start,end))
                requiredPageList.extend(l)
            else:
                requiredPageList.append(int(p))
    except ValueError as v:
        raise ValueError("Pages not provided in correct format")
    sortedUniquePagesList=list(set(requiredPageList))
    sortedUniquePagesList.sort()
    return sortedUniquePagesList


if __name__ == '__main__':
    print(getPageList())
