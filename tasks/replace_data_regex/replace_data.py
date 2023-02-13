import re

def findingvalue(fieldName):

    fieldDatas = {
        "^\d{3}W.*": "Branch Image Capture",
        "^\d{3}T.*": "Teller Machine",
        "^\d{3}B.*": "Back office",
        "^DON'S.*": "Back office",
        "^451.*": "Back office",
        "^420EIGAPPD": "Back office",
        "^\d{3}P.*": "Platform",
        "^\d{3}A.*": "Administrative",
        "^\d{3}L.*": "Lab/Training",
        "^[A-Z]{4}\S.*": "EIG Workstation",
        "^DUX.*": "EIG Workstation",
        "^999.*": "SCCM Deployment"
    }
    
    for regexPattern in fieldDatas:
        if re.match(regexPattern, fieldName):
            value = fieldDatas[regexPattern]
            return(value)

if __name__ == "__main__":

    with open('sample.txt', 'r') as s:
      datas = s.read().split("\n")
 
    with open('FinalOutput.txt', 'w') as output:
        output.write("Workstation Type\t Field Value\n")

    for data in datas:
        fieldValue = findingvalue(data)
        with open('FinalOutput.txt', 'a') as output:
            output.write(str(data)+"\t"+str(fieldValue)+"\n")
