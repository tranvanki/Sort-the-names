import tkinter as tk
from tkinter import ttk 
# define sort function
def compare_by_last_first_name(a, b):
    last_a, first_a = a.split()[-1], a.split()[0]
    last_b, first_b = b.split()[-1], b.split()[0]
    if last_a != last_b:
        return last_a > last_b
    else:
        first_a > first_b

def count_vowels(name):
    vowels = 'aeiou'
    return sum(char in vowels for char in name.lower())

def compare_by_vowel_count(a, b):
    return count_vowels(a) > count_vowels(b)

def my_sort(items, compare):
    items_copy = items[:]
    for i in range(len(items_copy) - 1):
        for j in range(i + 1, len(items_copy)):
            if compare(items_copy[i], items_copy[j]):
                items_copy[i], items_copy[j] = items_copy[j], items_copy[i]
    return items_copy

# Define the GUI application
class SortNamesApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sort Names")
        
        self.label = tk.Label(self, text="Enter names (comma-separated):")
        self.label.pack(pady=5)
        
        self.names_entry = tk.Entry(self, width=50)
        self.names_entry.pack(pady=5)
        self.names_entry.insert(0, 'Nguyen Trung Kien, Nguyen Van Binh, Nguyen Van An, Le Trung Binh, Le Duc Hoa, Hoang Mai, Ho Thu Hoai, Nguyen Thi Mai, Do Thi Lan')
        
        self.sort_last_first_btn = tk.Button(self, text="Sort by Last Name then First Name", command=self.sort_last_first)
        self.sort_last_first_btn.pack(pady=5)
        
        self.sort_vowel_count_btn = tk.Button(self, text="Sort by Vowel Count", command=self.sort_vowel_count)
        self.sort_vowel_count_btn.pack(pady=5)
        
        self.result_label = tk.Label(self, text="Sorted names will appear here")
        self.result_label.pack(pady=5)
    
    def sort_last_first(self):
        names = self.names_entry.get().split(',')
        names = [name.strip() for name in names]
        sorted_names = my_sort(names, lambda a, b: compare_by_last_first_name(a, b))
        self.result_label.config(text="Sorted by Last Name then First Name:\n" + "\n".join(sorted_names))
    
    def sort_vowel_count(self):
        names = self.names_entry.get().split(',')
        names = [name.strip() for name in names]
        sorted_names = my_sort(names, lambda a, b: compare_by_vowel_count(a, b))
        self.result_label.config(text="Sorted by Vowel Count:\n" + "\n".join(sorted_names))

# Run the application
if __name__ == "__main__":
    app = SortNamesApp()
    app.mainloop()