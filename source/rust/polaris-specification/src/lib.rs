pub mod v1 {
    // The name "messages" corresponds with the `package` name in the `.proto`
    // include!(concat!(env!("OUT_DIR"), "/v1.rs"));
    include!("v1.rs");
}
pub fn add(left: usize, right: usize) -> usize {
    left + right
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let result = add(2, 2);
        assert_eq!(result, 4);
        println!("result: {}", result);
        println!("result: {}", env!("OUT_DIR"));
        println!("result: {}", concat!(env!("OUT_DIR"), "/v1.rs"))
    }
}
