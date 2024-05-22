use std::{io, iter::Enumerate};
use rand::Rng;
use std::cmp::Ordering;

fn largest<T: PartialOrd + Copy>(list: &[T]) -> T {
    let mut largest = list[0];

    for &item in list.iter() {
        if item > largest {
            largest = item;
        }
    }

    largest
}

fn fnc1() {
    let number_list = vec![34, 50, 25, 100, 65];

    let result = largest(&number_list);
    println!("The largest number is {}", result);

    let char_list = vec!['y', 'm', 'a', 'q'];

    let result = largest(&char_list);
    println!("The largest char is {}", result);


    let secrect_number = rand::thread_rng().gen_range(1, 100); // [1, 100)
    print!("rand_number is: {}\n", secrect_number);

    loop {
        println!("please input a number:[0, 100)");
        let mut guess = String::new();
        io::stdin().read_line(&mut guess).expect("can't read a number!");

        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => {
                println!("invaild number, please input a number again!");
                continue
            }
        };
        print!("you guess numvber is: {}\n", guess);

        match guess.cmp(&secrect_number) {
            Ordering::Less => println!("guess_number {} is smaller than secrect number {}", guess, secrect_number),
            Ordering::Equal => println!("guess_number {} is equal to secrect number {}", guess, secrect_number),
            Ordering::Greater => println!("guess_number {} is larger than secrect number {}", guess, secrect_number),
        }
    }
}

fn fnc2() {

    const MAX_ITEAMS: i32 = 10000;
    println!("const MAX_ITEAMS = {}", MAX_ITEAMS);

    let mut x = 2;
    println!("x = {}", x);
    x = 10;
    println!("x = {}", x);
}

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

fn first_world(s: &String) -> usize {
    let bytes = s.as_bytes();

    for (i, &item) in bytes.iter().enumerate() {
         if item == b' ' {
            return i;
         }
    }
    s.len()
}

fn func3_4() {
    let s = String::from("Hello world");
    let idx = first_world(&s);
    println!("{}", idx);

}

fn main() {
    func3_4();

}