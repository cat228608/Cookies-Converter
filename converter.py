import json
import argparse

def converter(files):
    with open(files, 'r') as f:
        content = f.readlines()

    content = [x.strip() for x in content if x.startswith('#')==False and x.strip()!='']

    cookies = []
    for line in content:
        parts = line.split('\t')
        cookie = {"domain": parts[0], "path": parts[2], "name": parts[5], "value": parts[6]}
        cookies.append(cookie)
    return cookies

parser = argparse.ArgumentParser(description='Соси бибу') #Аня я тебя люблю!
parser.add_argument("-f")
args = parser.parse_args()
f = args.f
print(f)
if f == None:
    file = input("Укажите путь до файла с куки: ")
    result = converter(file)
    print(json.dumps(result))
else:
    result = converter(f)
    print(json.dumps(result))