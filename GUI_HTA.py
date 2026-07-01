"""
Created a GUI using tkinter. Since it is not strictly required for HTA
(as input can also be provided via CUI), it has been separated into a
separate file to keep the code readable. Place it in the same directory
as the main file and call it from there.

The following GUIs are included:
1. GUI for setting the Tiff path and values required for analysis
2. Classes and structures shared by 3. and 4. below
3. GUI for displaying fitting results and confirming whether localization exists
4. GUI for displaying localization duration results and selecting them (nearly identical code to 3.)
"""

# -------------------------------------------------------------------------------
# 1. GUI for setting the Tiff path and values required for analysis
# -------------------------------------------------------------------------------

import tkinter as tk
import tkinter.filedialog
from tkinter import ttk


def open_tiff(editbox):  # GUI for opening a Tiff file

    # File selection
    filetypes = [("Data files", "*.tiff *.tif *.mptiff")]
    filepath = tkinter.filedialog.askopenfilename(
        filetypes=filetypes, title="Please select a Tiff file", initialdir=dir
    )

    editbox.delete(0, tk.END)  # Clear all text in the entry box
    editbox.insert(tk.END, filepath)  # Write filepath (with newline)


# GUI for parameter input
# Reference:
# https://www.simugrammer.com/python_tkinter_widget/#:~:text=%E3%80%90Python%E3%80%91tkinter%E3%81%AEWidget%E3%81%AE%E9%85%8D%E7%BD%AE%E6%96%B9%E6%B3%95%E3%80%90%E3%82%B5%E3%83%B3%E3%83%97%E3%83%AB%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%A0%E3%81%A7%E8%A7%A3%E8%AA%AC%E3%80%91%201%20tkinter%E3%81%AEWidget%E3%81%A8%E3%81%AF%20tkinter%20%E3%81%AF%20python%20%E3%81%AB%E3%83%87%E3%83%95%E3%82%A9%E3%83%AB%E3%83%88%E3%81%A7%E5%85%A5%E3%81%A3%E3%81%A6%E3%81%84%E3%82%8B%E3%80%81GUI%E3%83%A9%E3%82%A4%E3%83%96%E3%83%A9%E3%83%AA%E3%81%A7%E3%81%99%E3%80%82%20...,%E3%81%9D%E3%81%AE%EF%BC%91%E3%80%8Eplace%E3%80%8F%E2%80%A6%E3%83%94%E3%83%B3%E3%83%9D%E3%82%A4%E3%83%B3%E3%83%88%E3%81%A7%E4%BD%8D%E7%BD%AE%E3%82%92%E6%8C%87%E5%AE%9A%20...%204%20%E3%81%9D%E3%81%AE%EF%BC%92%E3%80%8Epack%E3%80%8F%E2%80%A6%E7%B8%A6or%E6%A8%AA%E3%81%AB%E6%95%B4%E5%88%97%E3%81%97%E3%81%A6%E9%85%8D%E7%BD%AE%20...%205%20%E3%81%9D%E3%81%AE%EF%BC%93%E3%80%8Egrid%E3%80%8F%E2%80%A6EXCEL%E3%81%AE%E3%82%88%E3%81%86%E3%81%AB%E3%83%9E%E3%82%B9%E7%9B%AE%E7%8A%B6%E3%81%AB%E9%85%8D%E7%BD%AE%20
def valueget(params):
    root = tk.Tk()
    root.title("Please enter various settings")

    iconphoto = tk.PhotoImage(file="HTAicon.png")
    root.iconphoto(False, iconphoto)  # Use HTA icon
    root.geometry("880x300")

    # Entry for displaying filename
    filepath = tk.StringVar()
    filepath.set(params[0])
    text_filename = tk.Entry(width=130, textvariable=filepath)
    text_filename.grid(
        row=0, column=1, columnspan=8, sticky="wens", padx=0, pady=10, ipady=10
    )
    # File selection button
    tiff_icon = tk.PhotoImage(file="Tiff.png")
    button_select = tk.Button(
        image=tiff_icon,
        width=60,
        text="select Tiff",
        compound="top",
        command=lambda: open_tiff(text_filename),
    )
    button_select.grid(row=0, column=0, sticky="wens", padx=1, pady=10, ipady=10)

    # FPS input
    fps = tk.StringVar()
    fps.set(params[1])
    label_fps = tk.Label(root, text="fps")
    entry_fps = tk.Entry(width=5, textvariable=fps)
    label_fps.grid(row=1, column=1, sticky="wens")
    entry_fps.grid(row=1, column=2, sticky="wens", padx=5, pady=10)

    # Input for CheR observation end frame
    analyze_frame_Re = tk.StringVar()
    analyze_frame_Re.set(params[2])
    label_ana_frame_Re = tk.Label(root, text="CheR end")
    entry_ana_frame_Re = tk.Entry(width=5, textvariable=analyze_frame_Re)
    label_ana_frame_Re.grid(row=3, column=1, sticky="wens")
    entry_ana_frame_Re.grid(row=3, column=2, sticky="wens", padx=5, pady=10)

    # Input for CheB observation start frame
    analyze_frame_Bs = tk.StringVar()
    analyze_frame_Bs.set(params[3])
    label_ana_frame_Bs = tk.Label(root, text="CheB start")
    entry_ana_frame_Bs = tk.Entry(width=5, textvariable=analyze_frame_Bs)
    label_ana_frame_Bs.grid(row=3, column=4, sticky="wens")
    entry_ana_frame_Bs.grid(row=3, column=5, sticky="wens", padx=5, pady=10)

    # End frame for analysis
    analyze_frame = tk.StringVar()
    analyze_frame.set(params[4])
    label_ana_frame = tk.Label(root, text="CheB end")
    entry_ana_frame = tk.Entry(width=5, textvariable=analyze_frame)
    label_ana_frame.grid(row=3, column=6, sticky="wens")
    entry_ana_frame.grid(row=3, column=7, sticky="wens", padx=5, pady=10)

    # Solution exchange time
    addtion_time = tk.StringVar()
    addtion_time.set(",".join(map(str, params[5])))
    label_add = tk.Label(root, text="Solution exchange time (s)")
    entry_add = tk.Entry(width=10, textvariable=addtion_time)
    label_add.grid(row=5, column=1, sticky="wens")
    entry_add.grid(row=5, column=2, sticky="wens", padx=5, pady=10)

    # Fitting frame
    fitting_frame = tk.StringVar()
    fitting_frame.set(params[6])
    label_fit_frame = tk.Label(root, text="Frame for fitting")
    entry_fit_frame = ttk.Combobox(
        width=5, values=["", "Auto"], textvariable=fitting_frame
    )
    label_fit_frame.grid(row=5, column=4, sticky="wens")
    entry_fit_frame.grid(row=5, column=5, sticky="wens", padx=5, pady=10)

    # Minimum cell size
    mincellsize = tk.StringVar()
    mincellsize.set(params[7])
    label_mincs = tk.Label(root, text="MINCELLSIZE(pix)")
    entry_mincs = tk.Entry(width=10, textvariable=mincellsize)
    label_mincs.grid(row=1, column=4, sticky="wens")
    entry_mincs.grid(row=1, column=5, sticky="wens", padx=5, pady=10)

    # Maximum cell size
    maxcellsize = tk.StringVar()
    maxcellsize.set(params[8])
    label_maxcs = tk.Label(root, text="MAXCELLSIZE(pix)")
    entry_maxcs = tk.Entry(width=10, textvariable=maxcellsize)
    label_maxcs.grid(row=1, column=6, sticky="wens")
    entry_maxcs.grid(row=1, column=7, sticky="wens", padx=5, pady=10)

    # Input complete button
    button = tk.Button(text="Done", width=10, command=root.destroy)
    button.grid(row=6, column=8, sticky="wens", padx=10, pady=10)

    root.mainloop()

    ff = fitting_frame.get()
    try:
        if int(ff) > 0:
            ff = int(ff)
    except:
        if ff != "Auto":
            ff = "Auto"

    params = [
        filepath.get(),
        float(fps.get()),
        int(analyze_frame_Re.get()),
        int(analyze_frame_Bs.get()),
        int(analyze_frame.get()),
        sorted(list(map(float, addtion_time.get().split(",")))),
        ff,
        int(mincellsize.get()),
        int(maxcellsize.get()),
    ]

    return params


# -------------------------------------------------------------------------------

# 2. Classes and structures shared by 3. and 4. below

# -------------------------------------------------------------------------------

import os
import tkinter as tk
from PIL import ImageTk, Image

"""GUI for displaying cell images and graph images to select or discard data"""


class checkGUI(tk.Tk):
    def __init__(
        self,
        imgs: list[str],
        check_list: list[bool],
        file_dir: str,
        graph_dirname: str = "",
        cellimage_dirname: str = "",
    ):
        # Inherit tkinter functionality
        super().__init__()

        # Store arguments as member variables
        self.imgs = imgs
        self.check_list = check_list
        self.file_dir = file_dir
        self.graph_dirname = graph_dirname
        self.cellimage_dirname = cellimage_dirname

        self.count = 0

        iconphoto = tk.PhotoImage(file="HTAicon.png")
        self.iconphoto(False, iconphoto)  # Use HTA icon
        self.geometry("1000x500")

        # Canvas for result graph
        dir = self.file_dir + self.graph_dirname
        self.graph_canvas = ImageCanvas(self, dir, width=1000, height=200)
        self.graph_canvas.image_size = [1000, 200]
        self.graph_canvas.image_position = [500, 100]
        self.graph_canvas.image_filepath = os.path.join(
            self.file_dir, self.graph_dirname, self.imgs[self.count]
        )
        self.graph_canvas.draw_Image()
        self.graph_canvas.grid(row=1, column=0, columnspan=5, sticky="wens")

        # Canvas for cell and fitting result images
        dir = self.file_dir + self.cellimage_dirname
        self.cellimage_canvas = ImageCanvas(self, dir, width=600, height=200)
        self.cellimage_canvas.image_size = [600, 200]
        self.cellimage_canvas.image_position = [300, 100]
        self.cellimage_canvas.image_filepath = os.path.join(
            self.file_dir, self.cellimage_dirname, self.imgs[self.count]
        )
        self.cellimage_canvas.draw_Image()
        self.cellimage_canvas.grid(row=0, column=1, columnspan=3, sticky="wens")

        # Checkbox placement
        self.isCheck = tk.BooleanVar()
        self.isCheck.set(self.check_list[0])
        self.isCheck.trace_add(
            ("write", "unset"), self.callback
        )  # Command called when checkbox value changes
        local_check = tk.Checkbutton(
            text="Select data", variable=self.isCheck, font=("", 15)
        )
        local_check.grid(row=2, column=2, sticky="wens")

        # Label showing current position in the total
        self.count_text = tk.StringVar()
        self.count_text.set(
            f"{self.count+1}/{len(self.check_list)}"
        )  # Displayed as "X of Y" for readability
        counts_label = tk.Label(
            self, textvariable=self.count_text, font=("Arial", 20, "underline")
        )
        counts_label.grid(row=0, column=0, sticky="wens")

        # Button placement
        # Font size specification; font type is default
        fonts = ("Arial", 20)

        # NEXT > button placement
        button_r = tk.Button(
            text="NEXT ＞", width=5, font=fonts, command=self.nextImage
        )
        # Also triggered by arrow keys
        self.bind("<Right>", self.nextImage)
        self.bind("<d>", self.nextImage)

        button_r.grid(row=2, column=3, sticky="wens", padx=10, pady=10, ipady=5)

        # < BACK button placement
        button_l = tk.Button(
            text="＜ BACK", width=5, font=fonts, command=self.prevImage
        )
        # Also triggered by arrow keys
        self.bind("<Left>", self.prevImage)
        self.bind("<a>", self.prevImage)

        button_l.grid(row=2, column=1, sticky="wens", padx=10, pady=10, ipady=5)

    # Display the next image
    def nextImage(self, event=None):
        # event=None is required for keyboard operation

        if len(self.check_list) == 0:
            return
        self.count = (self.count + 1) % len(self.check_list)
        self.redraw()

    # Display the previous image
    def prevImage(self, event=None):
        # event=None is required for keyboard operation

        if len(self.check_list) == 0:
            return
        self.count = (self.count - 1) % len(self.check_list)
        self.redraw()

    # Refresh the screen
    def redraw(self):
        # Update count text
        self.count_text.set(f"{self.count+1}/{len(self.check_list)}")
        # Update checkbox state
        self.isCheck.set(self.check_list[self.count])

        # Update file paths
        self.graph_canvas.image_filepath = os.path.join(
            self.file_dir, self.graph_dirname, self.imgs[self.count]
        )
        self.cellimage_canvas.image_filepath = os.path.join(
            self.file_dir, self.cellimage_dirname, self.imgs[self.count]
        )
        # Draw images
        self.graph_canvas.draw_Image()
        self.cellimage_canvas.draw_Image()

    # Function called when checkbox value is updated
    def callback(self, var, index, mode):
        # Functions executed via trace_add require 3 arguments (var, index, mode).
        # None of them are used here, but do not remove them.

        # Update list value
        self.check_list[self.count] = self.isCheck.get()


"""Create a canvas for drawing images"""


class ImageCanvas(tk.Canvas):
    def __init__(self, root, filepath: str, width, height):

        self.image_filepath = filepath
        # Size of the image after resizing
        self.image_size = [200, 200]
        # Coordinates for displaying the image within the canvas
        # By default, the top-left corner of the image is aligned to the origin
        self.image_position = [100, 100]

        # Initialize tk.Canvas class
        super().__init__(root, width=width, height=height, highlightthickness=0)

    # Draw the image
    def draw_Image(self):
        img = Image.open(self.image_filepath)
        img = img.resize(self.image_size)
        # Image must be stored as a member variable or it will not be displayed
        self.image = ImageTk.PhotoImage(img)
        # Clear all objects drawn on the canvas
        self.delete("all")
        # Create image on the canvas
        self.create_image(*self.image_position, image=self.image)


# -------------------------------------------------------------------------------

# 3. GUI for displaying fitting results and confirming whether localization exists

# -------------------------------------------------------------------------------


def true_local_select(imgs, true_local, filepath):
    app = checkGUI(
        imgs,
        true_local,
        filepath,
        graph_dirname="graph_result",
        cellimage_dirname="fit_result",
    )
    app.title("Check fitting results")
    app.mainloop()
    # Return the check list at the end
    return app.check_list


# -------------------------------------------------------------------------------

# 4. GUI for displaying and selecting localization duration calculation results

# -------------------------------------------------------------------------------


# GUI for displaying fitting results and localization graphs to confirm results
def ld_select(imgs, true_local, filepath):
    app = checkGUI(
        imgs,
        true_local,
        filepath,
        graph_dirname="ld_result",
        cellimage_dirname="fit_result",
    )
    app.title("Check fitting results")
    app.mainloop()
    # Return the check list at the end
    return app.check_list
