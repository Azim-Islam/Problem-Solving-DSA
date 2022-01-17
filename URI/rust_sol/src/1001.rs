use std::io;

fn input_integer(input_txt: &mut String) -> i32{
    io::stdin().read_line(input_txt).expect("ERROR");
    let x : i32 = input_txt.trim().parse().expect("WOW");
    input_txt.clear();
    return x;
}

fn main(){
    let mut input_text = String::new();

    let x = input_integer(&mut input_text);
    let y = input_integer(&mut input_text);

    println!("X = {}", x+y);
}