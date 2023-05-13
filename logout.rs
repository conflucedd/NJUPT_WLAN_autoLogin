fn main()
{
    reqwest::blocking::Client::builder()
        .no_proxy()
        .timeout(std::time::Duration::from_millis(50))
        .build()
        .unwrap()
        .post("http://10.10.244.11:801/eportal/?c=ACSetting&a=Logout&wlanacip=10.255.252.150")
        .send();
}
