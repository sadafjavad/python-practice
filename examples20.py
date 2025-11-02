# Convert string to bytes
text = "hello"
byte_data = text.encode("utf-8")
if isinstance(byte_data,bytes):
    print(byte_data)
else:
    print("conversion failed")
    