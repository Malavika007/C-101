import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token        

    def upload_file(self, file_from, file_to):  
        
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:        
            dbx.files_upload(f.read(), file_to) 

def main():
    access_token = 'sl.BHre_ePiCBKWE5rj-m39Lex4V6RCUN_lGrol1wLwpQ5QeXLyW1Hzp7r50fSQQHEy_Q-Oc2eVTwuUSzt7E2pJjnBbWt4kRIJs5hqnsQmRWt5YJm8ycw7yKjG7SGKdsvT7r1ADWEg'
    transferData = TransferData(access_token)

    file_from = 'test.txt'
    file_to = '/test_dropbox/test.txt  "'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()