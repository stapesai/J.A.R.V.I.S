# STEP 1 - Open the CSV file and read the data into a list of lists
def data_extract(file_name):
    with open(file_name, 'r') as f:
        data = f.readlines()
    return data


def main():
    data = data_extract('csv2vcf.csv')
    for i in range(len(data)):
        if i == 0:
            continue
        else:
            entry = data[i].split(',')
            student_name = 'N:;' + entry[0] + '-' + entry[1] + '-' + entry[2] + '/' + entry[3]
            student_contact = 'TEL;TYPE=HOME:' + entry[4].strip()
            with open('output.vcf', 'a') as f:
                f.write('BEGIN:VCARD\nVERSION:3.0\n')
                f.write(student_name + '\n')
                f.write(student_contact + '\n')
                f.write('END:VCARD' + '\n \n')


main()
