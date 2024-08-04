# -*- coding: utf-8 -*-
from assertpy import assert_that, fail

from coding_exercise.application.splitter import Splitter, CABLE_MAX_LENGTH, TIMES_MAX
from coding_exercise.domain.model.cable import Cable


def test_should_not_return_none_when_splitting_cable():
    assert_that(Splitter().split(Cable(10, "coconuts"), 1)).is_not_none()


def test_error_when_splitting_cable_none():
    try:
        Splitter().split(None, 1)
        fail("should have raised error")
    except ValueError as e:
        assert_that(str(e)).is_equal_to("cable cannot be None")


def test_error_when_splitting_times_none():
    try:
        Splitter().split(Cable(10, "coconuts"), None)
        fail("should have raised error")
    except ValueError as e:
        assert_that(str(e)).is_equal_to("times cannot be None")


def test_error_when_splitting_cable_type_incorrect():
    try:
        Splitter().split("cable", 1)
        fail("should have raised error")
    except ValueError as e:
        assert_that(str(e)).is_equal_to("cable must be of type Cable")


def test_error_when_splitting_times_type_incorrect():
    try:
        Splitter().split(Cable(10, "coconuts"), 2.5)
        fail("should have raised error")
    except ValueError as e:
        assert_that(str(e)).is_equal_to("times must be of type int")


def test_error_when_splitting_invalid_cable_length():
    try:
        Splitter().split(Cable(CABLE_MAX_LENGTH + 2, "coconuts"), 5)
        fail("should have raised error")
    except ValueError as e:
        assert_that(str(e)).is_equal_to(
            "Cable length must be greater than or equal "
            "to 2 and less than or equal to 1024"
        )


def test_error_when_splitting_invalid_num_times():
    try:
        Splitter().split(Cable(10, "coconuts"), TIMES_MAX + 2)
        fail("should have raised error")
    except ValueError as e:
        assert_that(str(e)).is_equal_to(
            "Number of times must be greater than or equal "
            "to 1 and less than or equal to 64"
        )


def test_split_10_length_cable_1_time():
    actual_result = Splitter().split(Cable(10, "coconuts"), 1)
    expected_result = [Cable(5, "coconuts-00"), Cable(5, "coconuts-01")]

    assert_that(actual_result).is_equal_to(expected_result)


def test_split_5_length_cable_2_times():
    actual_result = Splitter().split(Cable(5, "coconuts"), 2)
    expected_result = [
        Cable(1, "coconuts-00"),
        Cable(1, "coconuts-01"),
        Cable(1, "coconuts-02"),
        Cable(1, "coconuts-03"),
        Cable(1, "coconuts-04"),
    ]

    assert_that(actual_result).is_equal_to(expected_result)


def test_split_7_length_cable_2_times():
    actual_result = Splitter().split(Cable(7, "telephone"), 2)
    expected_result = [
        Cable(2, "telephone-00"),
        Cable(2, "telephone-01"),
        Cable(2, "telephone-02"),
        Cable(1, "telephone-03"),
    ]

    assert_that(actual_result).is_equal_to(expected_result)


def test_split_20_length_cable_3_times():
    actual_result = Splitter().split(Cable(20, "hfc"), 3)
    expected_result = [
        Cable(5, "hfc-00"),
        Cable(5, "hfc-01"),
        Cable(5, "hfc-02"),
        Cable(5, "hfc-03"),
    ]

    assert_that(actual_result).is_equal_to(expected_result)


def test_split_50_length_cable_10_times():
    actual_result = Splitter().split(Cable(50, "internet"), 10)
    expected_result = [
        Cable(4, "internet-00"),
        Cable(4, "internet-01"),
        Cable(4, "internet-02"),
        Cable(4, "internet-03"),
        Cable(4, "internet-04"),
        Cable(4, "internet-05"),
        Cable(4, "internet-06"),
        Cable(4, "internet-07"),
        Cable(4, "internet-08"),
        Cable(4, "internet-09"),
        Cable(4, "internet-10"),
        Cable(4, "internet-11"),
        Cable(2, "internet-12"),
    ]
    print("here")
    print(list(str(r) for r in expected_result))
    print(list(str(r) for r in actual_result))

    assert_that(actual_result).is_equal_to(expected_result)
