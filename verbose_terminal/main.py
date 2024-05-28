# TERMINAL COLORS (ANSI code)
styles = {
    'success': '\033[1;32;42m',     # light green text, green background
    'warning': '\033[1;33;43m',     # light yellow text, yellow background
    'error': '\033[1;31;41m',       # light red text, red background
    'info': '\033[1;36;44m',        # light cyan text, blue background
    'success_light': '\033[1;32m',  # light green text
    'warning_light': '\033[1;33m',  # light yellow text
    'error_light': '\033[1;31m',    # light red text
    'info_light': '\033[1;36m'      # light cyan text
}

reset = '\033[0m' # resetear al estilo por defecto

def msg(msg: str, verbose: bool = False, style: str = 'reset'):
    if verbose:
      if style in styles:
        print(f'{styles[style]} {style.replace("_light", "")} message: {msg} {reset}')
      else:
        print(msg)

if __name__ == '__main__':
  # Examples of use
  msg("This is a success message with background", True, 'success')
  msg("This is a warning message with background", True, 'warning')
  msg("This is an error message with background", True, 'error')
  msg("This is an info message with background", True, 'info')
  msg("This is a success message light", True, 'success_light')
  msg("This is a warning message light", True, 'warning_light')
  msg("This is an error message light", True, 'error_light')
  msg("This is an info message light", True, 'info_light')
  msg("This is a plain message", True, 'reset')
  msg("This is a plain message", True)
  msg("This is a simple message, which will not seem", False)
  msg("This is a simple message, which will not seem")