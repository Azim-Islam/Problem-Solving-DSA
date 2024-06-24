use std::io;
fn main() {
    let mut string = String::new();
    io::stdin().read_line(&mut string).unwrap();
    let n: i64 = string.trim().parse().unwrap();

    for i in (2..n + 1).step_by(2) {
        println!("{}^2 = {}", i, i.pow(2));
    }
}
