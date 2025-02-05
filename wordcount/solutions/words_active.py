from dataclay import DataClayObject, activemethod

class Words(DataClayObject):
    words: list[str]
    raw_text: str

    @activemethod
    def load_text(self, text: str):
        """Load text to be processed.
        
        Instead of passing text as parameter, this function may read a local file,
        or access a distributed storage, or connect to a dataset, retrieve a S3
        object, etc.
        """
        self.raw_text = text

    @activemethod
    def split_and_sanitize(self) -> None:
        """Split the text into proper words, store them locally."""
        self.words = []
        for item in self.raw_text.split():
            # Remove punctuation signs and make the word lowercase
            sanitized = item.strip('.,').lower()
            self.words.append(sanitized)
    
    @activemethod
    def count_words(self) -> dict[str, int]:
        """Count unique words."""
        result = dict()
        for word in self.words:
            if word in result:
                result[word] += 1
            else:
                result[word] = 1
        return result
