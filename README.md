# High-Throughput-Analyzer
**Faster & more automatic analyzer of Che-protein dynamics in *E.coli* cells**

This project is developed and tested with Python 3.11/3.12 using VSCode + Jupyter (.ipynb support via the Jupyter extension). Other environments (e.g., plain Jupyter Notebook/Lab) should also work, but are not officially tested.


## ⚙️Setup
`pip install -r requirements.txt`

## 🚀Usage
### 0. Folder structure
We analyze tif files, and result files are generated one after another in the same location as the tif file.
If you put multiple tif files into a single folder, this causes problems, such as:  

✗ It becomes hard to understand later   
✗ Files with the same name get overwritten unintentionally  

To avoid this, use a one folder per tif file format.
We recommend creating a folder named date_chambername (as shown in the figure) and placing the tif file with the same name inside it.

### 1.

## 📄Licence
MIT
