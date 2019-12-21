# PhotoFrame
A "smart" photo viewing application.
The program displays images stored in the PHOTO_DIR directory. Once a day the program downloads all photos from the Google Drive folder of your choice, into the PHOTO_DIR directory. This allows you to give the photo frame to a loved one, and then update the pictures on the frame remotely. 

# Install
This software requires Python3 to run.
To install the dependencies by running `pip3 install -r requirements.txt`.
Then you will need to set up the downloader. 
Create a directory to hold the photos and set PHOTO_DIR in photoframe.py accordingly. 
Create a folder in Google Drive to remotely store the photos as well. Take the ID of this folder found in the URL, and change FOLDER_ID in downloader.py accordingly. 
The downloader code is based on the quickstart code provided by Google, you can set up the credentials for the API by following the first step in this guide: https://developers.google.com/drive/api/v3/quickstart/python.
Now you should run the downloader, `python3 downloader.py`, to ensure that it is working as expected. You can add any files you want to the Google Drive folder and they should be downloaded to PHOTO_DIR. 
You can now run `python3 photoframe.py` and the photoframe will run!
