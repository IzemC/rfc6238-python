import hmac
import time
import math

mode = 'sha512'
length = 10
T0 = 0
X = 30
T = time.time()
# steps = math.floor((T - T0)//X)
steps = 20000000000//X
msg = steps.to_bytes(8, 'big')
seed64 = "31323334353637383930313233343536373839303132333435363738393031323334353637383930313233343536373839303132333435363738393031323334"
key = int(seed64, 16).to_bytes(64, 'big')
hash = hmac.new(key, msg=msg, digestmod=mode).digest()
offset = hash[len(hash)-1] & 0xF
binary = ((hash[offset] & 0x7f) << 24) | ((hash[offset + 1] & 0xff) <<
                                          16) | ((hash[offset + 2] & 0xff) << 8) | (hash[offset + 3] & 0xff)
mask = pow(10, length)
otp = str(binary % mask)
otp = ('0'*(length-len(otp))) + otp
print(otp)
