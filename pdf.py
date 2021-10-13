
import fitz
# print(fitz.__doc__)
#https://pymupdf.readthedocs.io/en/latest/faq.html#how-to-split-single-pages

# doc = fitz.open(payslips)     # or fitz.Document(filename)

# Document.page_count	#the number of pages (int)


staffs = {'abiatar.pdf':'Festus.Abiatar@mha.gov.na', 'festus.pdf':'abiatarfestus@outlook.com', 'hanghome.pdf':'Hesekie.Hanghome@mha.gov.na','uugwanga.pdf':'Hileni.Uugwanga@mha.gov.na', 
'iita.pdf':'Laili.Iita@mha.gov.na', 'alugongo.pdf':'Hesekie.Hanghome@mha.gov.na', 'shimuningeni.pdf':'Selma.Shimuningeni@mha.gov.na',
'kashikuka.pdfcls':'Elizabeth.Kashikuka@mha.gov.na', 'nuuyoma.pdf':'Hilkka.Nuuyoma@mha.gov.na', 'iyagaya.pdf':'Bertha.Iyagaya@mha.gov.na',
'shikulo.pdf':'Josephine.Shikulo@mha.gov.na', 'ashipala.pdf':'Teofilia.Ashipala@mha.gov.na', 'aiyambo.pdf':'Uilika.Aiyambo@mha.gov.na',
'shimooshili.pdf':'Letitia.Shimooshili@mha.gov.na', 'kaapanda.pdf':'Emilia.Kaapanda@mha.gov.na', 'amadhila.pdf':'Isak.Amadhila@mha.gov.na',
'cardos.pdf':'Anna.Cardos@mha.gov.na', 'ndundu.pdf':'Stefanus.Ndundu@mha.gov.na', 'kashuupulwa.pdf':'Ndeshihafela.Kashuupulwa@mha.gov.na',
'itembu.pdf':'Petrina.Itembu@mha.gov.na', 'iipinge.pdf':'Josephine.Iipinge@mha.gov.na', 'matheus.pdf':'Sara.Matheus@mha.gov.na'
}

#----SPLIT PAGES----

src = fitz.open(r'C:\Users\Fessy\Desktop\January\payslips.pdf')
split_payslips = fitz.open()  # empty output PDF
print('Splitting pdf...')
for pg in src:  # for each page in input
    r = pg.rect  # input page rectangle
    # d = fitz.Rect(pg.cropbox_position,  # CropBox displacement if not
    #               pg.cropbox_position)  # starting at (0, 0)

    r1 = fitz.Rect(r.tl, r.width*0.43,r.height)  # left rect
    r2 = fitz.Rect(r.width*0.43,0, r.br) # right rect
    rect_list = [r1, r2]  # put them in a list

    for rx in rect_list:  # run thru rect list
        # rx += d  # add the CropBox displacement
        page = split_payslips.new_page(-1,  # new output page with rx dimensions
                           width = rx.width,
                           height = rx.height)
        page.show_pdf_page(
                page.rect,  # fill all new page with the image
                src,  # input document
                pg.number,  # input page number
                clip = rx,  # which part to use of input page
            )

# that's it, save output file
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
    # text = new_doc[0].get_text('text')
    # print(text)
    # print('*'*10)
    for name in staff_names:
        print(staff_names)
        print(name)
        if new_doc[0].search_for(name): #name in text: 
            print(f'Name found: {new_doc[0].search_for(name)}')
            new_doc.save(f'C:\\Users\\Fessy\\Desktop\\January\\{name}.pdf', garbage=3, deflate=True)
            staff_names.remove(name)
            break
        else:
            new_doc.save(f'C:\\Users\\Fessy\\Desktop\\January\\payslip{num}.pdf', garbage=3, deflate=True)
            num +=1
            break
    new_doc.close()

print('Page extraction done!')