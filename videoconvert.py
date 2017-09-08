import slitheringffmpeg

Video = slitheringffmpeg.SlitheringFFMPEG()
Video.Video = "BiddleHouse.mpe"
Video.VideoPath = "/home/nate/CMeLocal/"
Video.GetInfo()
Video.DisplayInfo()
Video.SuggestedHeight = 600
Video.SuggestedWidth = 800
Video.TargetThumbnailHeight = 75
Video.TargetThumbnailWidth = 100
Video.FixedScale()
Video.TargetBits()
Video.TargetVideo = "BiddleHouse"
Video.TargetVideoPath = "/home/nate/Videos/"
Video.VideoFlvCommand()
Video.VideoMp4Command()
Video.VideoOgvCommand()
Video.AnimatedGifCommand()
#Video.Test()

