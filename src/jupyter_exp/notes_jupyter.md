# Jupyter Notebook notes

# Kernel selection

See e.g. https://www.youtube.com/watch?v=K7NLegbvbNE

Use case: Use kernel from conda environment "ml-exp":
* activate your conda environment: `conda activate ml-exp`
* if not yet done, install ipykernel: `conda install -c anaconda ipykernel`
  * alternative: `conda install -c conda-forge ipykernel` or without the `-c` option at all 
* Install the kernel for Jupyter: `python -m ipykernel install --user --name=ml-exp`
  - -> Installed kernelspec ml-exp in /home/emm/.local/share/jupyter/kernels/ml-exp
  - optionally, give another name to display with option `--display-name "Python 3 ml-exp`
* Start notebook:`jupyter notebook`
* Open browser like:  http://localhost:8888/tree?token=4f218a9da50f224bd35776d83c8cc327ab5c896bc4d0b5f3
* Select kernel from drop-down list: "New" or "Start preferred Kernel", select "ml-exp" 

## Jupyter Keyboard Shortcuts 

Just a few I would use often... 

- Run cell: `Shift + Enter`
- Navigate up or down to cells: `Esc, Up` or `Esc, Down`
- Insert cell below or above: `Esc, Shift+B`, `Esc, Shift+A`
- Change cell type: 
  - change to MD: `Esc, Ctrl+M`
  - change to code: `Esc, Ctrl+C`
- Table of Contents:  `Ctrl + Shift + K`


### All shortcuts: 

| Description | Key combination| 
| --- | --- |
| Redo | Ctrl + Shift + Z | 
| Undo | Ctrl + Z | 
| Run Selected Cell | Shift + Enter | 
| Find Next | Ctrl + G | 
| Find Previous | Ctrl + Shift + G | 
| Find… | Ctrl + F | 
| Activate Next Tab | Ctrl + Shift + ] | 
| Activate Next Tab Bar | Ctrl + Shift + . | 
| Activate Previous Tab | Ctrl + Shift + [ | 
| Activate Previous Tab Bar | Ctrl + Shift + , | 
| Toggle Left Area | Ctrl + B | 
| Toggle Mode | Ctrl + Shift + D | 
| Toggle Right Area | Ctrl + J | 
| Toggle Sidebar Widget | Alt + 1 | 
| Toggle Sidebar Widget | Alt + 2 | 
| Toggle Sidebar Widget | Alt + 3 | 
| Toggle Sidebar Widget | Alt + 4 | 
| Toggle Sidebar Widget | Alt + 5 | 
| Toggle Sidebar Widget | Alt + 6 | 
| Toggle Sidebar Widget | Alt + 7 | 
| Toggle Sidebar Widget | Alt + 8 | 
| Toggle Sidebar Widget | Alt + 9 | 
| Toggle Sidebar Widget | Alt + 0 | 
| Toggle Sidebar Widget | Alt + Shift + 1 | 
| Toggle Sidebar Widget | Alt + Shift + 2 | 
| Toggle Sidebar Widget | Alt + Shift + 3 | 
| Toggle Sidebar Widget | Alt + Shift + 4 | 
| Toggle Sidebar Widget | Alt + Shift + 5 | 
| Toggle Sidebar Widget | Alt + Shift + 6 | 
| Toggle Sidebar Widget | Alt + Shift + 7 | 
| Toggle Sidebar Widget | Alt + Shift + 8 | 
| Toggle Sidebar Widget | Alt + Shift + 9 | 
| Toggle Sidebar Widget | Alt + Shift + 0 | 
| Activate Command Palette | Ctrl + Shift + C | 
| Show Keyboard Shortcuts… | Ctrl + Shift + H | 
| Pause | F9 | 
| Next | F10 | 
| Debugger Panel | Ctrl + Shift + E | 
| Step In | F11 | 
| Step Out | Shift + F11 | 
| Terminate | Shift + F9 | 
| Save Notebook | Ctrl + S | 
| Save Notebook As… | Ctrl + Shift + S | 
| Reopen Last | Ctrl + Shift + T | 
| Activate Previously Used Tab | Ctrl + Shift + ' | 
| Table of Contents | Ctrl + Shift + K | 