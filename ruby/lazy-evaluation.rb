# Enter your code here. Read input from STDIN. Print output to STDOUT
def is_prime?(n)
    root = Math.sqrt(n)
    i = 2
    while i <= root do
        if n % i == 0 then 
            return false 
        end
        i = i + 1
    end
    return true
end

def is_palindrome?(n)
    s = n.to_s()    
    s == s.reverse     
end

n = gets().to_i()
p 1.upto(Float::INFINITY).lazy.select{|x| is_palindrome?(x)}.select{|x| is_prime?(x)}.first(n)
