import json
import urllib.request

fd = open('specializations.json','r')

data = json.loads(fd.read())

print(list(data["objectID"].keys())[0])

for course_id in data["objectID"]:
    
    try:
    url = f"https://www.coursera.org/api/productPrices.v3/VerifiedCertificate~{course_id}~GBP~GB"

    page_data = urllib.request.urlopen(url)

    data = page_data.read().decode()

    jsdata = json.loads(data)

    print(jsdata['elements'][0]['amount'])

    