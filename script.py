with open("entry_list.txt", "r") as file:
    lines = file.readlines()

total_changes = 0
change_none = 0
change_fixed = 0

ignores = 0
total_none = 0
total_fixed = 0

for i, line in enumerate(lines):
    model = line.startswith('MODEL=')
    if not model:
        continue

    line = line.replace('MODEL=', '').split('_')
    distance = i + 8

    if distance >= len(lines):
        lines.append("\n" * (distance - len(lines) + 1))
        print("Newline added")

    if "traffic" in line:
        if not lines[distance].startswith("AI=fixed"):
            total_changes += 1
            change_fixed += 1
            lines.insert(distance, "AI=fixed\n")
            print(lines[i] + "Added: AI=fixed")
        else:
            ignores += 1
            print(lines[i] + "No Change: AI=fixed")
        total_fixed += 1
    else:
        if not lines[distance].startswith("AI=none"):
            total_changes += 1
            change_none += 1
            lines.insert(distance, "AI=none\n")
            print(lines[i] + "Added: AI=none")
        else:
            ignores += 1
            print(lines[i] + "No Change: AI=none")
        total_none += 1

with open("entry_list.txt", "w") as file:
    file.writelines(lines)

print("\nTotal Changes:", total_changes)
print("\tFixed:", change_fixed)
print("\tNone:", change_none)
print("Total ignores:", ignores)
print("\tTotal Fixed:", total_fixed)
print("\tTotal None:", total_none)
