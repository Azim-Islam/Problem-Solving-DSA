fn main(){
    for i in (2..101).step_by(2){
        if i%2 == 0{
            println!("{}", i);
        }
    }
}