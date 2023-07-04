import base64
import os


class MediaSecureError(Exception):
    """Custom exception for mediaSecure package errors."""


class EncodingOptions:
    def __init__(self):
        pass

    def encode_mediaFile(self, file_path):
        try:
            if not os.path.isfile(file_path):
                raise MediaSecureError(f"File not found at path: {file_path}")

            with open(file_path, 'rb') as mediaFile:
                file_ext = os.path.splitext(file_path)[1]
                print("Encoding file:", file_path)
                mediaFile_data = mediaFile.read()
                encoded_data = base64.b64encode(mediaFile_data)
                data = {"state": "Success", "encoded_data": encoded_data, "file_ext": file_ext}
                return encoded_data

        except Exception as e:
            raise MediaSecureError(f"Encoding failed: {str(e)}")

    def decode_mediaFile(self, encoded_data, output_file_path):
        try:
            decoded_data = base64.b64decode(encoded_data)

            with open(output_file_path, 'wb') as output_file:
                output_file.write(decoded_data)
                print("Decoding completed. File saved as", output_file_path)

        except Exception as e:
            raise MediaSecureError(f"Decoding failed: {str(e)}")

    def decode_mediaFile_toBytes(self, encoded_data):
        try:
            decoded_data = base64.b64decode(encoded_data)
            return decoded_data

        except Exception as e:
            raise MediaSecureError(f"Decoding to bytes failed: {str(e)}")
