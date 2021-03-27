

def test_contests(contest, program, input_file, output_file):
    result = contest(program, input_file)
    assert result == output_file.read_text()
