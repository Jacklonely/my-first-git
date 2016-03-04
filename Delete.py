#coding=gbk

import os
from os import listdir
from os.path import isfile, join

CheckDirs = {}

def RegisterCheckDirs(tab, SrcDir, TargetDir):
	global CheckDirs
	CheckDirs[tab] = {}
	CheckDirs[tab]['SrcDir'] = SrcDir
	CheckDirs[tab]['TargetDir'] = TargetDir

def DeletedUnusedEsqlFiles():
	def getFileListsInDir(dir):
		return [ f for f in listdir(dir) if isfile(join(dir,f)) ]
	
	global CheckDirs
	for key in CheckDirs.keys():
		SourceDir = CheckDirs[key]['SrcDir']
		TargetDir = CheckDirs[key]['TargetDir']
		
		esql_files = getFileListsInDir(SourceDir)
		files = getFileListsInDir(TargetDir)

		for fileName in files:
			if fileName not in esql_files:
				absFilePath = os.path.join(TargetDir, fileName)
				print 'deleting file: ', absFilePath
				cmd = 'del %s' %(absFilePath)
				os.system(cmd)

def main():
	DeletedUnusedEsqlFiles()

if __name__ == '__main__':
	main()
