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
      def sum_of_odd(list) do
            list              
              |> Enum.filter(fn(x) -> rem(x, 2) != 0 end)              
              |> Enum.sum
      end
end

array = Console.read_until_eof()
ans = Solution.sum_of_odd(array)
IO.puts(ans)