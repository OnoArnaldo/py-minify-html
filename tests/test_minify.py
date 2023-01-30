from minifyhtml import remove_blank_lines, trim_lines, remove_repeated_spaces, minify, remove_comments


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


def test_remove_comments():
    assert list(remove_comments([
        'line 1',
        '<!-- one line comment -->',
        '  line <!-- middle comment --> 2  ',
        '<!-- two lines',
        ' comment -->',
        'line 3 <!-- multi ',
        'comment --> line 4'
    ])) == [
        'line 1',
        '',
        '  line  2  ',
        '',
        '',
        'line 3 ',
        ' line 4'
    ]


def test_minify():
    assert list(minify([
        'line 1',
        '',
        '  line  2  <!-- comment -->',
        '  '
    ])) == [
        'line 1',
        'line 2'
    ]


def test_remove_comments():
    assert list(remove_comments([
        'before<!--https://page.domain.com/path/to/document/local-business-->after'
    ])) == ['beforeafter']