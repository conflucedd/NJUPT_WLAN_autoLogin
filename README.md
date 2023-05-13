# NJUPT_WLAN_autoLogin
A powerful python and rust script for auto login the NJUPT campus network.

# KNOWN ISSUE
When you log out from devices logged in with this method, all devices under the account logged in with the method will be logged out at the same time.

If you use the classic method, namely, the p.njupt.edu.cn, foregoing will not happen.

MAY HAVE OTHER DANGEROUS BUGS.

# GUIDE FOR PYTHON
run "pip install requests" to satisfy dependencies

View the source code and made necessary changes.

The only thing you need to change is the Student ID, your password, and your network provider.

# GUIDE FOR RUST
[dependencies]
reqwest = { version = "0.11.17", features = ["blocking"] }
