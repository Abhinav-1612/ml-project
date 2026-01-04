# for exception handeling 
import sys 
# sys =>The sys module in Python provides various functions and variables that are used to manipulate different parts of the Python runtime environmenta It allows operating on the interpreter as it provides access to the variables and functions that interact strongly with the interpreter.
from src.logger import logging
#23 May 2022
def error_message_detail(error,error_details:sys):
    _,_,exc_tb=error_details.exc_info()  # tell in which line ,code the erro occured and get stored in this variable 
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="error ocuured in python script name [{0}] line no [{1}] error message [{2}] ".format(
    file_name,exc_tb.tb_lineno,str(error))
    
    return error_message
    

# print the errormsg u need this class in every code

class CustomException(Exception):
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_details=error_details)

    def __str__(self):
        return self.error_message
  
