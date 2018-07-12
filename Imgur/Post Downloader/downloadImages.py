from imgurpython import ImgurClient
from hurry.filesize import size
from urllib.request import urlretrieve
import urllib, os, zipfile, signal, sys, yaml, time

def yamlInfo():
	fstream = open('creds.yaml', 'r')
	conf = yaml.load(fstream)
	client_id = conf["credentials"]["client_id"]
	client_secret = conf["credentials"]["client_secret"]
	return [client_id, client_secret]

def signal_handle( signal, handle ):
	print(' Exiting application...')
	sys.exit(0)

def albumParse( client, albumList, postInfo ):
	totalDownloadSize = 0
	postDownloadSize = 0
	urlAndfilePath = {}
	for album in albumList:
		albumInfo = client.get_album(album)
		images = client.get_album_images(album)

		postDownloadSize, urlAndfilePath = imageParser(images, albumInfo.title, urlAndfilePath)
		postInfo[albumInfo.title] = [albumInfo.images_count, albumInfo.link, postDownloadSize, urlAndfilePath]

		totalDownloadSize += postDownloadSize
	return totalDownloadSize, postInfo

def imageParser( images, title, urlAndfilePath ):
	imageSize = 0
	urlAndfilePath = {}
	for image in images:
		extn = image.type.split('/')
		fileNm = image.id + "." + extn[1]
		filePath = title + "/" + fileNm
		urlAndfilePath.update({image.link : filePath})

		imageSize = image.size + imageSize
	return imageSize, urlAndfilePath

def warnUser( downloadSize ):
	yesOrNo = input("Warning: You are about to download " + size(downloadSize) + "B. Proceed? (Y/N)")
	if yesOrNo == "Y" or yesOrNo == "y":
		print("Proceeding...")
	elif yesOrNo == "N" or yesOrNo == "n":
		sys.exit(0)
	else:
		print("Your response (" + yesOrNo + ") was not one of the expected responses: (Y,N)")
	return

def makeDir( dirName ):
    if not os.path.exists(dirName):
	    os.makedirs(dirName)
    return

def makeMetadataFile( title, numImages, postLink, postSize ):
	readme = title + "/" + title + ".txt"
	file = open(readme, "w")
	file.write(str(numImages) + " (" + str(size(postSize)) + ") images downloaded from " + postLink)
	file.close()
	return

def downloadImages( imageDict ):
	for key, val in imageDict.items():
		urlretrieve(key, val)

def creditsLeft( client ):
	credits = client.get_credits()
	userRemain, userLimit = credits['UserRemaining'], credits['UserLimit']
	clientRemain, clientLimit = credits['ClientRemaining'], credits['ClientLimit']
	timeLeft = credits['UserReset'] - time.time()
	print(str(userRemain) + "/" + str(userLimit) + " available used and " + str(clientRemain) + "/" + str(clientLimit) + " resets in " + str(time.strftime("%H hours, %M minutes, %S seconds", time.gmtime(timeLeft))) )

def main():
	#in case program interrupts with ctrl+c or ctrl+z
	signal.signal(signal.SIGINT, signal_handle)
	signal.signal(signal.SIGTSTP, signal_handle)

	#yaml file for connecting to imgur api
	idcred, secret = yamlInfo()
	client = ImgurClient(idcred, secret)

	#get bunch of urls here somehow
	albumList = ["VoPI3xV", "VWbSynt"]
	postInfo = {}
	totalDownloadSize, postInfo = albumParse(client, albumList, postInfo)

	#tell user total download size
	warnUser(totalDownloadSize)

	#make dir, metadata file, dl images
	for key, val in postInfo.items():
		makeDir(key)
		makeMetadataFile(key, val[0], val[1], val[2])
		downloadImages(val[3])

	#leftover credits
	creditsLeft(client)
main()
