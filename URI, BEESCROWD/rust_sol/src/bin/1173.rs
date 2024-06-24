use std::{io};

fn main(){
    let mut inp = String::new();
    io::stdin().read_line(&mut inp).unwrap();
    
    let mut num: i64 = inp.trim().parse().unwrap();

    let mut arr_fill : [i64; 10] = [0; 10];

    for i in (0..10){
        arr_fill[i] = num;
        println!("N[{}] = {}", i, num);
        num = num*2;
    }

}