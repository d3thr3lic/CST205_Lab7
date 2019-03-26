##Lab #7
##Mitchell and Nicholas Saunders

import os #to allow access to os.path.abspath(__file__) and os.path.dirname

##warmup for lab 7
  
def snowmanInDesert():
  pic = background = makePicture(getMediaPath() + "Desert_photo.jpg")
  pixels = getPixels(pic)
  x =  400 #position of snowman
  y =  400
  diameter_x = 100 #size of snowman based on headsize
  diameter_y = 100
  addArcFilled(pic,x,y,diameter_x,diameter_y,0,360,white) #Top
  addArcFilled(pic,x-(diameter_x/2),y+90,diameter_x*2,diameter_y*2,0,360,white) #Middle
  addArcFilled(pic,x-diameter_x,y+250,diameter_x*3,diameter_y*3,0,360,white) #Bottom
  
  writePictureTo(pic, getMediaPath() + "snowmanInDesert.jpg")
  repaint(pic)
  


def makeCard():
  #calls udf (user defined function) that will use setMediaPath() to define the working directory for later use
  setMediaPathToCurrentDir()
  
  background = makePicture(getMediaPath() + "Ireland.jpg")
  potOfGold = makePicture(getMediaPath() + "pot_of_gold.png")
  cornerDecor = makePicture(getMediaPath() + "corner_decor.png")
  
  card = pyCopyIgnoreColor(shrinkPic(potOfGold), background, 1019, 1069, makeColor(255,0,0))
  card = pyCopyIgnoreColor(cornerDecor, background, 0, 0, makeColor(255,0,0))
  card = pyCopyIgnoreColor(horiFlip(cornerDecor), background, 2003, 0, makeColor(255,0,0))
  card = pyCopyIgnoreColor(vertFlip(horiFlip(cornerDecor)), background, 2003, 1067, makeColor(255,0,0))
  card = pyCopyIgnoreColor(vertFlip(cornerDecor), background, 0, 1067, makeColor(255,0,0))
  
  textStyle = makeStyle(serif, bold, 85)
  addTextWithStyle(card, 500, 500, "Happy St. Patrick's Day Mom and Dad!", textStyle, makeColor(0, 180, 0))
  textStyle = makeStyle(serif, bold, 60)
  addTextWithStyle(card, 550, 950, "-Your sons", textStyle, makeColor(0, 180, 0))
      
  #repaint(card)
  print getMediaPath()
  writePictureTo(card, getMediaPath() + "card.jpg")

def pyCopyIgnoreColor(source, target, targetX, targetY, colorToIgnore):
  sWidth = getWidth(source)
  sHeight = getHeight(source)
  tWidth = getWidth(target)
  tHeight = getHeight(target)
  
  for x in range(0, sWidth):
    for y in range(0, sHeight):
      oldPix = getPixel(source, x, y)
      newX = x + targetX
      newY = y + targetY
      #this will allow me to have some of the photos leave the frame a little bit without crashing
      if (newX < tWidth) and (newX >= 0) and (newY < tHeight) and (newY >= 0):
        if getColor(oldPix) != colorToIgnore:
          newPix = getPixel(target, newX, newY)
          setColor(newPix, getColor(oldPix))
  return target
  
def setMediaPathToCurrentDir():
  fullPathToFile = os.path.abspath(__file__)
  if fullPathToFile.startswith('/'):
    setMediaPath(os.path.dirname(fullPathToFile))
  else:
    setMediaPath(os.path.dirname(fullPathToFile) + '\\')

def horiFlip(pic):
  #get dimensions of photo
  width = getWidth(pic)
  height = getHeight(pic)
  #make new photo
  canvas = makeEmptyPicture(width, height)

  #do the actual copy work
  for x in range(0, width):
    for y in range(0, height):
      oldPix = getPixel(pic, x, y)
      newPix = getPixel(canvas, x, y)
      mirrorPix = getPixel(canvas, (width - (x + 1)), y)
      setColor(mirrorPix, getColor(oldPix))
  return canvas

def vertFlip(pic):
  #get dimensions of photo
  width = getWidth(pic)
  height = getHeight(pic)
  #make new photo
  canvas = makeEmptyPicture(width, height)

  #do the actual copy work
  for x in range(0, width):
    for y in range(0, height):
      oldPix = getPixel(pic, x, y)
      newPix = getPixel(canvas, x, y)
      mirrorPix = getPixel(canvas, x, (height - 1) - y)
      setColor(mirrorPix, getColor(oldPix))
  return canvas
  
def shrinkPic(pic):
  #get dimensions of photo
  width = getWidth(pic)
  height = getHeight(pic)
  #make new photo
  canvas = makeEmptyPicture(width/2, height/2)
  for x in range(0, width, 2):
    for y in range(0, height, 2):
      oldPix = getPixel(pic, x, y)
      newPix = getPixel(canvas, x/2, y/2)
      setColor(newPix, getColor(oldPix))
  return canvas          