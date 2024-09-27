import io
import os
import pyAesCrypt


def MemoryCrypter(path, is_encrypted):
    sequence_bytes = io.BytesIO()

    with open(path, "rb") as f:
            file_content = io.BytesIO(f.read())
            
    with open(path, "wb") as f:
        if is_encrypted:
            pyAesCrypt.encryptStream( 
            file_content,
            sequence_bytes,
            password,
            bufferSize
            )
        else:
            pyAesCrypt.decryptStream(
                file_content,
                sequence_bytes,
                password,
                bufferSize,
                len(file_content.getvalue())
        )
        f.write(sequence_bytes.getvalue())

bufferSize= 64 * 1024
password = "test12345"

print("[1] - Encrypt\n[2] - Decrypt\n")
method = int(input("->"))
method = True if method == 1 else False

for file in os.listdir("test"):
    MemoryCrypter(
        os.path.join("test", file),
        method
    )