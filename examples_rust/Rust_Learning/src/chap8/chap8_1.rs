

pub fn chap8_1_1() {
    
    let y = vec![1, 2, 3];

    let mut v:Vec<i32> = Vec::new();
    v.push(12);
    v.push(120);

    for val in &v {
        println!("{}", val);
    }

    println!("{}", &v[1]);

    match v.get(120) {
        Some(x) => println!("match {}", x),
        None => println!("there is no 120"),
    }

}

pub fn chap8_1_2() {
    let mut v:Vec<i32> = Vec::new();
    v.push(12);
    v.push(120);

    for val in &mut v {
        *val += 50;
        println!("{}", val);
    }
}

enum SpreadsheetCell {
    Int(i32),
    Float(f64),
    Test(String),
}

pub fn chap8_1_3() {
    let row = vec![
        SpreadsheetCell::Int(3),
        SpreadsheetCell::Float(10.12),
        SpreadsheetCell::Test(String::from("blue")),
    ];
}

pub fn chap8_3() {
    let data = "initial contents".to_string();
    let data1 = String::from("initial contents");
    println!("{} == {}", data, data1);

    let mut s = "foo".to_string();
    s.push_str(" bar");
    println!("{}", s);

    s.push('l'); // char
    println!("{}", s);

    let s1 = "hello, ".to_string();
    let s2 = "world!".to_string();
    let s3 = s1 + &s2;
    println!("{}", s3);
    // println!("{} {}", s1, s2); 
}