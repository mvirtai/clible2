from clible.app.api_client import normalize_reference


def test_normalize_reference():
    # Yksinkertaisin tapaus
    assert normalize_reference("Gen 1:1") == ("gen", 1, [1])
    assert normalize_reference("John 3:16") == ("john", 3, [16])
    
    # Välilyönnit
    assert normalize_reference("Gen  1:1") == ("gen", 1, [1])
    
    # Isot kirjaimet
    assert normalize_reference("JOHN 3:16") == ("john", 3, [16])