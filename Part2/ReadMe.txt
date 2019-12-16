

*********************************************************************************
Test Instructions:
	Due to the size limitation on submission, the instances data (.txt .dzn) files are small instances with size <= 30, which can be used for MiniZinc Solvers (Sequential_Games.mzn and Sequential_Games_Solver.py).

	If want to test Python solver, please run Data_Generator.py directly by
		$python3 Data_Generator.py
	You will get 30 larger instances with size >= 250000. 
	After the Data_Generator terminate, run
		$python3 Python_Solver.py 
	to test the python_solver's running time

*********************************************************************************


Sequential_Games.mzn
	MiniZinc model with all constraints mentioned in the report.

	How to run:
		Open it with MiniZinc IDE and pass in .dzn file 

Data_Generator.py
	Generate random test data automatically, and save generated data into two types: .txt and .dzn. Variables can be edited for different data size.

	How to run:
		In terminal: $python3 Data_Generator.py

Sequential_Games_Solver.py
	A Python program that runs Sequential_Games.mzn in MiniZinc to solve several instances and record running time of each instances.
	Can choose different solver by comment current solver line and uncomment the other solver line.

	How to run:
		need minizinc library installed in terminal with: $pip3 install minizinc
		to load solvers from minizinc IDE: 
			$export PATH=/Applications/MiniZincIDE.app/Contents/Resources:$PATH
		run: $python3 Sequential_Games_Solver.py

Python_Solver.py
	Specific algorithm for this problem implemented in Python. Read instances from .txt files and record the running time for each instance. 

	How to run:
		$python3 Python_Solver.py


test_case#.dzn / test_case#.txt
	Instance data files in two file types for different use in MiniZinc and Python. 

