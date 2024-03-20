from constants import Constants


class Conversions:
    @staticmethod
    def WCpointToCCpoint(val):
        return int(val * (Constants.CharMapSize / Constants.WorldSize) + (Constants.CharMapSize / 2))

    @staticmethod
    def WClengthToCClength(val):
        return int(val * (Constants.CharMapSize / Constants.WorldSize))