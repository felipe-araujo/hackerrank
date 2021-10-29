fn main(){

    print!("{} days", 31);
    println!("");
    
    // prints to stderr
    eprintln!("Error!");

    println!("J'ai bu chaque {} de ton esprit {} et je me suis couché {}", 
            "mot", "fou", "ivre");

    // named parameters
    println!("Hier enconre j'avais {age} ans", age=20);
}