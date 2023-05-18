import tkinter as tk

def create_matrix():
    rows = int(entry_rows.get())
    columns = int(entry_columns.get())
    
    for i in range(rows):
        for j in range(columns):
            entry = tk.Entry(root, width=5)
            entry.insert(0, "0")  # Set default value to 0
            entry.grid(row=i+1, column=j)
            matrix_entries.append(entry)
    rref_button.grid(row=rows+1, column=0, columnspan=columns, pady=10)  # Position the "RREF" button under the input boxes
    root.update()  # Update the window to fit the input boxes
    root.geometry(f"{root.winfo_width()}x{root.winfo_height()}")  # Resize the window to fit the input boxes
def perform_rref():
    rows = int(entry_rows.get())
    columns = int(entry_columns.get())
    matrix = []
    for i in range(rows):
        row = []
        for j in range(columns):
            entry = matrix_entries[i * columns + j]
            value = float(entry.get())
            row.append(value)
        matrix.append(row)

    print(matrix)
    h = 0
    k = 0
    operations = ''
    count = 1
    while h < rows and k < columns:
        i_max = h
        while i_max < rows and matrix[i_max][k] == 0:
            i_max += 1

        if i_max == rows:
            k += 1
        else:
            matrix[h], matrix[i_max] = matrix[i_max], matrix[h]

            pivot = matrix[h][k]
            operations += f'{count}. Pivot {pivot:.3f} at A[{h},{j}]\n'
            count+=1
            for j in range(columns):
                matrix[h][j] /= pivot
            operations += f'{count}. Row {h} / {pivot}\n'
            count+=1
            for i in range(rows):
                if i != h:
                    f = matrix[i][k]
                    matrix[i][k] = 0
                    for j in range(k + 1, columns):
                        matrix[i][j] -= matrix[h][j] * f
                    operations += f'{count}. Row {i} - Row {h} * {f:.3f}\n'
                    count+=1
                

            h += 1
            k += 1
    print(operations)
    
    label_ops = tk.Label(root, text=operations,justify="left")
    label_ops.grid(row=rows+2, column=1, sticky="w")

    ref_text = ''
    for i in matrix:
        for j in i:
            ref_text+= f' {j:.2f} '
        ref_text+='\n'

    label_matrix = tk.Label(root, text=ref_text,justify="left")
    label_matrix.grid(row=rows+rows+2, column=1, sticky="w")

    root.update()
    new_width = root.winfo_reqwidth()
    new_height = root.winfo_reqheight()
    root.geometry(f"{new_width}x{new_height}") 
        

    print(matrix)


root = tk.Tk()
root.title("Matrix Input")

matrix_entries = []

label_rows = tk.Label(root, text="Number of rows:")
label_rows.grid(row=0, column=0, sticky="e")

entry_rows = tk.Entry(root)
entry_rows.grid(row=0, column=1)
entry_rows.insert(3,'3')

label_columns = tk.Label(root, text="Number of columns:")
label_columns.grid(row=0, column=2, sticky="e")

entry_columns = tk.Entry(root)
entry_columns.grid(row=0, column=3)
entry_columns.insert(3,'3')

create_button = tk.Button(root, text="Create Matrix", command=create_matrix)
create_button.grid(row=0, column=4)

rref_button = tk.Button(root, text="RREF", command=perform_rref)
# Hide the "RREF" button initially
rref_button.grid(row=0, column=0, columnspan=4, sticky="we")
rref_button.grid_remove()

root.mainloop()
