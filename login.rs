fn main()
{
    reqwest::blocking::Client::builder()
        .no_proxy()
        .timeout(std::time::Duration::from_millis(100))
        .build()
        .unwrap()
        .post("http://10.10.244.11:801/eportal/?c=ACSetting&a=Login&wlanacip=10.255.252.150")
        .form(&[("DDDDD", ",1,Bxxxxxxxx@njxy"), ("upass", "YOUR_PASSWORD")])
        .send();
}
