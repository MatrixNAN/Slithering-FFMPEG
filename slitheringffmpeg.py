import commands
import re
import os
#import subprocess

class SlitheringFFMPEG():
    def __init__(self):
        self.Ar = 0
        self.Ab = ""
        self.Vb = 0
        self.Duration = ""
        self.Start = 0.0
        self.Fps = 0
        self.AudioFormat = ""
        self.VideoFormat = ""
        self.ResolutionHeight = 0
        self.ResolutionWidth = 0
        self.Video = ""
        self.VideoPath = ""
        self.FfmpegCommand = "ffmpeg"
        self.OgvCommand = "ffmpeg2theora"
        self.HandBrakeCliCommand = "HandBrakeCLI"
        self.GifsicleCommand = "gifsicle"
        self.SuggestedHeight = 0
        self.SuggestedWidth = 0
        self.TargetHeight = 0
        self.TargetWidth = 0
        self.TargetVb = 0
        self.TargetAb = ""
        self.TargetAr = 0
        self.TargetDuration = 60
        self.TargetVideo = ""
        self.TargetVideoAddon = ""
        self.TargetVideoPath = ""
        self.TargetVideoExtension = ""
        self.TargetThumbnailHeight = 0
        self.TargetThumbnailWidth = 0
        self.TestOgv = ""
        self.TestFlv = ""
        self.TestMp4 = ""
        self.TestGif = ""
        self.TestVideoImage = ""
        return
    
    def ArCommand(self):
        ar_command = self.FfmpegCommand+" -i "+self.VideoPath+self.Video+" 2>&1 | perl -lane 'print $1 if /(\d+ Hz)/'"
        ar_number_command = " | perl -lane 'print $1 if /(\d+)/'"
        AR = commands.getoutput(ar_command+ar_number_command)
        return AR
    
    def AbCommand(self):
        ab_command = self.FfmpegCommand+" -i "+self.VideoPath+self.Video+" 2>&1 | perl -lane 'print $1 if /(s\d+)/'"
        AB = commands.getoutput(ab_command)
        return AB
    
    def AudioFormatCommand(self):
        audioformat_command = self.FfmpegCommand+" -i "+self.VideoPath+self.Video+" 2>&1 | perl -lane 'print $1 if /(Audio: \w+)/'"
        audioformat_only_command = " | perl -lane 'print $1 if /( \w+)/' | perl -lane 'print $1 if /(\w+)/'"
        audioformat = commands.getoutput(audioformat_command+audioformat_only_command)
        return audioformat
    
    def ResolutionCommand(self):
        resolution_command = self.FfmpegCommand+" -i "+self.VideoPath+self.Video+" 2>&1 | perl -lane 'print $1 if /(\d+x\d+)/'"
        resolution = commands.getoutput(resolution_command)
        return resolution
    
    def ResolutionHeightCommand(self):
        resolution_command = self.FfmpegCommand+" -i "+self.VideoPath+self.Video+" 2>&1 | perl -lane 'print $1 if /(, \d+x\d+)/'"
        resolution_height_command = " | perl -lane 'print $1 if /(x\d+)/' | perl -lane 'print $1 if /(\d+)/' | perl -lane 'print $1 if /(\d+)/'"
        resolution_height = commands.getoutput(resolution_command+resolution_height_command)
        return resolution_height
    
    def ResolutionWidthCommand(self):
        resolution_command = self.FfmpegCommand+" -i "+self.VideoPath+self.Video+" 2>&1 | perl -lane 'print $1 if /(, \d+x\d+)/'"
        resolution_width_command = " | perl -lane 'print $1 if /(\d+x)/' | perl -lane 'print $1 if /(\d+)/'"
        resolution_width = commands.getoutput(resolution_command+resolution_width_command)
        return resolution_width
    
    def DurationCommand(self):
        duration_command = self.FfmpegCommand+" -i "+self.VideoPath+self.Video+" 2>&1 | perl -lane 'print $1 if /(Duration: \d+:\d+:\d+.\d+)/'"
        duration_timeonly_command = " | perl -lane 'print $1 if /(\d+:\d+:\d+.\d+)/'"
        duration = commands.getoutput(duration_command+duration_timeonly_command) 
        return duration
    
    def StartTimeCommand(self):
        starttime_command = self.FfmpegCommand+" -i "+self.VideoPath+self.Video+" 2>&1 | perl -lane 'print $1 if /(start: \d+.\d+)/'"
        starttime_number_command = " | perl -lane 'print $1 if /(\d+.\d+)/'"
        starttime = commands.getoutput(starttime_command+starttime_number_command)
        return starttime
    
    def FpsCommand(self):
        fps_command = self.FfmpegCommand+" -i "+self.VideoPath+self.Video+" 2>&1 | perl -lane 'print $1 if /(\d+.\d+ fps)/'"
        fps_number_command = " | perl -lane 'print $1 if /(\d+)/'"
        fps = commands.getoutput(fps_command+fps_number_command)
        if (fps == ""):
            fps_command = self.FfmpegCommand+" -i "+self.VideoPath+self.Video+" 2>&1 | perl -lane 'print $1 if /(\d+ fps)/'"
        fps = commands.getoutput(fps_command+fps_number_command)
        return fps
    
    def VideoFormatCommand(self):
        video_format_command = self.FfmpegCommand+" -i "+self.VideoPath+self.Video+" 2>&1 | perl -lane 'print $1 if /(major_brand     : \w+)/'"
        video_format_only_command = " | perl -lane 'print $1 if /( \w+)/' | perl -lane 'print $1 if /(\w+)/'"
        video_format = commands.getoutput(video_format_command+video_format_only_command)
        return video_format
    
    def VideoBitRateCommand(self):
        video_bit_rate_command = self.FfmpegCommand+" -i "+self.VideoPath+self.Video+" 2>&1 | perl -lane 'print $1 if /(bitrate: \d+)/'"
        video_bit_rate_number_command = " | perl -lane 'print $1 if /(\d+)/'"
        video_bit_rate = commands.getoutput(video_bit_rate_command+video_bit_rate_number_command)
        return video_bit_rate
    
    def GetInfo(self):
        self.Ar = int(self.ArCommand())
        self.Ab = self.AbCommand()
        self.Vb = int(self.VideoBitRateCommand())
        self.AudioFormat = self.AudioFormatCommand()
        self.VideoFormat = self.VideoFormatCommand()
        self.Duration = self.DurationCommand()
        self.Start = float(self.StartTimeCommand())
        self.Fps = int(self.FpsCommand())
        self.ResolutionHeight = int(self.ResolutionHeightCommand())
        self.ResolutionWidth = int(self.ResolutionWidthCommand())
        return
    
    def DisplayInfo(self):
        print "Audio Rate: "+str(self.Ar)+" Hz"
        print "Audio Bits: "+self.Ab
        print "Audio Format: "+self.AudioFormat
        print "Video Format: "+self.VideoFormat
        print "Duration: "+self.Duration
        print "Start Time: "+str(self.Start)
        print "Frames Per Second: "+str(self.Fps)+" fps"
        print "Resolution: "+str(self.ResolutionWidth)+"x"+str(self.ResolutionHeight)
        print "Video: "+self.Video
        print "Video Bit Rate: "+str(self.Vb)
        #print commands.getoutput(self.FfmpegCommand+" -i "+self.Video)
        return
    
    def ConvertMultipleTwo (self, value):
        if (value % 2):
            value - 1
        else:
            value
        return value
    
    def GetNewHeight(self):
        if (self.ResolutionWidth > self.SuggestedWidth and self.ResolutionHeight > self.SuggestedHeight):	
            tempWidthRatio = float(self.ResolutionWidth) / float(self.SuggestedWidth)
            tempHeight = float(self.ResolutionHeight) / tempWidthRatio
            tempHeightFinal = self.ConvertMultipleTwo(tempHeight)
            
            if (tempHeightFinal < self.SuggestedHeight):
                self.TargetHeight = float(tempHeightFinal)
                return
            elif (tempHeightFinal > self.SuggestedHeight):
                tempHeightRatio = float(self.ResolutionHeight) / float(self.SuggestedHeight)
                tempWidth = float(self.ResolutionHeight) / tempHeightRatio	
                tempWidthFinal = self.ConvertMultipleTwo(tempHeight)
                
                if (tempWidthFinal < self.SuggestedWidth):
                    self.TargetHeight = float(self.SuggestedHeight)
                    return
        elif (self.ResolutionWidth < self.SuggestedWidth and self.ResolutionHeight > self.SuggestedHeight):
            self.TargetHeight = float(self.SuggestedHeight)
            return
        elif (self.ResolutionWidth > self.SuggestedWidth and self.ResolutionHeight < self.SuggestedHeight):
            tempWidthRatio = float(self.ResolutionWidth) / float(self.SuggestedWidth)
            tempHeight = float(self.ResolutionWidth) / tempWidthRatio		
            tempHeightFinal = self.ConvertMultipleTwo(tempHeight)
            self.TargetHeight = float(tempHeightFinal)
            return
        elif (self.ResolutionWidth < self.SuggestedWidth and self.ResolutionHeight < self.SuggestedHeight):
            self.TargetHeight = float(self.ResolutionHeight)
            return
    
    def GetNewWidth (self):
        tempHeightRatio = float(self.ConvertMultipleTwo(self.ResolutionWidth)) / float(self.ResolutionHeight)
        tempWidth = float(self.ConvertMultipleTwo(self.TargetHeight)) * tempHeightRatio
        tempWidthFinal = self.ConvertMultipleTwo(tempWidth)

        if (self.TargetWidth < tempWidthFinal):
            self.TargetWidth = tempWidthFinal
        return
    
    def FixedScale(self):
        self.GetNewHeight()
        self.GetNewWidth()
        return
    
    def TargetBits(self):
        if (self.Vb < 1):
            self.TargetVb = 600
        else:
            self.TargetVb = self.Vb
            
        if (self.Ar < 1):
            self.TargetAr = 44100
        elif (self.Ar != 11025 or self.Ar != 22050 or self.Ar != 44100):
            if (self.Ar < 11025):
                self.TargetAr = 11025
            elif (self.Ar > 11025 and self.Ar < 22050):
                self.TargetAr = 22050
            elif (self.Ar > 22050):
                self.TargetAr = 44100
        else:
            self.TargetAr = self.Ar
        
        if (self.Ab == ""):
            self.TargetAb = "16"
            print "Audio Bits: "+str(self.TargetAb)
        else:
            self.TargetAb = self.Ab
        return
    
    def VideoFlvCommand(self):
        self.TargetVideoExtension = ".flv"
        self.TargetVideoAddon = ""
        self.GetTargetVideo()
        video_flv_command = self.FfmpegCommand+" -t "+str(self.TargetDuration)+" -i "+self.VideoPath+self.Video+" -ar "+str(self.TargetAr)+" -ab "+self.TargetAb+" -f flv -s "+str(int(self.TargetWidth))+"x"+str(int(self.TargetHeight))+" "+self.TargetVideoPath+self.TargetVideo+self.TargetVideoAddon+self.TargetVideoExtension
        print video_flv_command
        self.TestFlv = commands.getoutput(video_flv_command)
        return
    
    def VideoMp4Command(self):
        self.TargetVideoExtension = ".mp4"
        self.TargetVideoAddon = ""
        self.GetTargetVideo()
        video_mp4_command = self.HandBrakeCliCommand+' --preset "iPhone & iPod Touch" --width '+str(int(self.TargetWidth))+' --height '+str(int(self.TargetHeight))+' --vb '+str(self.TargetVb)+' --two-pass --turbo --input '+self.VideoPath+self.Video+' --output '+self.TargetVideoPath+self.TargetVideo+self.TargetVideoAddon+self.TargetVideoExtension
        print video_mp4_command
        self.TestMp4 = commands.getoutput(video_mp4_command)
        return
    
    def VideoOgvCommand(self):
        self.TargetVideoExtension = ".ogv"
        self.TargetVideoAddon = ""
        self.GetTargetVideo()
        video_Ogv_command = self.OgvCommand+" --speedlevel 0 --framerate "+str(self.Fps)+" --samplerate "+str(self.TargetAr)+" -s 0 -e "+str(self.TargetDuration)+" -x "+str(int(self.TargetWidth))+" -y "+str(int(self.TargetHeight))+" "+self.VideoPath+self.Video+" --output="+self.TargetVideoPath+self.TargetVideo+self.TargetVideoAddon+self.TargetVideoExtension
        print video_Ogv_command
        self.TestOgv = commands.getoutput(video_Ogv_command)
        return
    
    def AnimatedGifCommand(self):
        self.TargetVideoExtension = ".gif"
        self.TargetVideoAddon = ""
        self.GetTargetVideo()
        animated_gif_command = self.FfmpegCommand+" -t 5 -ss 00:00:03 -i "+self.VideoPath+self.Video+" -pix_fmt rgb24 -s "+str(int(self.TargetThumbnailWidth))+"x"+str(int(self.TargetThumbnailHeight))+" "+self.TargetVideoPath+self.TargetVideo+self.TargetVideoAddon+"Convert"+self.TargetVideoExtension
        animated_gif_video_command = self.GifsicleCommand+" "+self.TargetVideoPath+self.TargetVideo+self.TargetVideoAddon+"Convert"+self.TargetVideoExtension+" > "+self.TargetVideoPath+self.TargetVideo+self.TargetVideoExtension
        remove_animated_convert_command = "rm -f "+self.TargetVideoPath+self.TargetVideo+self.TargetVideoAddon+"Convert"+self.TargetVideoExtension
        print animated_gif_command
        self.TestGif = commands.getoutput(animated_gif_command)
        print animated_gif_video_command
        animated_gif_video = commands.getoutput(animated_gif_video_command)
        print remove_animated_convert_command
        remove_animated_convert = commands.getoutput(remove_animated_convert_command)
        return

    def VideoImageCommand(self):
        self.TargetVideoExtension = ".gif"
        self.TargetVideoAddon = "VideoImage"
        self.GetTargetVideo()
        animated_gif_command = self.FfmpegCommand+" -t 1 -ss 00:00:01 -i "+self.VideoPath+self.Video+" -pix_fmt rgb24 -s "+str(int(self.TargetWidth))+"x"+str(int(self.TargetHeight))+" "+self.TargetVideoPath+self.TargetVideo+self.TargetVideoAddon+self.TargetVideoExtension
        self.TestVideoImage = commands.getoutput(animated_gif_command)
        return

    def Test(self):
        print "OGV Video Conversion Test: "
        print self.TestOgv
        print
        print "FLV Video Conversion Test: "
        print self.TestFlv
        print
        print "MP4 Video Conversion Test: "
        print self.TestMp4
        print
        print "GIF Video Conversion Test: "
        print self.TestGif
        print
        print "Video Image Conversion Test: "
        print self.TestVideoImage
        print
        return

    def RemoveFlvVideo(self):
        self.TargetVideoExtension = ".flv"
        self.TargetVideoAddon = ""
        remove_flv_video_command = "rm -f "+self.TargetVideoPath+self.TargetVideo+self.TargetVideoAddon+self.TargetVideoExtension
        remove_flv_video = commands.getoutput(remove_flv_video_command)
        return
    
    def RemoveMp4Video(self):
        self.TargetVideoExtension = ".mp4"
        self.TargetVideoAddon = ""
        remove_mp4_video_command = "rm -f "+self.TargetVideoPath+self.TargetVideo+self.TargetVideoAddon+self.TargetVideoExtension
        remove_mp4_video = commands.getoutput(remove_mp4_video_command)
        return
    
    def RemoveOgvVideo(self):
        self.TargetVideoExtension = ".ogv"
        self.TargetVideoAddon = ""
        remove_ogv_video_command = "rm -f "+self.TargetVideoPath+self.TargetVideo+self.TargetVideoAddon+self.TargetVideoExtension
        remove_ogv_video = commands.getoutput(remove_ogv_video_command)
        return
    
    def RemoveGifVideo(self):
        self.TargetVideoExtension = ".gif"
        self.TargetVideoAddon = ""
        remove_gif_video_command = "rm -f "+self.TargetVideoPath+self.TargetVideo+self.TargetVideoAddon+self.TargetVideoExtension
        remove_gif_video = commands.getoutput(remove_gif_video_command)
        return

    def RemoveVideoImage(self):
        self.TargetVideoExtension = ".gif"
        self.TargetVideoAddon = "VideoImage"
        remove_gif_video_command = "rm -f "+self.TargetVideoPath+self.TargetVideo+self.TargetVideoAddon+self.TargetVideoExtension
        remove_gif_video = commands.getoutput(remove_gif_video_command)
        return

    def RemoveOriginalVideo(self):
        remove_original_video_command = "rm -f "+self.VideoPath+self.Video
        print "remove original video command = " + remove_original_video_command
        remove_original_video = commands.getoutput(remove_original_video_command)
        print remove_original_video_command 
        return
    
    def RemoveVideos(self):
        self.RemoveFlvVideo()
        self.RemoveMp4Video()
        self.RemoveOgvVideo()
        self.RemoveGifVideo()
        self.RemoveVideoImage()
        self.RemoveOriginalVideo()
        return
    
    def ExtractPath(self, videopath):
        self.VideoPath = os.path.dirname(videopath)
        return
    
    def ExtractFileName(self, videofile):
        self.Video = os.path.basename(videofile)
        return
    
    def GetTargetVideo(self):
    	self.TargetVideo = os.path.splitext(self.Video)[0]
        return
