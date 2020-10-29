# Python Modules
 * #### Packages

## Modules Introduction:
__1.__ what are packages in python?
		
  A package is a namespace that organizes a set of related set of modules
  and that must have **_ init _.py**
  

  When working on large application, which has many modules written and dumped into a file location. As complexity grows it is very hard to identify and track the modules.
  It is good practice to group the similar modules into a package. 
  
  Example package structure


    ├── package_first                  
    │   ├── foo  
    |        └── __unit__.py                
    └── __unit__.py  
		
	
	
__2.__  **_init _.py** ?
  
  If the **_ _init_ _.py** file in the package directory contains a list named **_ all _**, it is taken to be a list of modules that should be imported when the statement from <package_name> import * is encountered.
  
  The **_ _init_ _.py** file can also decide which modules the package exports as the API, while keeping other modules internal, by overriding the **_ all _** variable  
  
  		#__init__.py:

		__all__ = ["module_name1","module_name2"] # here we can selectively call and restrict the modules to be imported
  

## Below Changes are implemented
### Build a calculator package that has separate module for:
  1. sin, cos, tan, tanh, SoftMax, Sigmoid, ReLU, log and e
  2. The modules shall include their derivatives as well
  3. If we do import calculator, we should be able to access all the above function (except deviratives)
  4. For derivates we must do: from package import derivatives. 
  5. Outputs are returned as well as printed using only f-string
  6. Write simple test cases to check the outputs of each operator and their derivative


## Function used
  * cos
  * sin
  * tan
  * tanh
  * sigmoid
  * softmax
  * exponential
  * log
  * derivatives for each Function
  
  ## Output
  
  ### From Local test logs
  
  ### ![output](https://github.com/Gaju27/session12/blob/main/local_output.JPG)
  
  
  ### From Github Action test logs
  
  #### ![github_action](https://github.com/Gaju27/session11/blob/main/git_action_output.JPG)
