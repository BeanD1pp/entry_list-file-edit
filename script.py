with open("entry_list.txt", "r") as file:
    lines = file.readlines()

for i, line in enumerate(lines):
    model = line.startswith('MODEL=')
    line = line.replace('MODEL=', '')
    line = line.split('_')
    position = i + 8

    if not model:
        continue

    if position >= len(lines):
        lines.append("\n" * 8)
        print("added")

    if "traffic" in line:
        if not lines[position].startswith("AI=fixed"):
            lines.insert(i + 8, "AI=fixed\n")
            print(lines[i] + "Added: AI=fixed")
        else:
            print(lines[i] + "No Change: AI=fixed")
    else:
        if not lines[position].startswith("AI=none"):
            lines.insert(i + 8, "AI=none\n")
            print(lines[i] + "Added: AI=none")
        else:
            print(lines[i] + "No Change: AI=none")

with open("entry_list.txt", "w") as file:
    file.writelines(lines)
