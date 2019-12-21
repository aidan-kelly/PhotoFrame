from __future__ import print_function
import pickle
import os.path
import io
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaIoBaseDownload
import photoframe

# If modifying these scopes, delete the file token.pickle.
# This scope gives us read and download privileges.
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
FOLDER_ID = "13GLStO44I77rrVfWOaYWo6Y81g8Gkm6V"

def main():
    """Shows basic usage of the Drive v3 API.
    Downloads all files founds in a folder specified.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)

    # Call the Drive v3 API
    # Lists off all files in the folder.
    results = service.files().list(
        q= f"'{FOLDER_ID}' in parents", fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])

    # Download all files in the folder.
    print(f"\nStarting download! {len(items)} files found.")
    for item in items:
        file_id = item['id']
        file_name = item['name']

        print(f" [+] Downloading {file_name}.")

        #download the file
        request = service.files().get_media(fileId=file_id)
        fh = io.FileIO(f"{photoframe.PHOTO_DIR}/{file_name}", 'wb')
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
    print(f"Download complete!\n")



if __name__ == '__main__':
    main()