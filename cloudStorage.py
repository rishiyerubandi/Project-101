import dropbox

class TransferData:
    def __init__(self,accessToken):
        self.accessToken = accessToken

    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.accessToken)

        f = open(file_from, 'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    accessToken = 'sl.A8i4nIsGflPp61KjVjxlh6BqgiR6Eysru_mJCx5mRh6cOdg2q9Vvjofk9KSMNcgPK2yuajjAY9QAEb54kow9dm_UvWTWd9YCpd8tZTVTBOMIvV5rOVzGGPZ7YAEe42PHS8tSrwk'
    transferData = TransferData(accessToken)

    file_from = input("Enter the file path to transfer: ")
    file_to = input("Enter the full path to upload to Dropbox: ")

    transferData.upload_file(file_from, file_to)
    print("File has been moved successfully")
    
main()