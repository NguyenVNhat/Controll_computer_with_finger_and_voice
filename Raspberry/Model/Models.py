import Sound,GenerateNewDataWebsite,GenerateNewDataCMD

def Hello():
    Sound.hello()
def GetAudio():
    return Sound.get_audio()
def AddnewWebsiteData(Website):
    GenerateNewDataWebsite.addNewWebsiteRequest(Website)
def AddnewCMDData(CMD):
    GenerateNewDataCMD.addNewCMDRequest(CMD)

