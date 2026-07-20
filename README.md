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

### 2. File loading and configuration of various settings
The first cell in this section launches a GUI for parameter input.

### 3. Estimation of Cellular Fluorescence Intensity

### 4. Review Results of estimation of Cellular Fluorescence Intensity

### 5. Fitting

### 6. Save cell distribution map

### 7. Manual Visal Inspection

### 8. Estimate localization duration

### 9. Manual Visal Inspection of localization Duration

Additional analysys
---

### 10. Save Powerpoint, pole&cyto in text file

### 11. Centroid trajectory

### 12. Aggregation of parameters [cell area, average brightness etc]

### 13. Visualyze cell area

### 14. Variation in the number of analyzed cells

## 📄Licence
MIT
