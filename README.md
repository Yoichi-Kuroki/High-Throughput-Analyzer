# High-Throughput-Analyzer
**Faster & more automatic analyzer of Che-protein dynamics in *E.coli* cells**

This project is developed and tested with Python 3.11/3.12 using VSCode + Jupyter (.ipynb support via the Jupyter extension). Other environments (e.g., plain Jupyter Notebook/Lab) should also work, but are not officially tested.


## ⚙️Setup
`pip install -r requirements.txt`

## 🚀How to analyze
### 0. Folder structure
We analyze tif files, and result files are generated one after another in the same location as the tif file.
If you put multiple tif files into a single folder, this causes problems, such as:  

✗ It becomes hard to understand later   
✗ Files with the same name get overwritten unintentionally  

To avoid this, use a one folder per tif file format.
We recommend creating a folder named date_chambername (as shown in the figure) and placing the tif file with the same name inside it.
<p align="center">
  <img width="300"  alt="image" src="https://github.com/user-attachments/assets/76b63f01-29c1-4997-8060-8d4b731479a8" />
</p>


**In general, you just execute the cells sequentially, starting from the top one.**
### 1. Function declarations and library imports
16 cells. This section handles library imports and function declarations. You only need to run it once per analysis—after that, the functions are registered and ready to use.

### 2. Configuration of various settings and File loading
The first cell in this section launches a GUI for parameter input.
<p align="center">
  <img width="1969" height="723" alt="image" src="https://github.com/user-attachments/assets/7fdbae41-87d5-4041-a0e9-e58d8bb2e78d" />
</p>

You can load file that you 
In the second cell, it loads the Tiff file.
Please wait, as this takes more than 10 seconds.

For images of 1152×1152 pixels, it will apply correction for excitation light unevenness. 
Even if the size is different, it can still be loaded, but correction will not be applied, so you will see the warning: "The analysis image and correction image sizes do not match!"

### 3. Estimation of Cellular Fluorescence Intensity
Detects and tracks cells from images, converts them into low-dimensional data, and collects various parameters.
This step will take about 10 minutes or more.

### 4. Review Results of estimation of Cellular Fluorescence Intensity
It is recommended to check the quality of the entered parameters and the aggregated luminance (intensity) values.
Additional analysis > Let's try running the "Variation in the number of analyzed cells" section.

### 5. Fitting
Now, if you run the "Fitting" cell, the graphs will all be output at once.
These results fall into three patterns:

- Cases where fitting succeeded and the pole was estimated (a time trace will be plotted)
- Cases where fitting succeeded but the pole could not be estimated
- Cases where fitting failed

It is necessary for the analyst to briefly review these results.
<img width="1269" height="582" alt="image" src="https://github.com/user-attachments/assets/4fb4178b-c0f8-44ef-95b6-ac2fd74e34db" />

### 6. Save cell distribution map
This section displays an important clue that tells you which cell number the program has assigned to each cell.
When you run the cell, "cell_distribution_map.png" and "[tif filename]_cell_map.zip" will be saved.
Cell Distribution Map.png can be checked visually. Additionally, for checking changes over time, it is recommended to use cell_map.zip in conjunction with ImageJ.
cell_map.zip contains `.roi` files for use with ImageJ's ROI Manager feature.
<p align="center">
  <img width="300"  alt="image" src="https://github.com/user-attachments/assets/37a90291-5c48-448b-9ce3-215c1c0a3c57" />
</p>

### 7. Manual Visual Inspection
<p align="center">
  <img height="300" alt="mvi_hta" src="https://github.com/user-attachments/assets/080bf588-9b06-4285-8526-c9a273f7ad85" />
</p>

### 8. Estimate localization duration

### 9. Manual Visual Inspection of localization Duration

Additional analysis
---

### 10. Save Powerpoint, pole&cyto in text file

### 11. Centroid trajectory

### 12. Aggregation of parameters [cell area, average brightness etc]

### 13. Visualize cell area

### 14. Variation in the number of analyzed cells

In the first cell, you can see the variation in the number of tracked cells.
The orange line represents the number of cells detected in each frame, while the blue line represents the number of cells that have been assigned numbers and are being successfully tracked. Since cells are gradually lost from tracking over time, the blue line will gradually decrease. If the blue or orange line drops suddenly, this may indicate an issue such as defocusing, so please check the original image.

In the next cell, you can get a rough idea of things like the timing of solution exchange and the time at which localization reached its maximum.
The blue line is the average, across all cells, of the "maximum intracellular luminance (intensity) value."
The red line is the average, across all cells, of the "mean intracellular luminance (intensity) value."
The green line is the difference between the two.
Additionally, the vertical black line indicates the currently set solution exchange time. If this does not match the pattern of change in the luminance values, you will need to reconfigure the parameter settings. Since this affects not only the localization duration but also things like the fitting, please set it as precisely as possible.

In the third cell, you can check the change over time in the average cell length.
Normally, the length changes very little.
However, if the salt concentration of the exchanged solution is incorrect, for example, you may observe the cells shrinking or elongating.
<img width="1494" height="450" alt="image" src="https://github.com/user-attachments/assets/4fe9ea3b-cf56-46b1-8866-0f10dc239559" />


## 📄Licence
MIT
