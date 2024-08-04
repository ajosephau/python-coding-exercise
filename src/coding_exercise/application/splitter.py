# -*- coding: utf-8 -*-
from coding_exercise.domain.model.cable import Cable

# Can abstract these constants into a separate configuration file:
# kept in this file for simplicity
CABLE_MIN_LENGTH = 2
CABLE_MAX_LENGTH = 1024
TIMES_MIN = 1
TIMES_MAX = 64


class Splitter:
    def __validate(self, cable: Cable, times: int):
        """Validate that splitter parameters are correct

        Parameters
        ----------
        cable : @Cable, required
            cable object to be split (default is None)
        times : int, required
            the number of times (default is None)

        Raises
        ------
        ValueError
            If invalid parameters are passed.
        """

        # Check cable exists:
        if not cable:
            raise ValueError("cable cannot be None")

        # Check times exists:
        if not times:
            raise ValueError("times cannot be None")

        # Check cable type:
        if not isinstance(cable, Cable):
            raise ValueError("cable must be of type Cable")

        # Check times type:
        if not isinstance(times, int):
            raise ValueError("times must be of type int")

        # Valid minimum/maximum values for Cable.length
        if not (CABLE_MIN_LENGTH <= cable.length <= CABLE_MAX_LENGTH):
            raise ValueError(
                f"Cable length must be greater than or equal to {CABLE_MIN_LENGTH} "
                f"and less than or equal to {CABLE_MAX_LENGTH}"
            )

        # Valid minimum/maximum values for times
        if not (TIMES_MIN <= times <= TIMES_MAX):
            raise ValueError(
                f"Number of times must be greater than or equal to {TIMES_MIN} "
                f"and less than or equal to {TIMES_MAX}"
            )

        # valid configuration

    def split(self, cable: Cable, times: int) -> list[Cable]:
        """Split given cable

        Parameters
        ----------
        cable : @Cable, required
            cable object to be split (default is None)
        times : int, required
            the number of times (default is None)

        Raises
        ------
        ValueError
            If invalid parameters are passed.
        """

        self.__validate(cable, times)

        units = list(range(0, cable.length))
        split_cables = []
        split_cable_units = []
        split_cable_size = cable.length // (times + 1)

        # partition list by chunk size....
        for i in range(0, len(units), split_cable_size):
            split_cable_units.append(units[i : i + split_cable_size])

        # determine split cable by chunked size above
        for i, c in enumerate(split_cable_units):
            split_cables.append(Cable(len(c), f"{cable.name}-{str(i).zfill(2)}"))

        return split_cables
