use std::io;

fn main() -> io::Result<()>{
    let mut input_s = String::new();
    io::stdin().read_line(&mut input_s)?;
    let mut input_vec = input_s.split();
    Ok(())
}