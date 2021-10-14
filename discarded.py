
import json
import fitz
import environ

# print(fitz.__doc__)
#https://pymupdf.readthedocs.io/en/latest/faq.html#how-to-split-single-pages

env = environ.Env()
# reading .env file
environ.Env.read_env()

staffs_str = env.str("STAFFS")
# print(staffs_str)
print(type(staffs_str))
# staffs = json.loads(staffs_str)
staffs = {"shingenge.pdf":"Enos.Shingenge@mha.gov.na", "abiatar.pdf":"Festus.Abiatar@mha.gov.na", "hanghome.pdf":"Hesekie.Hanghome@mha.gov.na","uugwanga.pdf":"Hileni.Uugwanga@mha.gov.na", "iita.pdf":"Laili.Iita@mha.gov.na", "alugongo.pdf":"Hesekie.Hanghome@mha.gov.na", "shimuningeni.pdf":"Selma.Shimuningeni@mha.gov.na",  "kashikuka.pdf":"Elizabeth.Kashikuka@mha.gov.na", "nuuyoma.pdf":"Hilkka.Nuuyoma@mha.gov.na", "iyagaya.pdf":"Bertha.Iyagaya@mha.gov.na", "shikulo.pdf":"Josephine.Shikulo@mha.gov.na", "ashipala.pdf":"Teofilia.Ashipala@mha.gov.na", "aiyambo.pdf":"Uilika.Aiyambo@mha.gov.na", "shimooshili.pdf":"Letitia.Shimooshili@mha.gov.na", "kaapanda.pdf":"Emilia.Kaapanda@mha.gov.na", "amadhila.pdf":"Isak.Amadhila@mha.gov.na", "cardos.pdf":"Anna.Cardos@mha.gov.na", "ndundu.pdf":"Stefanus.Ndundu@mha.gov.na", "kashuupulwa.pdf":"Ndeshihafela.Kashuupulwa@mha.gov.na", "itembu.pdf":"Petrina.Itembu@mha.gov.na", "iipinge.pdf":"Josephine.Iipinge@mha.gov.na", "matheus.pdf":"Sara.Matheus@mha.gov.na"}
# print(staffs)
# print(type(staffs))

#----SPLIT PAGES----

src = fitz.open(r'C:\Users\Fessy\Desktop\January\payslips.pdf')
split_payslips = fitz.open()  # empty output PDF
print('Splitting pdf...')
for pg in src:  # for each page in input
    r = pg.rect  # input page rectangle

    r1 = fitz.Rect(r.tl, r.width*0.43,r.height)  # left rect
    r2 = fitz.Rect(r.width*0.43,0, r.br) # right rect
    rect_list = [r1, r2]  # put them in a list

    for rx in rect_list:  # run thru rect list
        page = split_payslips.new_page(-1,  # new output page with rx dimensions
                                        width = rx.width,
                                        height = rx.height)
        page.show_pdf_page(page.rect,  # fill all new page with the image
                            src,  # input document
                            pg.number,  # input page number
                            clip = rx,  # which part to use of input page
                            )


split_payslips.save('C:\\Users\\Fessy\\Desktop\\January\\split_payslips.pdf',
                    garbage=3,  # eliminate duplicate objects
                    deflate=True  # compress stuff where possible
                    )

print('Splitting done!')

#----EXTRACT PAGES----
print('Extracting pages...')
num = 1
staff_names = [name[:len(name)-4] for name in staffs.keys()]
all_payslips = fitz.open('C:\\Users\\Fessy\\Desktop\\January\\split_payslips.pdf')
for pg in all_payslips:
    new_doc = fitz.open()                 # new empty PDF
    new_doc.insert_pdf(all_payslips, from_page=pg.number, to_page=pg.number)  # current page in iteration
    # text = str(new_doc[0].get_text("text"))
    # print(text)
    # print('*'*50)
    text = new_doc[0].get_textpage()
    print(text.extractText())
    print('*'*50)
    for name in staff_names:
        if new_doc[0].search_for(name): #name in text
        # if name in text:
            # print(f'{name.capitalize()} found at: {new_doc[0].search_for(name)}')
            new_doc.save(f'C:\\Users\\Fessy\\Desktop\\January\\{name}.pdf', garbage=3, deflate=True)
            staff_names.remove(name)
            new_doc.close()
            break
    try:    
        new_doc.save(f'C:\\Users\\Fessy\\Desktop\\January\\payslip{num}.pdf', garbage=3, deflate=True)
        num +=1
        new_doc.close()
    except ValueError:
        pass

print('Page extraction done!')