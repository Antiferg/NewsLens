import sys

def error_message_detail(error,error_detail:sys):
    _,_,err = error_detail.exc_info()
    filename=err.tb_frame.f_code.co_filename
    error_message=f'The error occured in {filename} on line {err.tb_lineno} with {str(error)} error'
    return error_message

class CustomExceptionMessage(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    def __str__(self):
        return self.error_message