import tornado.ioloop
import tornado.web
import socket
import os
import sys
import zlib
import StringIO
import base64
import numpy as np;
import json
from datetime import datetime, date

from rh_icon.common.settings import Settings
from rh_icon.web.viewer import Viewer
from rh_icon.common.utility import Utility;
from rh_icon.common.database import Database


def transform(path):

    print 'converting', path
    names = ["membrane three", "membrane two"]
    annotations = []
    with open(path, 'r') as content_file:
	content = content_file.read()
	data = json.loads( content )
	if len(data) == 0:
	    return

	annotations.append( data[1] )
	annotations.append( data[0] )

    data = json.dumps( annotations )
    with open(path, 'w') as outfile:
	outfile.write(data)

if __name__ == "__main__":
	
    for i in range(20, 80):
	path = '/home/fgonda/icon/data/labels/train-input_00%d.default.json'%(i)
        if os.path.exists( path ):
		transform( path )
