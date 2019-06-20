import struct
import configparser

# Construction of the RGB triplet
# base on the triplet (y,m,n)
def hexformat(configmenu):
    red = configparser.countconfig('y',configmenu)%255
    green = configparser.countconfig('m',configmenu)%255
    blue = configparser.countconfig('n',configmenu)%255
    res = '%02x%02x%02x' % (red,green,blue)
    return res

# Add some modification on the hexa color
def modifycolor(rgbstr,int):
    # Reconstructrion of RGB triplet
    rgbtriplet = struct.unpack('BBB',bytes.fromhex(rgbstr))
    red = rgbtriplet[0]
    green = rgbtriplet[1]
    blue = rgbtriplet[2]

    if red > green and red > blue:
        if red <= 190:
            red = (red+65)
        if (green+int)<151:
            green = (green+int)%150
        if (blue+int)<231:
            blue = (blue+int+20)%230

    elif green > blue:
        if green<=200:
            green = (green+55)
        if (blue+int)<231:
            blue = (blue+int)%230
        if (red+int)<151:
            red = (red+int)%150

    else:
        if blue<=200:
            blue = (blue+55)
        if (green+int)<201: green = (green+int)

        if (red+int)<201:
            red = (red+int)%200

    res = '%02x%02x%02x' % (abs(red),abs(green),abs(blue))
    return res

# Reduce shadow of the hexa color
def reflectioncolor(rgbstr):
    # Reconstructrion of RGB triplet
    rgbtriplet = struct.unpack('BBB',bytes.fromhex(rgbstr))
    red = rgbtriplet[0]
    green = rgbtriplet[1]
    blue = rgbtriplet[2]
    if red>green and red>blue:
        green= green + (red-green)*1/2
        blue= blue + (red-blue)*1/2
    elif green>blue:
        blue=blue + (green-blue)*1/2
        red= red + (green-red)*1/2
    else:
        red= red + (blue-red)*1/2
        green= green + (blue-green)*1/2
    res = '%02x%02x%02x' % (int(red),int(green),int(blue))
    return res

# Increase shadow of the hexa color
def shadowcolor(rgbstr):
    # Reconstructrion of RGB triplet
    rgbtriplet = struct.unpack('BBB',bytes.fromhex(rgbstr))
    red = rgbtriplet[0]
    green = rgbtriplet[1]
    blue = rgbtriplet[2]

    if red>green and red>blue:
        green= green - (red-green)*1/4
        blue= blue - (red-blue)*1/4
    elif green>blue:
        blue= blue - (green-blue)*1/4
        red= red - (green-red)*1/4
    else:
        red= red - (blue-red)*1/4
        green= green - (blue-green)*1/4
    res = '%02x%02x%02x' % (abs(int(red)),abs(int(green)),abs(int(blue)))
    return res