fn main()
{
    reqwest::blocking::Client::builder()
        .no_proxy()
        .timeout(std::time::Duration::from_millis(100))
        .build()
        .unwrap()
        .post("http://10.10.244.11:801/eportal/?c=ACSetting&a=Login&wlanacip=10.255.252.150")


// IMPORTANT!!!
// In the next code line:

// replace "Bxxxxxxxx" and "YOUR_PASSWORD" to your Student ID and password
// replace "@xxxx" to "@cmcc" if you use the NJUPT_CMCC; to "@njxy" if you use NJUPT_CHINANET
// delete "@xxxx" if you use the WLAN NJUPT. (this is not tested)
        .form(&[("DDDDD", ",1,Bxxxxxxxx@xxxx"), ("upass", "YOUR_PASSWORD")])
//                             ######## ####               #############

        .send();
}
