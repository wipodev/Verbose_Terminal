from .styles import styles, reset

class Msg:
    @staticmethod
    def msg(message: str, verbose: bool = False, style: str = 'reset'):
        if verbose:
            if style in styles:
                print(f'{styles[style]} {style.replace("_light", "")} message: {message} {reset}')
            else:
                print(message)
    
    @classmethod
    def success(cls, message, verbose=False):
        cls.msg(message, verbose=verbose, style='success')

    @classmethod
    def warning(cls, message, verbose=False):
        cls.msg(message, verbose=verbose, style='warning')

    @classmethod
    def error(cls, message, verbose=False):
        cls.msg(message, verbose=verbose, style='error')

    @classmethod
    def info(cls, message, verbose=False):
        cls.msg(message, verbose=verbose, style='info')

    @classmethod
    def success_light(cls, message, verbose=False):
        cls.msg(message, verbose=verbose, style='success_light')

    @classmethod
    def warning_light(cls, message, verbose=False):
        cls.msg(message, verbose=verbose, style='warning_light')

    @classmethod
    def error_light(cls, message, verbose=False):
        cls.msg(message, verbose=verbose, style='error_light')

    @classmethod
    def info_light(cls, message, verbose=False):
        cls.msg(message, verbose=verbose, style='info_light')

if __name__ == '__main__':
  # Examples of use
  Msg.success("Test message", True)
  Msg.warning("Test message", True)
  Msg.error("Test message", True)
  Msg.info("Test message", True)
  Msg.success_light("Test message", True)
  Msg.warning_light("Test message", True)
  Msg.error_light("Test message", True)
  Msg.info_light("Test message", True)