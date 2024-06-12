pub fn chap8_1_1() {
    let y = vec![1, 2, 3];

    let mut v: Vec<i32> = Vec::new();
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
    let mut v: Vec<i32> = Vec::new();
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

    let s1 = "tic".to_string();
    let s2 = "tac".to_string();
    let s3 = "toe".to_string();

    // let s4 = s1 + "-" + &s2 + "-" + &s3;

    let s4 = format!("{}-{}-{}", s1, s2, s3);
    println!("{}", s4);
}

pub fn chap8_4() {
    let len = "&&sssa".to_string().len();
    print!("{}", len);

    for val in "&&sssa".bytes() {
        print!("{}\n", val);
    }

    for val in "&&sssa".chars() {
        print!("{}\n", val);
    }
}

use ::std::collections::HashMap;

pub fn chap8_5() {
    // let mut socres: HashMap<String, i32> = HashMap::new();
    let mut socres = HashMap::new();
    socres.insert("key1".to_string(), 10);

    for (key, val) in &socres {
        print!("{}: {}\n ", key, val);
    }

    let score = socres.get(&"key1".to_string()); // 获取value

    match score {
        Some(s) => println!("{}\n", s),
        None => println!("team not exit!"),
    }

    // 更新update
    socres.insert("key1".to_string(), 25); // 直接覆盖
    socres.entry("key2".to_string()).or_insert(50);
    socres.entry("key1".to_string()).or_insert(50); // key1存在，不会执行，值还是25

    for (key, val) in &socres {
        print!("{}: {}\n ", key, val);
    }

    // 等价于另外一种写法
    // let teams = vec!["blue".to_string(), "yellow".to_string()];
    // let initial_scores = vec![10, 20];
    // let socres: HashMap<_, _> = teams.iter().zip(initial_scores.iter()).collect();

    // for (key, val) in socres {
    //     print!("{}: {}\n", key, val);
    // }

    let text = "hello world wonderful place hello";

    let mut map = HashMap::new();

    for word in text.split_whitespace() {
        let count = map.entry(word).or_insert(0);
        *count += 1;
    }
    println!("{:#?}", map);

    
}
