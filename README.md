Project Report: BMR and Protein Intake Recommendation Program

Project Description
The project involves developing a tkinter-based application that calculates Basal Metabolic Rate (BMR) and recommends daily protein intake based on user-entered data such as weight, height, age, and gender. It also includes functionality to log daily protein intake, display cumulative intake, and track progress towards recommended goals.

GitHub Repository
You can find the final code for this project on my GitHub repository: https://github.com/julianaperesmachado/ProteinCalculator.JulianaPeres/blob/main/ProteinCalculator.py

Programming Concepts Implemented
1.	Graphical User Interface (GUI) using tkinter for creating windows, labels, buttons, and entry widgets.
2.	Image Handling with Pillow (PIL) for loading and resizing images in the GUI.
3.	Error Handling with try-except blocks to manage invalid user inputs.
4.	Data Persistence using dictionaries to store and display protein intake history.
5.	Object-Oriented Programming (OOP) with tkinter frames and classes for modular code organization.

New Techniques Learned
•	Image Handling with Pillow: Loading and resizing images for GUI elements.
•	Creating Custom GUI Components: Using tkinter to build custom frames (like HistoryWindow) for specific functionalities.
•	GUI Layout and Design: Placing widgets and frames within the main window for structured user interaction and utilizing different fonts and colors to enhance GUI aesthetics and readability in tkinter applications.

Screenshots
  Main Application Window: 
 
  Pop-up messagebox:
 
  Protein Intake Logging Window: 

Overall Flow of the Program (Flowchart)
 
Function Names and Their Input/Output
1.	calculate_protein_intake()
•	Inputs: Weight, height, age, gender from user inputs.
•	Outputs: BMR, recommended protein intake displayed in the GUI.
2.	save_data_to_file()
•	Inputs: User name, weight, height, age, gender, BMR, recommended protein intake.
•	Outputs: Data appended to bmr_data.txt.
3.	log_protein_prompt() and open_log_intake_window()
•	Inputs: User confirmation to log daily protein intake.
•	Outputs: Opens a window for logging protein intake with historical data display.
4.	HistoryWindow class
•	Inputs: Parent window, user name.
•	Outputs: Displays protein intake history and allows logging new entries.
Structure of Classes Used

HistoryWindow Class:
•	Variables:
  o	user_name: Name of the current user.
  o	total_protein_intake: Cumulative protein intake logged.
  o	recommended_goal: Recommended daily protein intake goal.
  o	history_text: Text widget to display protein intake history.
o	protein_entry: Entry widget to input daily protein intake.
•	Methods:
  o	__init__(self, parent): Initialize GUI components within the parent window.
  o	log_daily_protein_intake(self): Log daily protein intake and update display.
  o	update_protein_history_display(self): Update the displayed protein intake history.

References
Image credit (Protein Rich Food Flat Icons Set - De Macrovector): 
https://stock.adobe.com/br/search?filters%5Bcontent_type%3Aphoto%5D=1&filters%5Bcontent_type%3Aillustration%5D=1&filters%5Bcontent_type%3Azip_vector%5D=1&filters%5Bcontent_type%3Avideo%5D=1&filters%5Bcontent_type%3Atemplate%5D=1&filters%5Bcontent_type%3A3d%5D=1&filters%5Bcontent_type%3Aaudio%5D=0&filters%5Binclude_stock_enterprise%5D=0&filters%5Bis_editorial%5D=0&filters%5Bfree_collection%5D=0&filters%5Bcontent_type%3Aimage%5D=1&k=protein+food&order=relevance&safe_search=1&limit=100&search_page=14&search_type=pagination&get_facets=0&asset_id=112316855
