from mediaSecure.encodeB64 import EncodingOptions

instance = EncodingOptions()

# Example usage:
image_file_path = '/path/to/file'
encoded_image = instance.encode_mediaFile(image_file_path)
# Print the encoded image data (in Base64 format)
print(encoded_image)

with open("outPutImage.png", "wb") as f:
    f.write(encoded_image)

# Decode the image and save it to a file
output_file_path = 'output_image.jpg'
instance.decode_mediaFile(encoded_image, output_file_path)

# Decode the image and return it as bytes
decoded_image = instance.decode_mediaFile_toBytes(encoded_image)
print(decoded_image)
