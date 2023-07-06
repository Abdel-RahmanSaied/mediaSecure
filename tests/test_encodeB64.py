import os
import base64
import tempfile
import pytest
from mediaSecure.encodeB64 import EncodingOptions, MediaSecureError

# export PYTHONPATH="/mnt/WorkDisk/@projects:$PYTHONPATH"

@pytest.fixture
def encoding_options():
    return EncodingOptions()


def test_encode_mediaFile(encoding_options):
    # Create a temporary file with some content
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b'Test data')
        file_path = temp_file.name

    try:
        # Encode the temporary file
        encoded_data = encoding_options.encode_mediaFile(file_path)

        # Verify the encoded data
        assert encoded_data["state"] == "Success"
        assert encoded_data["encoded_data"] == base64.b64encode(b'Test data')
        assert encoded_data["file_ext"] == os.path.splitext(file_path)[1]
    finally:
        # Clean up the temporary file
        os.remove(file_path)


def test_decode_mediaFile(encoding_options):
    # Create a temporary file and encode its contents
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b'Test data')
        encoded_data = base64.b64encode(b'Test data')

    try:
        # Decode the encoded data to a temporary output file
        with tempfile.NamedTemporaryFile(delete=False) as output_file:
            output_file_path = output_file.name
            encoding_options.decode_mediaFile(encoded_data, output_file_path)

            # Verify the output file's contents
            with open(output_file_path, 'rb') as f:
                assert f.read() == b'Test data'
    finally:
        # Clean up the temporary files
        os.remove(temp_file.name)
        os.remove(output_file_path)


def test_encode_mediaFile_file_not_found(encoding_options):
    # File path that does not exist
    file_path = '/path/to/nonexistent/file.txt'

    # Verify that MediaSecureError is raised with the appropriate error message
    with pytest.raises(MediaSecureError) as e:
        encoding_options.encode_mediaFile(file_path)
    assert str(e.value) == f"File not found at path: {file_path}"
    # assert str(e.value) == f"Encoding failed:  {file_path}"


def test_decode_mediaFile_decoding_failed(encoding_options):
    # Invalid encoded data
    encoded_data = 'invalid_base64_data'

    # Output file path
    output_file_path = '/path/to/output/file.txt'

    # Verify that MediaSecureError is raised with the appropriate error message
    with pytest.raises(MediaSecureError) as e:
        encoding_options.decode_mediaFile(encoded_data, output_file_path)
    assert str(e.value) == f"Decoding failed: Incorrect padding"


def test_decode_mediaFile_toBytes(encoding_options):
    # Encoded data
    encoded_data = base64.b64encode(b'Test data')

    # Decode the encoded data to bytes
    decoded_data = encoding_options.decode_mediaFile_toBytes(encoded_data)

    # Verify the decoded data
    assert decoded_data == b'Test data'