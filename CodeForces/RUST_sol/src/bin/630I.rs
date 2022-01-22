use std::{io};

fn main(){
    let mut s = String::new();
    io::stdin().read_line(&mut s).unwrap();
    let n: i64 = s.trim().parse().unwrap();
    let p1: i64 = 2*3*(4 as i64).pow((n-2) as u32);
    let p2: i64 = (n-3)*4*3*3*(4 as i64).pow((n-4).abs() as u32);
    println!("{}", p1+p2);
}