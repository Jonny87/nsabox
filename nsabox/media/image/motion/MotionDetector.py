'''
Created on 10.08.2013

@author: Mischa
'''
from PIL import Image
from StringIO import StringIO
import subprocess

class MotionDetector(object):
    '''
    classdocs
    '''

    def __init__(self, threshold, sensitivity):
        '''
        Constructor
        '''
        # Motion detection settings:
        # Threshold (how much a pixel has to change by to be marked as "changed")
        # Sensitivity (how many changed pixels before capturing an image)
        # ForceCapture (whether to force an image to be captured every forceCaptureTime seconds)        
        self.__threshold = threshold
        self.__sensitivity = sensitivity
        self.__threshold = 20
        self.__sensitivity = 20
        '''
        self.forceCapture = True
        self.forceCaptureTime = 60 * 60 # Once an hour
            
        # File settings
        self.saveWidth = 1280
        self.saveHeight = 960
        
        self.diskSpaceToReserve = 40 * 1024 * 1024 # Keep 40 mb free on disk
        '''
        
    def recognizeMotion(self, image1, image2):
        motionDetected = False
        
        buffer1 = image1.load()
        buffer2 = image2.load()
        
        # Count changed pixels
        changedPixels = 0
        for x in xrange(0, 100):
            for y in xrange(0, 75):
                # Just check green channel as it's the highest quality channel
                pixdiff = abs(buffer1[x,y][1] - buffer2[x,y][1])
                if pixdiff > self.threshold:
                    changedPixels += 1
    
        '''
        # Check force capture
        if self.forceCapture:
            if time.time() - lastCapture > self.forceCaptureTime:
                changedPixels = self.sensitivity + 1
        '''
                    
        # Save an image if pixels changed
        if changedPixels > self.sensitivity:
            # lastCapture = time.time()
            motionDetected = True
            # self.__saveImage(self.saveWidth, self.saveHeight, self.diskSpaceToReserve)
        
        return motionDetected
        
    # Capture a small test image (for motion detection)
    def captureTestImage(self):
        command = "raspistill -w %s -h %s -t 0 -e bmp -o -" % (100, 75)
        imageData = StringIO()
        imageData.write(subprocess.check_output(command, shell=True))
        imageData.seek(0)
        image = Image.open(imageData)
        imageData.close()
        return image
    
    '''
    # Keep free space above given level
    def __keepDiskSpaceFree(self, bytesToReserve):
        if (self.__getFreeSpace() < bytesToReserve):
            for filename in sorted(os.listdir(".")):
                if filename.startswith("capture") and filename.endswith(".jpg"):
                    os.remove(filename)
                    print "Deleted %s to avoid filling disk" % filename
                    if (self.__getFreeSpace() > bytesToReserve):
                        return
    
    # Get available disk space
    def __getFreeSpace(self):
        st = os.statvfs(".")
        du = st.f_bavail * st.f_frsize
        return du
    ''' 