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
      def reverse_list(list) do
            case list do                  
                  [] -> []
                  [h | t] -> reverse_list(t) ++ [h]
            end
      end
end 

array = Console.read_until_eof()
Solution.reverse_list(array)
      |> Enum.each(fn n -> IO.puts(n) end)