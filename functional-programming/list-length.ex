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

defmodule Solution do
    def size(array) do
        case array do
            [] -> 0
            [_h | t] -> 1 + size(t)
        end
    end

end
array = Console.read_until_eof()
IO.puts(Solution.size(array))
