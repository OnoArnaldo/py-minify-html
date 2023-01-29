from minifyhtml import remove_blank_lines, trim_lines, remove_repeated_spaces, minify


def test_remove_blank_lines():
    assert list(remove_blank_lines([
        'line 1',
        '',
        '  line 2  ',
        '  '
    ])) == [
        'line 1',
        '  line 2  ',
        '  '
    ]


def test_trim_lines():
    assert list(trim_lines([
        'line 1',
        '',
        '  line  2  ',
        '  '
    ])) == [
        'line 1',
        '',
        'line  2',
        ''
    ]


def test_remove_repeated_spaces():
    assert list(remove_repeated_spaces([
        'line 1',
        '',
        '  line  2  ',
        '  '
    ])) == [
        'line 1',
        '',
        ' line 2 ',
        ' '
    ]


def test_minify():
    assert list(minify([
        'line 1',
        '',
        '  line  2  ',
        '  '
    ])) == [
        'line 1',
        'line 2'
    ]