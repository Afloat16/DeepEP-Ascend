import pytest

from deep_ep.utils.testing import parse_num_bytes


@pytest.mark.parametrize(
    ('text', 'expected'),
    (
        ('1K', 1 << 10),
        ('1.5 MiB', 3 << 19),
        ('9007199254740993', 9007199254740993),
        ('1.0009765624999999999K', 1024),
    ),
)
def test_parse_num_bytes_exact(text, expected):
    assert parse_num_bytes(text) == expected


@pytest.mark.parametrize('text', ('0', '0.0001', '-1G', '1.2.3M', '1P'))
def test_parse_num_bytes_rejects_invalid_values(text):
    with pytest.raises(ValueError):
        parse_num_bytes(text)
