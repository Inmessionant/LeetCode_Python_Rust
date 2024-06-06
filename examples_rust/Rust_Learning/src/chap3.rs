fn func3_2() {
    let guess: isize = "32".parse().expect("not a number");
    println!("guess = {}", guess)
}

fn func3_3() {
    let tup = (1, 2, 3);
    let (x, y, z) = tup;
    println!("{} {} {}", x, y, z);
    println!("{} {} {}", tup.0, tup.1, tup.2);

    let a: [i32; 3] = [1, 2, 3];
    let a = [32; 10];

    for (idx, &item) in a.iter().enumerate() {
        print!("{} => {}\n", idx, item)
    }
}

fn func3_4() -> i32 {
    let x = 5;
    println!("before x = {}", x);
    let y = {
        let x = 1;
        println!("inside x = {}", x);
        x + 3
    };
    println!("outside x = {}", x);
    println!("outside y = {}", y);
    5
}

fn func3_5() {
    let number = 11;

    if number < 0 {
        println!("number < 0 number = {}", number);
    } else if number < 10 {
        println!("number < 10 number = {}", number);
    } else {
        println!("default number = {}", number);
    }

    let cur = if number < 100 { 5 } else { 6 };
    println!(" cur = {}", cur);
}

fn func3_6() {
    let mut cnt: i32 = 1000;
    loop {
        println!("cnt = {}", cnt);
        cnt -= 1;
        if cnt == 0 {
            break;
        }
    }

    cnt = 1000;

    while (cnt > 0) {
        println!("cnt = {}", cnt);
        cnt -= 1;
    }

    let a = [10, 20, 30, 40, 50];

    for val in a.iter() {
        println!("val = {}", val);
    }

    for number in (1..5).rev() {
        println!("number = {}", number);
    }
}
