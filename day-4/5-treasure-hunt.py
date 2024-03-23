row1 = ["🀫", "🀫", "🀫"]
row2 = ["🀫", "🀫", "🀫"]
row3 = ["🀫", "🀫", "🀫"]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("where do you want to put the treasure/")
print(position[0])

col = int(position[0])
row = int(position[1])

col = int(col)
row = int(row)

selectedRow = map[row]
selectedRow[col] = "X"


map[col][row] = "X"
print(f"{row1}\n{row2}\n{row3}")
