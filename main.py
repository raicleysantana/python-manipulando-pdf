import os
from PyPDF2 import PdfFileMerger

if __name__ == '__main__':
    input_dir = r"docs"
    x = [a for a in os.listdir(input_dir) if a.endswith(".pdf")]
    merger = PdfFileMerger()

    for pdf in x:
        merger.append(open("docs/{}".format(pdf), 'rb'))

    with open("result.pdf", "wb") as fout:
        merger.write(fout)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
