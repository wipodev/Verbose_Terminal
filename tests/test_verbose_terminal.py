from verbose_terminal import Msg

def test_success_verbose(capsys):
    Msg.success("Test success message", verbose=True)
    captured = capsys.readouterr()
    print(captured.out)
    assert "success message: Test success message" in captured.out

def test_warning_verbose(capsys):
    Msg.warning("Test warning message", verbose=True)
    captured = capsys.readouterr()
    print(captured.out)
    assert "warning message: Test warning message" in captured.out

def test_error_verbose(capsys):
    Msg.error("Test error message", verbose=True)
    captured = capsys.readouterr()
    print(captured.out)
    assert "error message: Test error message" in captured.out

def test_info_verbose(capsys):
    Msg.info("Test info message", verbose=True)
    captured = capsys.readouterr()
    print(captured.out)
    assert "info message: Test info message" in captured.out

def test_success_light_verbose(capsys):
    Msg.success_light("Test success light message", verbose=True)
    captured = capsys.readouterr()
    print(captured.out)
    assert "success message: Test success light message" in captured.out

def test_warning_light_verbose(capsys):
    Msg.warning_light("Test warning light message", verbose=True)
    captured = capsys.readouterr()
    print(captured.out)
    assert "warning message: Test warning light message" in captured.out

def test_error_light_verbose(capsys):
    Msg.error_light("Test error light message", verbose=True)
    captured = capsys.readouterr()
    print(captured.out)
    assert "error message: Test error light message" in captured.out

def test_info_light_verbose(capsys):
    Msg.info_light("Test info light message", verbose=True)
    captured = capsys.readouterr()
    print(captured.out)
    assert "info message: Test info light message" in captured.out

def test_simple_message(capsys):
    Msg.msg("Test simple message", verbose=True)
    captured = capsys.readouterr()
    print(captured.out)
    assert "Test simple message" in captured.out

def test_verbose_false(capsys):
    Msg.success("Test verbose false message", verbose=False)
    captured = capsys.readouterr()
    print(captured.out)
    assert "" in captured.out