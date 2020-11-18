from cis301.phonebill.phonebill_dumper import PhoneBillDumper


class TextDumper(PhoneBillDumper):
    pass

    """
        Classes that implement this interface read some source and from it create a phone bill.
        """

    @classmethod
    def __subclasshook__(cls, subclass):
        """
        verifies if the implementing class has implemented all abstract methods
        """
        return (hasattr(subclass, 'dump') and
                callable(subclass.dump) or
                NotImplemented)

    T = TypeVar('T', bounds=AbstractPhoneBill)

    @abc.abstractmethod
    def parse(self) -> AbstractPhoneBill:
        """
        Parses some source and returns a phone bill

        Raises:
            raises I/O exception when accessing an invalid file
        """
        pass