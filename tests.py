def test_output(script_runner):
    ret = script_runner.run("csv_sum.py")
    assert ret.success
    assert ret.stdout == "30\n"
    assert ret.stderr == ""
