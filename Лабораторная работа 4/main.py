class ROD:
    """
    Class describing a refractive optical device
    """
    def __init__(self, name: str, spectrum_range: str, diameter: float, thickness: float):
        self.name = name
        self.spectrum_range = spectrum_range
        self.diameter = diameter
        self.thickness = thickness

    def __str__(self) -> str:
        """
        Returns the name and spectrum range of a refractive optical device
        :return: name, spectrum_range
        """
        return f"Name-{self.name}, Spectrum range-{self.spectrum_range}"

    def __repr__(self) -> str:
        """
        The method returns a string indicating how an instance of the ROD class can be initialized
        :return: a string indicating how an instance of the ROD class can be initialized
        """
        return f"{self.__class__.__name__}(name={self.name!r}, spectrum_range={self.spectrum_range!r}, " \
               f"diameter={self.diameter!r}, thickness={self.thickness!r} "

    def is_terahertz_device(self) -> bool:
        """
        The method checks whether a refractive optical device is a terahertz device
        :return: True if spectrum range is terahertz, otherwise return False
        """
        if self.spectrum_range == 'terahertz':
            return True
        else:
            return False


class FresnelLens(ROD):
    """
    Class describing a Fresnel Lens
    """
    def __init__(self, name: str, spectrum_range: str, diameter: float, thickness: float, focal_length: float):
        super().__init__(name, spectrum_range, diameter, thickness)
        self.focal_length = focal_length

    def __repr__(self):
        """
        The method returns a string indicating how an instance of the Fresnel Lens class can be initialized
        :return: a string indicating how an instance of the Fresnel Lens class can be initialized
        """
        return f"{self.__class__.__name__}(name={self.name!r}, spectrum_range={self.spectrum_range!r}, " \
               f"diameter={self.diameter!r}, thickness={self.thickness!r}, focal_length={self.focal_length!r}"


if __name__ == "__main__":
    # Write your solution here
    pass
