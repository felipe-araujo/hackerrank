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

array = Console.read_until_eof()

array
    |> Enum.map(fn t -> abs(t) end)
    |> Enum.each(fn t -> IO.puts(t) end)
