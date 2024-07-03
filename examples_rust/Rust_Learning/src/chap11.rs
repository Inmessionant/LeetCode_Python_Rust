
mod tests {
    #[test]
    pub fn chap11() {
        assert_eq!(2+2, 4);
    }

    #[test]
    pub fn another() {
        // panic!("tests failed.");
    }
}
    

pub fn chap11_1() {
    assert_eq!(2+2, 4);
}

pub fn chap11_2() {
    assert_eq!(2 + 2, 4); // equal
    assert_ne!(1, 2);  // not equal
}

pub fn chap11_3() {
    assert!(1==2, "1 != 2"); // 第2个参数为自定义信息
    assert_eq!(2 + 2, 4); // equal，第3个参数为自定义信息
    assert_ne!(1, 2);  // not equal
    format!("hello {}", "JL"); // 拼接字符串
}

pub fn chap11_5() {
    #[test]
    fn it_works() -> Result<(), String>{
        if 2 + 2 == 4 {
            Ok(())
        } else {
            Err(String::from("2 + 2 != 4"))
        }
    }
}