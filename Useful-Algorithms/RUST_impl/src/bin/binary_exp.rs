fn bin_pow(mut a :i128, mut n :i128) -> i128{
    let mut result :i128 = 1;
    while n > 0{
        if n&1 == 1{
            result = result*a;
        }
        a = a*a;
        n = n>>1;
    }
    return result;
}
fn main(){
    println!("{}", bin_pow(3, 4));
}