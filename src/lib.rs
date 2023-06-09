pub mod v1;

#[test]
fn it_works() {
    println!("ok");
    let r = v1::ConfigSimpleResponse {
        code: Some(0),
        info: Some("success".to_string()),
    };

    println!("{:?}", r);
}
