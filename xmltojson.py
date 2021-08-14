import xmltodict
import json

def xml_f1():
    with open("xml_file1.xml") as xml_file:
        dictionary = xmltodict.parse(xml_file.read())

    json_data = json.dumps(dictionary)

    with open("json_file.json", "x") as json_file:
        json_file.write(json_data)

xml_f1()


def xml_f2():
    with open("xml_file2.xml") as xml_file2:
        dictionary2 = xmltodict.parse(xml_file2.read())

    json_data2 = json.dumps(dictionary2, ensure_ascii= False)
    with open("json_filedva.json", "x") as json_file2:
        json_file2.write(json_data2)

xml_f2()

def xml_f3():
    with open("xml_file3.xml") as xml_file3:
        dictionary3 = xmltodict.parse(xml_file3.read())

    json_data3 = json.dumps(dictionary3)
    with open("json_filetri.json", "x") as json_file3:
        json_file3.write(json_data3)

xml_f3()