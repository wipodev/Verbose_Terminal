from verbose_terminal import success, warning, error, info, success_light, warning_light, error_light, info_light, msg

def test_msg(capsys):
  success("Test message", True)
  out, err = capsys.readouterr()
  assert out == "\033[1;32;42m success message: Test message \033[0m\n"