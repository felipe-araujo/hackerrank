messages = ['Why did the chicken cross the road?',
'Gb trg gb gur bgure fvqr!']
def decode(message)
    message.chars.map { |c|
        t = (c.ord + 13)
        if c >= 'a' and c<= 'z'
            t.chr > 'z'? (t - ('z'.ord - 'a'.ord + 1)).chr: t.chr
        elsif c >= 'A' and c<= 'Z'
            t.chr > 'Z'? (t - ('Z'.ord - 'a'.ord + 1)).chr: t.chr
        else
           c
        end
    }.join("")
end

def rot13(secret_messages)
  secret_messages.map { |msg| decode(msg) }
end

expected = ["Jul qvq gur puvpxra pebff gur ebnq?",
"To get to the other side!"]
puts(rot13(messages))
puts ''
puts(expected)

puts 'asd fgH?'.chars.map { |c| c}.join("")