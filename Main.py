import tkinter as tk
import time

class GrassSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Touching Grass Simulator")
        self.root.geometry("1000x700")
        self.root.configure(background="white")

        self.touching = False
        self.start_time = 0

        self.label = tk.Label(root, text="You are not touching grass", font=("Arial", 24, "bold"), bg=self.root["bg"])
        self.label.pack(pady=10)

        self.grass_img = tk.PhotoImage(file="grass.png")

        self.grass = tk.Label(root, image=self.grass_img)
        self.grass.pack(pady=20)

        self.grass.bind("<Enter>", self.start_touching)
        self.grass.bind("<Leave>", self.stop_touching)

        self.update_timer()

    def start_touching(self, event):
        self.grass.config(cursor="hand2")
        self.touching = True
        self.start_time = time.time()

    def stop_touching(self, event):
        self.grass.config(cursor="")
        self.touching = False
        self.root.configure(background="white")
        self.label.config(text="You stopped touching grass", font=("Arial", 24, "bold"), bg=self.root["bg"])

    def update_timer(self):
        current_time = 0
        if self.touching:
            current_time = time.time() - self.start_time
            self.label.config(text=f"You are touching grass since: {current_time:.1f} s", font=("Arial", 24, "bold"), bg=self.root["bg"])
        if current_time > 60:
            self.root.configure(background="gold")
        elif current_time > 30:
            self.root.configure(background="silver")
        elif current_time > 15:
            self.root.configure(background="#8B4513")

        self.root.after(100, self.update_timer)

root = tk.Tk()
app = GrassSimulator(root)
root.mainloop()
