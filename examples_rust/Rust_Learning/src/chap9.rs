use std::{fs::File, io::{self, ErrorKind, Read}};

use std::error::Error;

pub fn chap9_1() {
    // panic!("run and crush");
    let v = vec![1, 2, 3];
    // v[9]; index out of bounds: the len is 3 but the index is 9
}
enum Result<T, E> {
    Ok(T),
    Err(E),
}
pub fn chap9_2() {
    // 等效于 let f = File::open("hello.txt").unwrap();
    // let f = File::open("hello.txt");

    // let f = match f {
    //     Ok(file) => {println!("opening file {:?} success", file); file},
    //     Err(error) => match error.kind() {
    //         ErrorKind::NotFound => match File::create("hello.txt") {
    //             Ok(fc) => fc,
    //             Err(e) => panic!("error creating file {:?}", e),
    //         },
    //         other_error => panic!("error opening the file {:?}", other_error),
    //     }
    // };

    let f = File::open("hello.txt").expect("can't open file");
}

pub fn chap9_3() {
    // fn read_username_from_file() -> Result<(), Box<dyn Error>> {
    //     let f = File::open("hello.txt");

    //     let mut f = match f {
    //         Ok(file) => file,
    //         Err(e) => return Err(e),
    //     };

    //     let mut s = String::new();
    //     f.read_to_string(& mut s);
    //     Ok(s);
    //     match f.read_to_string(& mut s) {
    //         Ok(_) => Ok(s),
    //         Err(e) => Err(e),
    //     }
    // }
}
