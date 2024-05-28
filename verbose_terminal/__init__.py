from .main import msg

# Aliases for styles
def success(message, verbose=False):
    msg(message, verbose=verbose, style='success')

def warning(message, verbose=False):
    msg(message, verbose=verbose, style='warning')

def error(message, verbose=False):
    msg(message, verbose=verbose, style='error')

def info(message, verbose=False):
    msg(message, verbose=verbose, style='info')

def success_light(message, verbose=False):
    msg(message, verbose=verbose, style='success_light')

def warning_light(message, verbose=False):
    msg(message, verbose=verbose, style='warning_light')

def error_light(message, verbose=False):
    msg(message, verbose=verbose, style='error_light')

def info_light(message, verbose=False):
    msg(message, verbose=verbose, style='info_light')
