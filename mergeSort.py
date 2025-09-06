import tkinter as tk
from tkinter import ttk, messagebox
import random

class MergeSortGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Interactive Merge & Sort Visualization")
        self.root.geometry("800x600")
        self.root.configure(bg='#1a1a1a')  # Dark background
        
        # Initial arrays
        self.array_a = [3, 7, 11, 15, 20]
        self.array_b = [4, 8, 12, 16, 25]
        self.merged_array = []
        self.is_merged = False
        
        # Create the GUI
        self.create_widgets()
        self.update_display()
    
    def create_widgets(self):
        # Title
        title_label = tk.Label(self.root, text="Interactive Merge & Sort Visualization", 
                              font=('Arial', 18, 'bold'), bg='#1a1a1a', fg='#00ff88')
        title_label.pack(pady=20)
        
        # Main frame
        main_frame = tk.Frame(self.root, bg='#1a1a1a')
        main_frame.pack(expand=True, fill='both', padx=20, pady=10)
        
        # Arrays display frame
        arrays_frame = tk.Frame(main_frame, bg='#1a1a1a')
        arrays_frame.pack(pady=20)
        
        # Array A display
        self.array_a_frame = tk.LabelFrame(arrays_frame, text="Array A", 
                                          font=('Arial', 12, 'bold'), bg='#2c2c2c', 
                                          fg='#00ccff', padx=10, pady=10)
        self.array_a_frame.grid(row=0, column=0, padx=20, pady=10)
        
        # Array B display
        self.array_b_frame = tk.LabelFrame(arrays_frame, text="Array B", 
                                          font=('Arial', 12, 'bold'), bg='#2c2c2c', 
                                          fg='#ff6b35', padx=10, pady=10)
        self.array_b_frame.grid(row=0, column=1, padx=20, pady=10)
        
        # Merged array display (initially hidden)
        self.merged_frame = tk.LabelFrame(arrays_frame, text="Merged Array", 
                                         font=('Arial', 12, 'bold'), bg='#2c2c2c', 
                                         fg='#00ff88', padx=10, pady=10)
        self.merged_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
        self.merged_frame.grid_remove()  # Hide initially
        
        # Buttons frame
        buttons_frame = tk.Frame(main_frame, bg='#1a1a1a')
        buttons_frame.pack(pady=20)
        
        # Merge button
        self.merge_btn = tk.Button(buttons_frame, text="🔀 MERGE ARRAYS", 
                                  command=self.merge_arrays, 
                                  font=('Arial', 12, 'bold'), 
                                  bg='#00ccff', fg='#1a1a1a', 
                                  padx=20, pady=10, 
                                  relief='raised', borderwidth=3)
        self.merge_btn.pack(side='left', padx=10)
        
        # Sort button
        self.sort_btn = tk.Button(buttons_frame, text="📊 SORT ARRAYS", 
                                 command=self.sort_arrays, 
                                 font=('Arial', 12, 'bold'), 
                                 bg='#ff6b35', fg='#1a1a1a', 
                                 padx=20, pady=10, 
                                 relief='raised', borderwidth=3)
        self.sort_btn.pack(side='left', padx=10)
        
        # Reset button
        reset_btn = tk.Button(buttons_frame, text="🔄 RESET", 
                             command=self.reset_arrays, 
                             font=('Arial', 12, 'bold'), 
                             bg='#666666', fg='white', 
                             padx=20, pady=10, 
                             relief='raised', borderwidth=3)
        reset_btn.pack(side='left', padx=10)
        
        # Randomize button
        randomize_btn = tk.Button(buttons_frame, text="🎲 RANDOMIZE", 
                                 command=self.randomize_arrays, 
                                 font=('Arial', 12, 'bold'), 
                                 bg='#9d4edd', fg='white', 
                                 padx=20, pady=10, 
                                 relief='raised', borderwidth=3)
        randomize_btn.pack(side='left', padx=10)
        
        # Status label
        self.status_label = tk.Label(main_frame, text="Ready to merge or sort!", 
                                   font=('Arial', 11), bg='#1a1a1a', fg='#cccccc')
        self.status_label.pack(pady=10)
        
        # Instructions
        instructions = tk.Text(main_frame, height=6, width=70, 
                              font=('Arial', 10), bg='#333333', fg='#cccccc',
                              relief='solid', borderwidth=2, padx=10, pady=10)
        instructions.pack(pady=20)
        instructions.insert('1.0', """INSTRUCTIONS:
• MERGE: Combines Array A and Array B into one array (maintains original order)
• SORT: Sorts individual arrays OR the merged array if it exists
• You can do operations in any order: Merge→Sort or Sort→Merge
• RESET: Returns to original arrays
• RANDOMIZE: Creates new random arrays to experiment with""")
        instructions.config(state='disabled')  # Make read-only
    
    def create_array_display(self, array, parent_frame):
        # Clear existing widgets
        for widget in parent_frame.winfo_children():
            widget.destroy()
        
        # Create a frame for array elements
        elements_frame = tk.Frame(parent_frame, bg=parent_frame['bg'])
        elements_frame.pack()
        
        # Display each element in a box
        for i, value in enumerate(array):
            element_frame = tk.Frame(elements_frame, bg='#444444', relief='solid', 
                                   borderwidth=2, padx=5, pady=5)
            element_frame.pack(side='left', padx=2, pady=5)
            
            element_label = tk.Label(element_frame, text=str(value), 
                                   font=('Arial', 12, 'bold'), 
                                   bg='#444444', fg='#ffffff')
            element_label.pack()
        
        # Display array as text below
        array_text = tk.Label(parent_frame, text=f"{array}", 
                             font=('Arial', 10), 
                             bg=parent_frame['bg'], fg='#888888')
        array_text.pack(pady=5)
    
    def update_display(self):
        """Update all array displays"""
        self.create_array_display(self.array_a, self.array_a_frame)
        self.create_array_display(self.array_b, self.array_b_frame)
        
        if self.is_merged and self.merged_array:
            self.create_array_display(self.merged_array, self.merged_frame)
            self.merged_frame.grid()  # Show merged frame
        else:
            self.merged_frame.grid_remove()  # Hide merged frame
    
    def merge_arrays(self):
        """Merge Array A and Array B"""
        if self.is_merged:
            messagebox.showinfo("Already Merged", "Arrays are already merged! Use RESET to start over.")
            return
        
        # Simple merge (concatenation)
        self.merged_array = self.array_a + self.array_b
        self.is_merged = True
        
        self.update_display()
        self.status_label.config(text=f"✅ Arrays merged! Result: {self.merged_array}")
        
        # Update button states
        self.merge_btn.config(state='disabled', bg='#555555')
    
    def sort_arrays(self):
        """Sort arrays (individual arrays if not merged, or merged array if merged)"""
        if self.is_merged:
            # Sort the merged array
            self.merged_array.sort()
            self.status_label.config(text=f"✅ Merged array sorted! Result: {self.merged_array}")
        else:
            # Sort individual arrays
            self.array_a.sort()
            self.array_b.sort()
            self.status_label.config(text=f"✅ Individual arrays sorted! A: {self.array_a}, B: {self.array_b}")
        
        self.update_display()
    
    def reset_arrays(self):
        """Reset to original arrays"""
        self.array_a = [3, 7, 11, 15, 20]
        self.array_b = [4, 8, 12, 16, 25]
        self.merged_array = []
        self.is_merged = False
        
        # Reset button states
        self.merge_btn.config(state='normal', bg='#00ccff')
        
        self.update_display()
        self.status_label.config(text="🔄 Reset complete! Ready to merge or sort again.")
    
    def randomize_arrays(self):
        """Create random arrays"""
        self.array_a = sorted([random.randint(1, 50) for _ in range(random.randint(3, 6))])
        self.array_b = sorted([random.randint(1, 50) for _ in range(random.randint(3, 6))])
        self.merged_array = []
        self.is_merged = False
        
        # Reset button states
        self.merge_btn.config(state='normal', bg='#00ccff')
        
        self.update_display()
        self.status_label.config(text=f"🎲 New random arrays created! A: {self.array_a}, B: {self.array_b}")

class MergeSortDemo:
    def __init__(self):
        self.root = tk.Tk()
        self.gui = MergeSortGUI(self.root)
    
    def run(self):
        """Start the application"""
        self.root.mainloop()

def main():
    """Main function to run the application"""
    print("🚀 Starting Interactive Merge & Sort Visualization...")
    print("Close the window or press Ctrl+C to exit.")
    
    try:
        app = MergeSortDemo()
        app.run()
    except KeyboardInterrupt:
        print("\n👋 Application closed by user.")
    except Exception as e:
        print(f"❌ Error: {e}")
        messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    main()
