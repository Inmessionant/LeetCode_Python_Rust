

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