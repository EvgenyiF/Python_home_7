import csv
def writer(text, file):
    with open(file,'a+', newline="",encoding="utf-8") as f:
        file_writer = csv.writer(f, delimiter = ";", lineterminator="\r")
        file_writer.writerow (text)