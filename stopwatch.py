import tkinter as tk
from tkinter import StringVar

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")
        self.root.geometry("400x300")
        
        # Background color
        self.background_color = "#2E4053"  
        self.root.configure(bg=self.background_color)
        
        self.time_var = StringVar()
        self.time_var.set("00:00:00")
        
        self.running = False
        self.elapsed_time = 0
        
        # Stopwatch Display
        self.time_label = tk.Label(
            root, textvariable=self.time_var, 
            font=("Helvetica", 30, "bold"), 
            bg="white", fg="black", 
            relief="ridge", borderwidth=5
        )
        self.time_label.place(relx=0.5, rely=0.4, anchor="center")  # Center aligned
        
        # Buttons Frame
        button_frame = tk.Frame(root, bg=self.background_color)
        button_frame.place(relx=0.5, rely=0.7, anchor="center")  # Center aligned
        
        self.start_button = tk.Button(
            button_frame, text="Start", command=self.start, 
            width=12, height=2, font=("Arial", 12, "bold"), 
            bg="#2ECC71", fg="white", relief="raised"
        )
        self.start_button.grid(row=0, column=0, padx=10, pady=10)
        
        self.stop_button = tk.Button(
            button_frame, text="Stop", command=self.stop, 
            width=12, height=2, font=("Arial", 12, "bold"), 
            bg="#E74C3C", fg="white", relief="raised"
        )
        self.stop_button.grid(row=0, column=1, padx=10, pady=10)
        
        self.reset_button = tk.Button(
            button_frame, text="Reset", command=self.reset, 
            width=12, height=2, font=("Arial", 12, "bold"), 
            bg="#3498DB", fg="white", relief="raised"
        )
        self.reset_button.grid(row=0, column=2, padx=10, pady=10)
    
    def update_time(self):
        if self.running:
            self.elapsed_time += 1
            minutes, seconds = divmod(self.elapsed_time, 60)
            hours, minutes = divmod(minutes, 60)
            self.time_var.set(f"{hours:02}:{minutes:02}:{seconds:02}")
            self.root.after(1000, self.update_time)
    
    def start(self):
        if not self.running:
            self.running = True
            self.update_time()
    
    def stop(self):
        self.running = False
    
    def reset(self):
        self.running = False
        self.elapsed_time = 0
        self.time_var.set("00:00:00")

if __name__ == "__main__":
    root = tk.Tk() 
    stopwatch = Stopwatch(root)
    root.mainloop()
