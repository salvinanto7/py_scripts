import csv
with open('C:\\Users\Salvinanto7\Downloads\contact.csv') as f:
    reader = csv.reader(f)
    with open('C:\\Users\Salvinanto7\Downloads\contact_output.csv', 'w') as g:
        writer = csv.writer(g)
        for row in reader:
            new_row = [' '.join([row[0], row[1]])] + row[2:]
            writer.writerow(new_row)