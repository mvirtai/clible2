import httpx
from loguru import logger


def normalize_reference(reference: str) -> tuple[str, int, list[int]]:
    """Normalize reference to (book, chapter, verses).
    
    Normalizes:
    - Lowercase for consistency
    - Whitespace cleanup
    """
    # Puhdista välilyönnit ja muuta pieniksi kirjaimiksi
    reference = " ".join(reference.split()).lower()  # "Gen  1:1" -> "gen 1:1"
    
    # Erota kirja ja "luku:jakeet"
    parts = reference.rsplit(" ", 1)  # ["gen", "1:1"]
    if len(parts) != 2:
        raise ValueError(f"Invalid reference format: {reference}")
    
    book = parts[0]  # "gen"
    
    # Erota luku ja jakeet
    chapter_verse = parts[1].split(":", 1)  # ["1", "1"]
    if len(chapter_verse) != 2:
        raise ValueError(f"Invalid reference format: {reference}")
    
    chapter = int(chapter_verse[0])  # 1
    verse_str = chapter_verse[1].strip()  # "1"
    
    # Yksinkertaisin: vain ensimmäinen jae nyt
    verses = [int(verse_str)]  # [1]
    
    return book, chapter, verses