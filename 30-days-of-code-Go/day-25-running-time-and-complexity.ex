defmodule Solution do
  def is_prime(n) do
    case n do
      1 -> false
      2 -> true
      _ -> is_prime(n, 2)
    end

  end

  def is_prime(n, acc) when n > 2 do
    cond do
      :math.sqrt(n) < acc ->
        true
      rem(n, acc) == 0 ->
        false
      true ->
        is_prime(n, acc+1)
    end
  end
end


size = IO.read(:stdio, :line)
  |> String.trim
  |> String.to_integer

array = Enum.to_list(1..size)
  |> Enum.map(fn _ -> IO.read(:stdio, :line) end)
  |> Enum.map(&String.trim/1)
  |> Enum.map(&String.to_integer/1)

array
  |> Enum.map(&Solution.is_prime/1)
  |> Enum.map(fn prime -> if(prime, do: 'Prime', else: 'Not prime') end)
  |> Enum.each(&IO.puts/1)
