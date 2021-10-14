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
staffs = json.loads(staffs_str)

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