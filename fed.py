import base64

print base64.b64encode("password")
cGFzc3dvcmQ=

print base64.b64decode("cGFzc3dvcmQ=")
password
