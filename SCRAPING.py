# scraping kariyer.net
# getting salary data for bilgisayar muhendisi, veri bilimci, yazilim muhendisi, and mobil yazilim muhendisi and the most hired fields in turkey
# storing the data in csv file

from bs4 import BeautifulSoup
import requests
import csv

def scraping():
    file = open('files/jobs_salaries.csv', 'w', newline="")
    writer = csv.writer(file)
    writer.writerow(["is", "ortalama maas", "en yuksek maas", "en dusuk maas"])

    result = requests.get("https://www.kariyer.net/pozisyonlar").content
    soup = BeautifulSoup(result, "lxml")
    jobs = soup.find_all("a")


    for job in jobs:
        row = []
        job_name = job.text
        if job_name == "Bilgisayar Mühendisi" or job_name == "Veri Bilimci" or job_name == "Yazılım Mühendisi" or job_name == "Mobil Yazılım Mühendisi":
            row += [job_name]
            link = job["href"]
            result1 = requests.get("https://www.kariyer.net" + link).content
            soup1 = BeautifulSoup(result1, "lxml")
            ortalama_salary = soup1.find("div", class_ = "pg-salary-box-value").text
            row += [ortalama_salary]
            a = soup1.find("div", class_ = "pg-salary-box double")
            b = a.find("div", class_ = "left")
            c = a.find("div", class_ = "right")
            en_yuksek = c.find("div", class_ = "pg-salary-box-value").text
            row += [en_yuksek]
            en_dusuk = b.find("div", class_ = "pg-salary-box-value").text
            row += [en_dusuk]
        
            file1 = open(f'files/{job_name}_most_hired_fields.csv', 'w', newline="")
            writer1 = csv.writer(file1)
            writer1.writerow(["field", "ortalama"])
            fields = []
            averages = []
            bolumler = soup1.find_all("div", class_= "pg-progress-row")
            for bolum in bolumler:
                bolum = bolum.text.strip().split("\n")
                fields += [bolum[0]]
                averages += [bolum[1]]
            for i in range(5):
                fields.pop(-1)
                averages.pop(-1)
            
            for i in range(len(fields)):
                row1 = []
                row1+= [fields[i], averages[i]]
                writer1.writerow(row1)
            writer.writerow(row)

    file.close()
