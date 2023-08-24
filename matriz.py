import tkinter as tk
import random

class MatrixApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Matrix Selection")
        
        self.matrix = [[0] * 5 for _ in range(10)]
        self.disabled_positions = set()
        self.selected_count = 0
        
        self.create_matrix_buttons()
        
    def create_matrix_buttons(self):
        for row in range(10):
            for col in range(5):
                button = tk.Button(self.root, text=f"{row+1},{col+1}", command=lambda r=row, c=col: self.toggle_selection(r, c))
                button.grid(row=row, column=col, padx=5, pady=5)
                self.matrix[row][col] = button
                
        restart_button = tk.Button(self.root, text="Restart Matrix", command=self.restart_matrix)
        restart_button.grid(row=10, columnspan=5, pady=10)
        
    def toggle_selection(self, row, col):
        if (row, col) not in self.disabled_positions and self.selected_count < 5:
            self.disabled_positions.add((row, col))
            self.selected_count += 1
            self.update_matrix_buttons()
            
    def update_matrix_buttons(self):
        for row in range(10):
            for col in range(5):
                button = self.matrix[row][col]
                if (row, col) in self.disabled_positions:
                    button.config(state="disabled", bg="gray")
                else:
                    button.config(state="normal", bg="SystemButtonFace")
                    
    def restart_matrix(self):
        self.disabled_positions.clear()
        self.selected_count = 0
        self.update_matrix_buttons()
        
    def generate_random_number(self):
        available_positions = [(r, c) for r in range(10) for c in range(5) if (r, c) not in self.disabled_positions]
        if available_positions:
            random_position = random.choice(available_positions)
            self.toggle_selection(random_position[0], random_position[1])

def main():
    root = tk.Tk()
    app = MatrixApp(root)
    
    generate_button = tk.Button(root, text="Generate Random Number", command=app.generate_random_number)
    generate_button.grid(row=11, columnspan=5, pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    main()

