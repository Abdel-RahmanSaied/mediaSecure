from mediaSecure.encodeB64 import EncodingOptions
import os

# Example usage:
if __name__ == "__main__":
    # Initialize an instance of EncodingOptions
    instance = EncodingOptions()

    # Example 1: Encoding a media file
    image_file_path = '/mnt/WorkDisk/@projects/mediaEncryptor/191.png'
    encoded_image = instance.encode_mediaFile(image_file_path)
    print(encoded_image.keys())
    if encoded_image["state"] == "Success":
        print("Encoding successful.")
        file_ext = encoded_image["file_ext"]
        # Print the encoded image data (in Base64 format)
        # print(encoded_image["encoded_data"])
        # Save the encoded image to a file
        output_file_path = f'encoded_image{file_ext}'
        with open(output_file_path, 'w') as f:
            f.write(encoded_image["encoded_data"].decode())

    else:
        print("Encoding failed. Error:", encoded_image["error"])

    # Example 2: Decoding the image and saving it to a file
    if encoded_image["state"] == "Success":
        output_file_path = 'decoded_image.jpg'
        try:
            instance.decode_mediaFile(encoded_image["encoded_data"], output_file_path)
            print("Decoding successful. Image saved as", output_file_path)
        except Exception as e:
            print("Decoding failed. Error:", str(e))

    # Example 3: Decoding the image and returning it as bytes
    if encoded_image["state"] == "Success":
        try:
            decoded_image = instance.decode_mediaFile_toBytes(encoded_image["encoded_data"])
            print("Decoding to bytes successful.")
            # print(decoded_image)
        except MediaSecureError as e:
            print("Decoding to bytes failed. Error:", str(e))
