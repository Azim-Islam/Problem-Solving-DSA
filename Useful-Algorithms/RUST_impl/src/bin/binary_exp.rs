fn bin_pow(mut a :i64, mut n :i64) -> i64{
    let mut result :i64 = 1;
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
    println!("{}", bin_pow(3, 13));
}