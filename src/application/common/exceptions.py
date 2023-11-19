class ApplicationException(Exception):
    @property
    def message(self) -> str:
        return "Application error occured"
