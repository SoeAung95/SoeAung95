import pyotp

# Example Key
secret = "JBSWY3DPEHPK3PXP"
totp = pyotp.TOTP(secret)
print("Your OTP is:", totp.now())
