from typing import Union


# TODO Написать 3 класса с документацией и аннотацией типов


class Saw:
    def __init__(self, size: Union[float, int], sharpness: Union[int, float]):
        """
        Creates a saw with length measured in mm and sharpness parameter taking a value from 0 to 1
        :param size: saw size in mm
        :param sharpness: saw sharpness taking a value from 0 to 1
        Examples:
        >>> saw = Saw(150, 1)
        """
        """
        TEST UNIT:
        ~~~~~~~~~~
            Here the input parameters are checked
        """
        if not isinstance(size, (int, float)):
            raise TypeError(f"size - {size} must be int or float")

        if not size > 0:
            raise TypeError(f"size - {size} must be positive value")

        if not isinstance(sharpness, (int, float)):
            raise TypeError(f"sharpness - {sharpness} must be int or float")

        if not 0 <= sharpness <= 1:
            raise TypeError(f"sharpness - {sharpness} must take a value from 0 to 1")

        self.SIZE = size
        self.SHARPNESS = sharpness

    def sharpen(self, sharpening_stage: float) -> None:
        """
        Changes the sharpening stage of a saw.
        :return: None
        Examples:
        >>> saw = Saw(200, 0.2)
        >>> saw.sharpen(0.5)
        Your saw was sharpened to stage 0.5
        """

        if not isinstance(sharpening_stage, float):
            raise TypeError(f"sharpening stage - {sharpening_stage} must be float")

        if not self.SHARPNESS < sharpening_stage < 1:
            raise TypeError(f"sharpening stage - {sharpening_stage} must take a value from actual sharpness to 1")

        ...
        return print(f'Your saw was sharpened to stage {sharpening_stage}')

    def check_sawing_possibility(self, width: Union[float, int], elasticity: Union[float, int]) -> None:
        """
        Checks the possibility of sawing the material with actual saw
        :param width: The width of material in mm
        :param elasticity: The elasticity of material in range (0, 1000] GPa
        :return: None
         Examples:
        >>> saw = Saw(147, 0.64)
        >>> saw.check_sawing_possibility(35, 57)
        """
        if not isinstance(width, (int, float)):
            raise TypeError(f"width - {width} must be int or float")

        if not isinstance(elasticity, (int, float)):
            raise TypeError(f"elasticity - {elasticity} must be int or float")

        if not width > 0:
            raise TypeError(f"width - {width} must be positive value")

        if not 0 < elasticity < 1000:
            raise TypeError(f"elasticity - {elasticity} must be in range (0, 1000] GPa")

        ...


class Drill:
    def __init__(self, voltage: int, chuck_diameter: Union[int, float], bit_diameter: Union[int, float]):
        """
        Creates a drill with voltage measured in V, chuck diameter taking a value from 1 to 20 mm and bit diameter in mm
        :param voltage: drill voltage in V
        :param chuck_diameter: drill chuck diameter taking a value from 1 to 20
        :param bit_diameter: drill bit diameter in mm
        Examples:
        >>> drill = Drill(12,15,4)
        """
        """
        TEST UNIT:
        ~~~~~~~~~~
            Here the input parameters are checked
        """
        if not isinstance(voltage, int):
            raise TypeError(f"voltage - {voltage} must be int")

        if not voltage > 0:
            raise TypeError(f"voltage - {voltage} must be positive value")

        if not isinstance(chuck_diameter, (int, float)):
            raise TypeError(f"chuck diameter - {chuck_diameter} must be int or float")

        if not 1 <= chuck_diameter <= 20:
            raise TypeError(f"chuck diameter - {chuck_diameter} must take a value from 1 to 20")

        if not isinstance(bit_diameter, (int, float)):
            raise TypeError(f"bit diameter - {bit_diameter} must be int or float")

        if not 0.1 <= bit_diameter <= chuck_diameter:
            raise TypeError(f"bit diameter - {bit_diameter} must take a value from 0.1 to chuck diameter")

        self.VOLTAGE = voltage
        self.CHUCK_DIAMETER = chuck_diameter
        self.BIT_DIAMETER = bit_diameter

    def change_drill_bit(self, new_bit_diameter: Union[int, float]) -> None:
        """
        Changes the drill bit.
        :return: None
        Examples:
        >>> drill = Drill(18,10,2)
        >>> drill.change_drill_bit(5)
        You have changed the drill bit diameter to 5 mm
        """

        if not isinstance(new_bit_diameter, Union[int, float]):
            raise TypeError(f"new bit diameter - {new_bit_diameter} must be int or float")

        if not 0.1 <= new_bit_diameter <= self.CHUCK_DIAMETER:
            raise TypeError(f"new bit diameter - {new_bit_diameter} must take a value from 0.1 to drill chuck diameter")

        ...
        return print(f'You have changed the drill bit diameter to {new_bit_diameter} mm')

    def check_drilling_possibility(self, hole_diameter: Union[float, int], hardness: Union[float, int]) -> None:
        """
        Checks the possibility of drilling a hole in the material with actual drill and drill bit
        :param hole_diameter: The diameter of hole in mm
        :param hardness: The hardness of material in range (0, 1000] HB
        :return: None
         Examples:
        >>> drill = Drill(14,12,6)
        >>> drill.check_drilling_possibility(6, 400)
        """
        if not isinstance(hole_diameter, (int, float)):
            raise TypeError(f"hole diameter - {hole_diameter} must be int or float")

        if not isinstance(hardness, (int, float)):
            raise TypeError(f"hardness - {hardness} must be int or float")

        if not hole_diameter > 0:
            raise TypeError(f"hole diameter - {hole_diameter} must be positive value")

        if not 0 < hardness <= 1000:
            raise TypeError(f"hardness - {hardness} must be in range (0, 1000] GPa")

        ...


class WoodenPlank:
    def __init__(self, length: Union[int, float], wideness: Union[int, float], height: Union[int, float],
                 elasticity: Union[int, float], hardness: Union[int, float]):
        """
        Creates a wooden plank with length, wideness and heigth measured in mm, elasticity in range (0, 1000] GPa and
        hardness in range (0, 1000] HB
        :param length: length of the wooden plank in mm
        :param wideness: wideness of the wooden plank in mm
        :param height: heigth of the wooden plank in mm
        :param elasticity: elasticity of the wooden plank in range (0, 1000] GPa
        :param hardness: hardness of the wooden plank in range (0, 1000] HB
        Examples:
        >>> wooden_plank = WoodenPlank(1200,150,40,400,240)
        """
        """
        TEST UNIT:
        ~~~~~~~~~~
            Here the input parameters are checked
        """
        if not isinstance(wideness, (int, float)):
            raise TypeError(f"wideness - {wideness} must be int or float")

        if not isinstance(length, (int, float)):
            raise TypeError(f"length - {length} must be int or float")

        if not isinstance(height, (int, float)):
            raise TypeError(f"heigth - {height} must be int or float")

        if not wideness > 0:
            raise TypeError(f"wideness - {wideness} must be positive value")

        if not length > 0:
            raise TypeError(f"length - {length} must be positive value")

        if not height > 0:
            raise TypeError(f"heigth - {height} must be positive value")

        if not isinstance(hardness, (int, float)):
            raise TypeError(f"hardness - {hardness} must be int or float")

        if not 0 < hardness <= 1000:
            raise TypeError(f"hardness - {hardness} must be in range (0, 1000] GPa")

        if not isinstance(elasticity, (int, float)):
            raise TypeError(f"elasticity - {elasticity} must be int or float")

        if not 0 < elasticity < 1000:
            raise TypeError(f"elasticity - {elasticity} must be in range (0, 1000] GPa")

        self.LENGTH = length
        self.WIDENESS = wideness
        self.HEIGHT = height
        self.ELASTICITY = elasticity
        self.HARDNESS = hardness

    def check_sawing_possibility(self, actual_saw: Saw) -> None:
        """
        Checking the sawing possibility with actual saw.
        :param actual_saw: Actual saw
        :return: None
        Examples:
        >>> WoodenPlank.check_sawing_possibility(WoodenPlank(1200,150,40,400,240), Saw(350, 0.78))
        """

        if not isinstance(actual_saw, Saw):
            raise TypeError(f"actual_saw - {actual_saw} must be Saw")

        ...

    def check_drilling_possibility(self, actual_drill: Drill) -> None:
        """
        Checks the drilling possibility with actual drill
        :param actual_drill: actual drill
        :return: None
        Examples:
        >>> WoodenPlank.check_drilling_possibility(WoodenPlank(1200,150,40,400,240), Drill(12, 20, 8))
        """
        if not isinstance(actual_drill, Drill):
            raise TypeError(f"actual_drill - {actual_drill} must be Drill")

        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    import doctest

    doctest.testmod()
