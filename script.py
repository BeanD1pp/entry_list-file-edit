with open("entry_list.txt", "r") as file:
    lines = file.readlines()

for i, line in enumerate(lines):
    model = line.startswith('MODEL=')
    line = line.replace('MODEL=', '')
    line = line.split('_')
    
    if model and "traffic" in line:
        lines.insert(i + 8, "AI=fixed\n")
    elif model:
        lines.insert(i + 8, "AI=none\n")

with open("entry_list.txt", "w") as file:
    file.writelines(lines)
