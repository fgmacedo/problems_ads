def test_contests(contest, input_file, output_file):
    result = contest(input_file)
    expected = output_file.read_text()
    print("Result:")
    print(result)
    print("Expected:")
    print(expected)
    assert result == expected
