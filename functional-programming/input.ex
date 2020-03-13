defmodule Console do

    def read_until_eof() do
        read_until_eof([])
    end

    def read_until_eof(acc) do
        case IO.read(:stdio, :line) do
            :eof ->
                acc
            data -> 
                acc = acc ++ [String.to_integer(String.trim(data))]            
                read_until_eof(acc)
        end
    end
end

IO.inspect(Console.read_until_eof())