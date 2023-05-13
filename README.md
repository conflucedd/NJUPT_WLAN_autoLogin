# NJUPT_WLAN_autoLogin
A powerful python and rust script for auto login the NJUPT campus network.

# KNOWN ISSUE
When you log out from devices logged in with this method, all devices under the account logged in with the method will be logged out at the same time.

If you use the classic method, namely, the p.njupt.edu.cn, foregoing will not happen.

MAY HAVE OTHER DANGEROUS BUGS.

# GUIDE FOR PYTHON
Install python and add it to path, then run "pip install requests" in command-line tools.

View the source code for your operating system and made necessary changes.

The only thing you need to change is the Student ID, your password, and your network provider.

Run it and see if it works.

We test the ChinaNet and CMCC, and those is supported.

# GUIDE FOR RUST
[dependencies]

reqwest = { version = "0.11.17", features = ["blocking"] }
