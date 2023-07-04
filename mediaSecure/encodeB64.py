import base64
import os
class EncodingOptions:
    def __init__(self):
        pass

    def encode_mediaFile(self, file_path):
        try:
            # print(os.getcwd())
            with open(file_path, 'rb') as mediaFile:
                file_ext = os.path.splitext(file_path)[1]
                print("Encoding file: ", file_path)
                mediaFile_data = mediaFile.read()
                encoded_data = base64.b64encode(mediaFile_data)
                data = {"state": "Success", "encoded_data": encoded_data, "file_ext": file_ext}
                return encoded_data
        except Exception as e:
            print(e)
            return {"state": "Failed", "error": e}

    def decode_mediaFile(self, encoded_data, output_file_path):
        decoded_data = base64.b64decode(encoded_data)
        with open(output_file_path, 'wb') as output_file:
            output_file.write(decoded_data)
            print("Decoding completed. File saved as", output_file_path)

    def decode_mediaFile_toBytes(self, encoded_data):
        decoded_data = base64.b64decode(encoded_data)
        return decoded_data
