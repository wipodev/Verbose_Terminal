from verbose_terminal import Msg

def test_msg(capsys):
    Msg.success("Test message", True)
    captured = capsys.readouterr()
    assert "success message: Test message" in captured.out