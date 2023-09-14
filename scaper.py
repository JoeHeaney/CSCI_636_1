import requests, bs4
url = "https://directory.seas.upenn.edu/"
page = requests.get(url)

soup = bs4.BeautifulSoup(page.content, 'html.parser')

staffNames = soup.findAll('div', attrs ={'class':'StaffListName'})
staffDepartments = soup.findAll('div', attrs ={'class':'StaffListTitles'})

file1 = open('names.txt','w')
file2 = open('bios.txt','w')
file1.writelines(['NAMES OF PROFESSORS'])
file2.writelines(['BIOS OF PROFESSORS'])
for staffNames, staffDepartments in zip(staffNames, staffDepartments):
    file1.writelines(staffNames.text)
    file2.writelines(staffDepartments.text)
file1.close()
file2.close()

