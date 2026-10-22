# FoodMatch Complete — 50 Menus

## Included
- Flask web application
- Responsive HTML/CSS for desktop and mobile
- 50 menu items and 50 separate JPG food illustrations in `static/images`
- Weighted Scoring Model sample ranking
- Menu category filtering and menu-name search
- `requirements.txt`

## Run on Windows (VS Code PowerShell)
Open a terminal in the folder containing `app.py` and run:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

If PowerShell blocks script activation, run this in the current terminal first:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```
Then activate the environment again. Alternatively, skip activation and run:
```powershell
py -m pip install flask
py app.py
```

Open http://127.0.0.1:5000 in your browser.

## Important
Menu prices, taste scores and spiciness are illustrative sample data, not survey results. Images are illustrative generated images, not verified photos of actual restaurant dishes.
