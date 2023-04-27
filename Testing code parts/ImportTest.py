file = open('data.txt', encoding="utf8")
lines = file.readlines()

for index, line in enumerate(lines):
    if index!=1:
        if "💩" in line:
            print(line.strip())  
    
    
file.close()