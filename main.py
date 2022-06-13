from numpy import arange


class TestVarriables:
    numberOfTest = 0
    TYPE_ERROR = "Значения диапазона должны представлять из себя число."
    RANGE_ERROR = "Неверно задан диапазон."



def LAB3_VAR2_5(start, stop, step):
    if type(start) != int and type(start) != float:
        return TestVarriables.TYPE_ERROR

    if type(stop) != int and type(stop) != float:
        return TestVarriables.TYPE_ERROR

    if type(step) != int and type(step) != float:
        return TestVarriables.TYPE_ERROR

    values = []
    for i in arange(start, stop, step):
        if (i == 0):
            values.append("ZeroDivision")
        else:
            values.append(f(i))

    if values == []:
        return TestVarriables.RANGE_ERROR

    return values


def TEST_LAB3_VAR2_5(result, expectedResult):
    TestVarriables.numberOfTest += 1
    if (result == expectedResult):
        print("Тест " + str(TestVarriables.numberOfTest) + " пройден")
    else:
        print("Тест " + str(TestVarriables.numberOfTest) + " не пройден")


# int
TEST_LAB3_VAR2_5(LAB3_VAR2_5(-10, 10, 2),
                 [7.01, 7.015625, 7.027777777777778, 7.0625, 7.25, 'ZeroDivision', 7.25, 7.0625, 7.027777777777778,
                  7.015625])
TEST_LAB3_VAR2_5(LAB3_VAR2_5(10, -10, -2),
                 [7.01, 7.015625, 7.027777777777778, 7.0625, 7.25, 'ZeroDivision', 7.25, 7.0625, 7.027777777777778,
                  7.015625])
TEST_LAB3_VAR2_5(LAB3_VAR2_5(10, -10, 2), TestVarriables.RANGE_ERROR)
TEST_LAB3_VAR2_5(LAB3_VAR2_5(-10, 10, -2), TestVarriables.RANGE_ERROR)

# string
TEST_LAB3_VAR2_5(LAB3_VAR2_5("-10", 10, 1), TestVarriables.TYPE_ERROR)
TEST_LAB3_VAR2_5(LAB3_VAR2_5(10, "-10", 1), TestVarriables.TYPE_ERROR)
TEST_LAB3_VAR2_5(LAB3_VAR2_5(10, -10, "1"), TestVarriables.TYPE_ERROR)

# float
TEST_LAB3_VAR2_5(LAB3_VAR2_5(-10.1, 10, 4),
                 [7.009802960494069, 7.026874496103198, 7.226757369614512, 7.2770083102493075, 7.028727377190463,
                  7.010203040506071])
TEST_LAB3_VAR2_5(LAB3_VAR2_5(-10, 10.1, 3), [7.01, 7.020408163265306, 7.0625, 8.0, 7.25, 7.04, 7.015625])
TEST_LAB3_VAR2_5(LAB3_VAR2_5(-10, 10, 3.1),
                 [7.01, 7.021003990758244, 7.069252077562327, 9.040816326530607, 7.173611111111112, 7.033057851239669,
                  7.013520822065981])
TEST_LAB3_VAR2_5(LAB3_VAR2_5(-11.1, 12.1, 4.1),
                 [7.008116224332441, 7.020408163265306, 7.118906064209274, 7.6944444444444455, 7.03559985760057,
                  7.011317338162065])

# bool
TEST_LAB3_VAR2_5(LAB3_VAR2_5(10, -10, False), TestVarriables.TYPE_ERROR)
TEST_LAB3_VAR2_5(LAB3_VAR2_5(10, True, -1), TestVarriables.TYPE_ERROR)
TEST_LAB3_VAR2_5(LAB3_VAR2_5(False, -10, -1), TestVarriables.TYPE_ERROR)

# List
TEST_LAB3_VAR2_5(LAB3_VAR2_5([1, 2, 3], -10, -1), TestVarriables.TYPE_ERROR)

# dict
TEST_LAB3_VAR2_5(LAB3_VAR2_5({1: "1"}, -10, -1), TestVarriables.TYPE_ERROR)

# tuple
TEST_LAB3_VAR2_5(LAB3_VAR2_5((1, 1), -10, -1), TestVarriables.TYPE_ERROR)

# range
TEST_LAB3_VAR2_5(LAB3_VAR2_5(range(1, 2), -10, -1), TestVarriables.TYPE_ERROR)

# set
TEST_LAB3_VAR2_5(LAB3_VAR2_5({1, 2}, -10, -1), TestVarriables.TYPE_ERROR)
