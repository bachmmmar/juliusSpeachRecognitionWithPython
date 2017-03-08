
class ConfigEntry:
    def __init__(self, name, wordgroups, executable):
        self.name_ = name
        self.wordgroups_ = wordgroups
        self.executables_ = executable

    def getGroups(self):
        return self.wordgroups_

    def getExecutable(self):
        return self.executables_

    def getName(self):
        return self.name_