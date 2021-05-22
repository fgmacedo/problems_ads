def test_contests(contest, input_file, output_file):
    result = contest(input_file)
    assert result == output_file.read_text()
