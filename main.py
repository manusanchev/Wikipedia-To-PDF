import requests


class CheckExists:
    def __init__(self):
        self.url = ""

    @staticmethod
    def checkPages(alumno):
        response = requests.get("http://alumno" + alumno + ".departamento-informatica-jose-cabrera.es/obras")
        validate = response.ok
        if validate:
            print('alumno' + alumno + ' is ok')
        else:
            anotherOportunity = requests.get("http://alumno" + alumno + ".departamento-informatica-jose-cabrera.es/Obras")
            validate = anotherOportunity.ok
            if(validate):
                print('alumno' + alumno + ' is ok')
            else:
                print('alumno' + alumno + ' is not ok')


check = CheckExists()
for i in range(1, 17):
    check.checkPages(str(i))
