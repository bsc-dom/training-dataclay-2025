from dataclay import DataClayObject, activemethod

class Words(DataClayObject):
    words: list[str]
    raw_text: str

    def load_text(self, text: str):
        """Load text to be processed.
        
        Instead of passing text as parameter, this function may read a local file,
        or access a distributed storage, or connect to a dataset, retrieve a S3
        object, etc.
        """
        ...

    def split_and_sanitize(self) -> None:
        """Split the text into proper words, store them locally."""
        ...
    
    def count_words(self) -> dict[str, int]:
        """Count unique words."""
        ...
