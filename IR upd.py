import cv2
from tkinter import *
from tkinter import filedialog
import pytesseract

class ImageReader:
    def __init__(self):
        window = Tk()
        window.title("Studio Super: Perfect Parlay 1.0")  # Create and add a frame to window
        frame0 = Frame(window)
        frame0.grid(row=1, column=1, sticky=W)
        
        
        self.path_label = Label(window, text="Please input your path:")
        self.path_label.grid(row=0, column=0, sticky=W, padx=10, pady=10)


        #browse images button
        self.browse_button = Button(window, text="Browse Images", command=self.browse_image)
        self.browse_button.grid(row=0, column=2, padx=10, pady=10)

        #browse images entry
        self.path_entry = Entry(window)
        self.path_entry.grid(row=0, column=1, padx=10, pady=10)

        #compile list
        btlist = Button(window, text="Compile List", command=self.desired).grid(row=0, column=4, padx=10, pady=10)
        
#       Text area to display extracted text
        self.desired_rows = Text(window, height=10, width=50)
        self.desired_rows.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.7)

        # Make the window size fixed
        window.resizable(False, False)

        # Make the window size large enough to fit the long rows of text
        window.geometry("1000x600")

        window.mainloop()

    def browse_image(self):
        # Open file dialog to select an image
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")])
        self.path_entry.delete(0, END)  # Clear previous content
        self.path_entry.insert(END, file_path)

        # Find the rows that contain the desired strings
    def desired(self):
        img1 = self.path_entry.get()
        img = cv2.imread(img1)
        
        pytesseract.pytesseract.tesseract_cmd = 'C:\\\\Program Files\\\\Tesseract-OCR\\\\tesseract.exe'
        
        # Extract text from the image
        text = pytesseract.image_to_string(img)

        # Split the text into rows
        rows = text.split('\n')
        desired_rows = []

        for row in rows:
            # Use a logical or operator instead of a logical and operator
            if ("hit 4/5 for 80%" in row or "hit 5/5 for 100%" in row) or ("hit 8/10 for 80%" in row or "hit 9/10 for 90%" in row or "hit 10/10 for 100%" in row):
        # Split the row into columns
                columns = row.split()

        # Check if the row contains a player name
                if len(columns) > 1 and columns[0] != "name":
                    desired_rows.append(row)


        # Insert a separator and a label for the new image
        self.desired_rows.insert(END, "\n" + "-" * 50 + "\n")
        self.desired_rows.insert(END, "Text from " + img1 + "\n")

        # Add a tag to configure the color
        self.desired_rows.tag_configure("red", foreground="red")

        for row in desired_rows:
            # Split the row into columns
            columns = row.split()

            # Check if the row contains a player name
            if len(columns) > 1 and columns[0] != "name":
                # Insert player name in red with the "red" tag
                self.desired_rows.insert(END, columns[0] + " ", "red")
                # Insert the rest of the row in black
                self.desired_rows.insert(END, " ".join(columns[2:]) + "\n")
            else:
                # Insert the entire row in black
                self.desired_rows.insert(END, columns[0:] + "\n")


ImageReader()

