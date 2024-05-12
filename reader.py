from pdf2image import convert_from_path
from os import remove
from pytesseract import image_to_string
images = convert_from_path("2023-PSSD-York-University.pdf", poppler_path='poppler-24.02.0/Library/bin')
for i in range(len(images)):
    images[i].save('page'+str(i)+'.jpg', 'JPEG')
    with open("page"+str(i)+".jpg", "r") as file:
        table = image_to_string("page"+str(i)+".jpg", config="--psm 6")
        # Remove title from each page
        table = table.replace("Record of employees' 2023 salaries and benefits", "").replace("Registre des traitements et avantages verses aux employes en 2023", "")
        table = table.replace("~","").replace("|", "").replace("'","").replace("(","").replace("_","").replace("=","").replace("-","")
        print(table)
    remove("page"+str(i)+".jpg")
